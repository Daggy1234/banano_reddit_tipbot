import subprocess
from time import sleep
from shared import PYTHON_COMMAND

filename = "tipbot.py"
while True:
    p = subprocess.Popen(PYTHON_COMMAND + " " + filename, shell=True).wait()
    if p == 0:
        break
    sleep(5)
    continue
