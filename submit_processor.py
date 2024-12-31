"""
This project is used to create a .html file as the user's OJ annual report.

This module is all functions that are used to process the user's information.

"""

import json
from datetime import datetime

def process_submits(submits: list) -> dict:
    """
    Process the user's submits.

    :param submits: The user's submits.
    :return:        The user's submits in a dictionary, in format {
                        `"user"`: the user's outer id,
                        `"submit_indexs"`: the list of the submit's id,
                        `"submit_problems"`: the dictionary of the submit's problems, in format {
                            `problem_id`: {
                                `"title"`: the problem's title in Chinese,
                                `"submits"`: the list of the submit's id,
                                `"languages"`: the dictionary of the submit's languages, in format {
                                    `"language"`: the number of submits in given language,
                                    ...
                                },
                                `"scores"`: the list of the submit's score,
                                `"highest_score"`: the highest score of the problem,
                                `"dates"`: the dictionary of the submit's dates, in format {
                                    `"YYYY-MM-DD"`: the number of submits,
                                    ...
                                },
                                `"times"`: the dictionary of the submit's times, in format {
                                    `"HH"`: the number of submits,
                                    ...
                                },
                                `"errors"`: the number of compile errors,
                            },
                            ...
                        },
                        `"submit_languages"`: the dictionary of the submit's languages, in format {
                            `"C++11"`: the number of C++11 submits,
                            ...
                        },
                        `"compile_errors"`: the list of the compile errors, in format {
                            `"id"`: the submit's id,
                            `"problem"`: the problem's id,
                            `"problem_title"`: the problem's title in Chinese,
                            `"language"`: the version of the compiler used,
                            `"error_message"`: compile error message,
                        },
                        `"codes"`: the list of the code submitted,
                        `"scores"`: the list of the score,
                        `"create_times"`: the dictionary of the submit's times, in format {
                            `"HH"`: the number of submits,
                            ...
                        },
                        `"create_dates"`: the dictionary of the submit's dates, in format {
                            `"YYYY-MM-DD"`: the number of submits,
                            ...
                        },
                    }

    The format of the user's each submit: {
        `"id"`: the submit's id,
        `"user"`: the user's inner id,
        `"user_username"`: the user's outer id,
        `"problem"`: the problem's id,
        `"problem_title"`: the problem's title in Chinese,
        `"language"`: the version of the compiler used,
        `"code"`: the code submitted,
        `"judge_status"`: the status of the submit, "C" for completed,
        `"compile_status"`: the status of the compiler, "O" for OK, "E" for error,
        `"run_results"`: the results of the 10 test cases, in format `[[result, time (ms), memory (KB)], ...]`,
        `"error_message"`: compile error message,
        `"score"`: the score of the submit,
        `"create_time"`: the time of the submit, in format "YYYY-MM-DDTHH:MM:SS.000000Z"
    }

    """
    print(f"Processing the user's submits ...")

    user = submits[0]['user_username']
    submit_indexs = []
    submit_problems = {}
    submit_languages = {}
    compile_errors = []
    codes = []
    scores = []
    create_times = {}
    create_dates = {}

    for submit in submits:
        # get the submit's id
        submit_indexs.append(submit['id'])
        # get the language of the submit
        if submit['language'] not in submit_languages:
            submit_languages[submit['language']] = 1
        else:
            submit_languages[submit['language']] += 1
        # get the code of the submit
        codes.append(submit['code'])
        # get the score of the submit
        scores.append(submit['score'])
        # get the date and time of the submit
        create_date_time = datetime.strptime(submit['create_time'], "%Y-%m-%dT%H:%M:%S.%fZ")
        date = create_date_time.strftime("%Y-%m-%d")
        if date not in create_dates:
            create_dates[date] = 1
        else:
            create_dates[date] += 1
        time = create_date_time.strftime("%H")
        if time not in create_times:
            create_times[time] = 1
        else:
            create_times[time] += 1
        # get the compile error message
        if submit['compile_status'] == "E":
            compile_errors.append({
                "id": submit['id'],
                "problem": submit['problem'],
                "problem_title": submit['problem_title'],
                "language": submit['language'],
                "error_message": submit['error_message'],
            })
        # get the problem's id
        if str(submit['problem']) not in submit_problems:
            submit_problems[str(submit['problem'])] = {
                "title": submit['problem_title'],
                "submits": [submit['id']],
                "languages": {submit['language']: 1},
                "scores": [submit['score']],
                "highest_score": submit['score'],
                "dates": {date: 1},
                "times": {time: 1},
                "errors": (1 if submit['compile_status'] == "E" else 0),
            }
        else:
            submit_problems[str(submit['problem'])]['submits'].append(submit['id'])
            if submit['language'] not in submit_problems[str(submit['problem'])]['languages']:
                submit_problems[str(submit['problem'])]['languages'][submit['language']] = 1
            else:
                submit_problems[str(submit['problem'])]['languages'][submit['language']] += 1
            submit_problems[str(submit['problem'])]['scores'].append(submit['score'])
            submit_problems[str(submit['problem'])]['highest_score'] = max(submit_problems[str(submit['problem'])]['highest_score'], submit['score'])
            if date not in submit_problems[str(submit['problem'])]['dates']:
                submit_problems[str(submit['problem'])]['dates'][date] = 1
            else:
                submit_problems[str(submit['problem'])]['dates'][date] += 1
            if time not in submit_problems[str(submit['problem'])]['times']:
                submit_problems[str(submit['problem'])]['times'][time] = 1
            else:
                submit_problems[str(submit['problem'])]['times'][time] += 1
            if submit['compile_status'] == "E":
                submit_problems[str(submit['problem'])]['errors'] += 1
    
    print(f"Process the user's submits successfully.")

    return {
        "user": user,
        "submit_indexs": submit_indexs,
        "submit_problems": submit_problems,
        "submit_languages": submit_languages,
        "compile_errors": compile_errors,
        "codes": codes,
        "scores": scores,
        "create_times": create_times,
        "create_dates": create_dates,
    }

def process_codes(codes: list) -> dict:
    """
    Process the user's codes.

    :param codes:   The user's codes.
    :return:        The user's code information in a dictionary, in format {
                        `"libraries"`: the dictionary of the used libraries, in format {
                            `library`: the number of used library,
                            ...
                        },
                        `"code_length"`: the dictionary of the code's length, in format {
                            `length`: the number of code,
                            ...
                        },
                        `"total_lines"`: the total number of lines of the code,
                        `"total_chars"`: the total number of characters of the code,

    """
    print(f"Processing the user's codes ...")

    libraries = {}
    code_length = {}
    total_lines = 0
    total_chars = 0
    for code in codes:
        lines = code.split('\n')
        # decect all used libraries
        for line in lines:
            line = line.strip()
            if line.startswith('#include'):
                library = line[8:].strip()
                library = library[1:-1]
                if library not in libraries:
                    libraries[library] = 1
                else:
                    libraries[library] += 1
        # count the number of lines
        lines_count = len(lines)
        if lines_count not in code_length:
            code_length[lines_count] = 1
        else:
            code_length[lines_count] += 1
        total_lines += lines_count
        # count the number of characters
        chars_count = 0
        for line in lines:
            chars_count += len(line)
        total_chars += chars_count

    print(f"Process the user's codes successfully.")

    return {
        "libraries": libraries,
        "code_length": code_length,
        "total_lines": total_lines,
        "total_chars": total_chars,
    }

