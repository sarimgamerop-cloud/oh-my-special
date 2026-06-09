import os 
from pathlib import Path
import colorama
from colorama import Fore, Back, Style
colorama.init()


class Commands:
    '''Hub for all main commands:'''
    def __init__(self):
        # doc: Disable the commands:
        self.commmands_enabled = True
        self.interpret = None
        self.shell_name = None
        self.default_path = 'C:/Users'
        self.valid_command_cd = None
        self.error = None
        self.cur_dir = f'({self.default_path}) '
        self.known_commands = ['cd','pwd','ls','exit']

    def greeter(self):
        main_line = 'Oh-My-Special ~ Shell: '
        self.interpret = main_line.split(' ~ Shell: ')
        self.shell_name = main_line.split('Oh-My-Special')
        
        ## DEBUG LINE : 
        # print(f'interpret: {self.interpret} shell_name: {self.shell_name}')
   
    def prompt(self,dir=""):
        print(Fore.YELLOW + dir +
Fore.RED + self.interpret[0]
+ Fore.YELLOW + self.shell_name[1]
+ Fore.WHITE +  "> ",end="")

    def cd(self,cd_command):
        if not cd_command.split():
            return 'The command must be valid.'
            valid_command_cd = False

        if cd_command.startswith('cd'):
            valid_command_cd = True
            directory_user = cd_command.split('cd ')
        else:
            valid_command_cd = False

        try:
            os.chdir(directory_user[1])
        except FileNotFoundError:
            self.error = 'FileError'
            return f'{self.error}: Provided path was not found.'
        
        self.cur_dir = f"({directory_user[1]}) "
        # self.prompt(dir=self.cur_dir)
        return ''

        # doc: DEBUG:
        ### return f'Success. Path: [{os.getcwd()}]'

    
    def exit(self):
        quit()

    def pwd(self):
        print(Fore.WHITE + 'Current Directory: \n' + Fore.GREEN +'→ '+ self.cur_dir)
    

    def ls(self):
        stripped_directory = self.cur_dir.strip('() ')
        files_in_path = os.listdir(stripped_directory)
        print( Fore.RED + '→ ' + '[ Files: ]'+ Fore.RESET)
        for files in files_in_path:
            if '.' in files:
                name, ext = files.rsplit('.', 1)
                print(f"⋅ {Fore.GREEN}{name}{Fore.WHITE} | {Fore.YELLOW}  {ext}{Fore.RESET}")
            else:
                print(f"⋅ {Fore.GREEN}{files}{Fore.RESET} | {Fore.YELLOW}  folder{Fore.RESET}")



    def checks(self,full_command):

        for cmds in self.known_commands:
            if full_command.startswith(cmds):
                break
        else:
            self.error = '[UnknownCommand]: '
            print(self.error + 'Command not found.')

        if full_command.startswith('cd'):
            print(self.cd(full_command))

        if full_command.startswith('pwd'):
            self.pwd()

        if full_command.startswith('ls'):
            self.ls()

        if full_command.startswith('exit'):
            self.exit()

        # print(os.getcwd())


# example object to remove : 'shell_instance not defined.' and  initilize.
# removing it will break the logic.
ex_obj = Commands()
ex_obj.greeter()