# -*- coding:utf-8 -*-

if __name__ == "__main__":
    import subprocess
    con_info = subprocess.Popen('pytest ./testcase/ --alluredir result/', shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE)
    print(con_info.stdout.readlines())