"""
This project is used to create a .html file as the user's OJ annual report.

This module is used to generate the .html file.

"""

from bs4 import BeautifulSoup
import json

def generate_html(submit_info: dict, code_info: dict):
    """
    Generate the .html file.

    :param submit_info: The user's submits information.
    :param code_info: The user's code information.
    """
    # create a new .html file
    with open('report.html', 'w') as f:
        # head of the .html file
        head = """
<!DOCTYPE html>
<html>
<head>
    <title>OJ Annual Report</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
<h1>清华大学电子工程系 2024 年秋季学期\n《数据与算法》OJ 实验总结报告</h1>
        """
        f.write(head)

        # user information ------------------------------------------------
        user_info = f"""
<p>同学，你好！你的学号为 {submit_info['user'][3:]}。</p>
        """
        f.write(user_info)

        # submit information ----------------------------------------------
        all_submit_info = f"""
<h2>提交信息</h2>
<p>本学期你共提交了 {len(submit_info['submit_indexs'])} 次代码。</p>
<p>以下是你的提交信息：</p>
<table>
    <tr>
        <th>题目</th>
        <th>提交次数</th>
        <th>使用最多的编译器</th>
        <th>最高分</th>
        <th>期末总分贡献</th>
    </tr>
        """
        f.write(all_submit_info)

        # submit table
        for problem_id, problem_info in submit_info['submit_problems'].items():
            submit_table = f"""
    <tr>
        <td>{problem_id} {problem_info['title']}</td>
        <td>{len(problem_info['submits'])}</td>
        <td>{max(problem_info['languages'], key=problem_info['languages'].get)}</td>
        <td>{problem_info['highest_score']}</td>
        <td>{problem_info['get_score']}</td>
    </tr>
            """
            f.write(submit_table)

        # submit summary
        submit_summary = f"""
</table>
<p>目前，你在《数据与算法》OJ 实验部分中的得分为 {submit_info['total_score']} 分。</p>
        """
        f.write(submit_summary)

        # rest problem
        rest_problem = f"""
<p>新的一年，你还有 {10 - len(submit_info['submit_problems'])} 道题目需要完成。加油！</p>
        """ if len(submit_info['submit_problems']) < 10 else """
<p>恭喜你！你已经完成了本学期的所有题目。</p>
        """
        f.write(rest_problem)

        # compiler information -------------------------------------------
        compiler_info = f"""
<h2>编译器信息</h2>
<p>你使用了以下编译器：</p>
<table>
    <tr>
        <th>编译器</th>
        <th>使用次数</th>
    </tr>
        """
        f.write(compiler_info)

        # compiler table
        for language, number in submit_info['submit_languages'].items():
            compiler_table = f"""
    <tr>
        <td>{language}</td>
        <td>{number}</td>
    </tr>
            """
            f.write(compiler_table)
        
        # compiler errors
        compiler_errors = f"""
</table>
<p>你共遇到了 {len(submit_info['compile_errors'])} 次编译错误。还需更加细心！</p>
        """ if len(submit_info['compile_errors']) > 0 else """
</table>
<p>你没有遇到编译错误！继续努力！</p>
        """
        f.write(compiler_errors)

        # date and time information --------------------------------------
        date_info = f"""
<h2>日期与时间信息</h2>
<p>你提交的代码集中在以下日期：</p>
<table>
    <tr>
        <th>日期</th>
        <th>提交次数</th>
    </tr>
        """
        f.write(date_info)

        # date table
        count = 10
        for date, number in sorted(submit_info['create_dates'].items()):
            date_table = f"""
    <tr>
        <td>{date}</td>
        <td>{number}</td>
    </tr>
            """
            f.write(date_table)
            count -= 1
            if count == 0:
                break
        
        # time table
        time_info = f"""
</table>
<p>你提交的代码集中在以下时间：</p>
<table>
    <tr>
        <th>时间</th>
        <th>提交次数</th>
    </tr>
        """
        f.write(time_info)

        # time table
        count = 10
        for time, number in sorted(submit_info['create_times'].items()):
            time_table = f"""
    <tr>
        <td>{time}</td>
        <td>{number}</td>
    </tr>
            """
            f.write(time_table)
            count -= 1
            if count == 0:
                break

        # code information -----------------------------------------------
        all_code_info = f"""
</table>
<h2>代码信息</h2>
<p>本学期你共写了 {code_info['total_lines']} 行代码，最长的一次提交有 {max(map(int, code_info['code_length'].keys()))} 行！</p>
<p>你使用了以下库：</p>
<table>
    <tr>
        <th>库</th>
        <th>使用次数</th>
    </tr>
        """
        f.write(all_code_info)

        # code table
        for library, number in code_info['libraries'].items():
            code_table = f"""
    <tr>
        <td>{library}</td>
        <td>{number}</td>
    </tr>
            """
            f.write(code_table)

        # code summary
        code_summary = f"""
</table>
<p>你总计向 OJ 提交了 {code_info['total_chars']} 个字符的代码！</p>
        """
        f.write(code_summary)

        # rest of the .html file
        end_body = """
</body>
</html>
        """
        f.write(end_body)

        
#         to_write = """<!DOCTYPE html>
# <html>
# <head>
#     <title>OJ Annual Report</title>
#     <style>
#         table {
#             width: 100%;
#             border-collapse: collapse;
#         }
#         th, td {
#             border: 1px solid black;
#             padding: 8px;
#             text-align: center;
#         }
#         th {
#             background-color: #f2f2f2;
#         }
#     </style>
# </head>
# <body>
# <h1>OJ Annual Report</h1>
# <h2>Submit Information</h2>
# <p>Total submits: """ + str(len(submit_info['submit_indexs'])) + """</p>
# <table>
#     <tr>
#         <th>Problem</th>
#         <th>Submits</th>
#         <th>Languages</th>
#         <th>Scores</th>
#         <th>Highest Score</th>
#         <th>Dates</th>
#         <th>Times</th>
#         <th>Errors</th>
#     </tr>"""
#         # write the submit information
#         for problem_id, problem_info in submit_info['submit_problems'].items():
#             to_write += f"""
#     <tr>
#         <td>{problem_info['title']}</td>
#         <td>{len(problem_info['submits'])}</td>
#         <td>{', '.join([f"{language}({count})" for language, count in problem_info['languages'].items()])}</td>
#         <td>{', '.join([str(score) for score in problem_info['scores']])}</td>
#         <td>{problem_info['highest_score']}</td>
#         <td>{', '.join([f"{date}({count})" for date, count in problem_info['dates'].items()])}</td>
#         <td>{', '.join([f"{time}({count})" for time, count in problem_info['times'].items()])}</td>
#         <td>{problem_info['errors']}</td>
#     </tr>"""
#         to_write += """
# </table>
# <h2>Code Information</h2>
# <p>Total lines: """ + str(code_info['total_lines']) + """</p>
# <table>
#     <tr>
#         <th>Library</th>
#         <th>Number</th>
#     </tr>"""
#         # write the code information
#         for library, number in code_info['libraries'].items():
#             to_write += f"""
#     <tr>
#         <td>{library}</td>
#         <td>{number}</td>
#     </tr>"""
#         to_write += """
# </table>
# </body>
# </html>"""
#         f.write(to_write)
    print("Generate the .html file successfully.")
