"""
The project is used to create a .html file as the user's OJ annual report.

This is the main file, which is used to run the project.

"""

import json
from datetime import datetime
import oj_website
import submit_processor
import html_generater


def main():
    # create an OJ_Website object
    oj = oj_website.OJ_Website()

    # get the user's information from the OJ website
    data = oj.get_data()

    # process the user's information
    if data['next'] is not None:
        print(f"Warning: The number of submits exceeds 800. The data may be incomplete.")
    total_submits = data['count']
    submits = data['results']
    submit_info = submit_processor.process_submits(submits)
    code_info = submit_processor.process_codes(submit_info['codes'])
    print(f"Total submits: {total_submits}")

    # delete codes to save space
    submit_info.pop('codes')

    # get deadline information from file
    deadlinestring = {}
    with open('deadlines.json', 'r') as f:
        deadlinestring = json.load(f)
    deadlines = {}
    for problem in deadlinestring:
        deadlines[problem] = datetime.strptime(deadlinestring[problem], '%Y-%m-%d')
    
    # calculate total score
    total_score = 0
    for problem in submit_info['submit_problems']:
        # get the date information and order the list from the earliest to the latest
        deadline = deadlines[problem]
        dates_after_deadline = []
        for datestring in submit_info['submit_problems'][problem]['dates']:
            date = datetime.strptime(datestring, '%Y-%m-%d')
            pass_deadline = date - deadline if date > deadline else 0
            for i in range(submit_info['submit_problems'][problem]['dates'][datestring]):
                dates_after_deadline.append(pass_deadline)
        dates_after_deadline.sort()

        # from end to top, search for the highest score
        highest_score = 0
        for i in range(len(submit_info['submit_problems'][problem]['scores'])):
            pass_deadline = dates_after_deadline[i]
            if pass_deadline == 0:
                if submit_info['submit_problems'][problem]['scores'][len(submit_info['submit_problems'][problem]['scores']) - i - 1] > highest_score:
                    highest_score = submit_info['submit_problems'][problem]['scores'][len(submit_info['submit_problems'][problem]['scores']) - i - 1]
            elif pass_deadline < 10:
                if submit_info['submit_problems'][problem]['scores'][len(submit_info['submit_problems'][problem]['scores']) - i - 1] * pass_deadline / 10 > highest_score:
                    highest_score = submit_info['submit_problems'][problem]['scores'][len(submit_info['submit_problems'][problem]['scores']) - i - 1] * pass_deadline / 10
            else:
                break
        
        total_score += highest_score
        submit_info['submit_problems'][problem]['get_score'] = highest_score * 0.04

    total_score /= 25
    submit_info['total_score'] = total_score
    
    # save the user's information to a .json file
    all_info = {
        'submit_info': submit_info,
        'code_info': code_info,
    }
    with open('result.json', 'w') as f:
        json.dump(all_info, f)
    
    # generate the .html file
    html_generater.generate_html(submit_info, code_info)



if __name__ == '__main__':
    main()

