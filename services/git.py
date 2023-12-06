import webbrowser
import re
import os
from const import repoDicts
from dotenv import load_dotenv

class GitService:
    def __init__(self):
        load_dotenv()
        self.repoDicts = repoDicts

    def execute(self, args, flags):
        for arg in args:
            for key, value in self.repoDicts.items():
                suffix = ''
                if re.search(arg, key):
                    if 'pr' in flags:
                        suffix = '/pulls/@me'
                    webbrowser.open(value + suffix)
        

        
