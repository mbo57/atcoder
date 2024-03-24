#!/bin/python3
import subprocess
import sys

args = sys.argv
if len(args) == 1:
    file1 = "ans.py"
    file2 = "main.py"
elif len(args) == 2:
    file1 = args[2]
    file2 = "main.py"
else:
    file1 = args[2]
    file2 = args[3]

for i in range(100):
    cmd = ["python3", "generate.py"]
    output_str = subprocess.run(cmd, capture_output=True, text=True).stdout

    cmd = ["python3", file1]
    output1 = subprocess.run(cmd, input=output_str, capture_output=True, text=True).stdout

    cmd = ["python3", file2]
    output2 = subprocess.run(cmd, input=output_str, capture_output=True, text=True).stdout

    if output2 != output1:
        print(output_str)
        print("=======")
        print(output1)
        print("=======")
        print(output2)
        exit(0)
    else:
        print("same answer")

