# 清华大学电子工程系 2024 年秋季学期《数据与算法》OJ 实验总结报告生成器
# Report Generator for OJ Experiments of _Data and Algorithm_ in Fall 2024, Department of Electronic Engineering, Tsinghua University

本程序用于生成清华大学电子工程系 2024 年秋季学期《数据与算法》OJ 实验总结报告。

This program is used to generate the report of OJ experiments of _Data and Algorithm_ in Fall 2024, Department of Electronic Engineering, Tsinghua University.

程序与**清华大学 2024 年年度人物张宇东**无关，与《数据与算法》课程教师及课程助教无关。

The program has nothing to do with **Zhang Yudong**, one of the ten **Tsinghua University 2024 Annual Figures**. It also has nothing to do with the teachers and teaching assistants of the _Data and Algorithm_ course.

## 模块 Modules

+ `main.py`: 主程序 Main program
+ `oj_website.py`: 使用 `serviceid` 和 `Auth-Token` 获取 OJ 数据 Using `serviceid` and `Auth-Token` to get OJ data
+ `submit_processor.py`: 处理、分析 OJ 提交数据 Processing and analyzing OJ submission data
+ `html_generator.py`: 生成实验总结报告 Generating the report of OJ experiments

## 使用 Usage

1. 克隆本仓库，或下载 ZIP 压缩包并解压

    Clone this repository, or download the ZIP file and unzip it

2. 安装依赖库

    Install the required libraries

    ```bash
    pip install -r requirements.txt
    ```

3. 运行 `main.py`

    Run `main.py`

    ```bash
    python main.py
    ```

    初次运行，程序会要求输入 `serviceid` 和 `Auth-Token`，请在浏览器中登录 OJ 并查看 Cookie，找到 `serviceid` 和 `Auth-Token`，并输入到程序中。

    When running for the first time, the program will ask for `serviceid` and `Auth-Token`. Please log in to OJ in the browser and view the Cookie, find `serviceid` and `Auth-Token`, and enter them into the program.

    输入后程序会生成 `config.json` 文件，下次运行时会自动读取。

    After entering, the program will generate the `config.json` file, which will be read automatically next time it is run.

4. 程序运行结束后，会在当前目录生成 `report.html` 文件，使用浏览器打开即可查看实验总结报告。

    After the program finishes running, a `report.html` file will be generated in the current directory. Open it with a browser to view the report.

## 反馈 Feedback

如有问题或建议，请在 **Issues** 中提出。

If you have any questions or suggestions, please raise them in **Issues**.