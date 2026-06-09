import os 
from pathlib import Path
import colorama
from colorama import Fore, Back, Style
colorama.init()
from commands import Commands



shell_instance = Commands()
# initializer to set up the new split attributes: 
greeter_init = shell_instance.greeter()
# print(shell_instance.cd('cd C:/User'))

os.chdir(shell_instance.default_path)
while True:
    shell_instance.prompt(dir=shell_instance.cur_dir)
    command_prompt = input()

    shell_instance.checks(command_prompt)




