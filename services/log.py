import subprocess
import os
import re
from const import logsAvailable

class LogService:
    def __init__(self):
        self.logsAvailable = logsAvailable
        self.update_active_containers()

    def execute(self, args, flags):
        for arg in args:
            for key, value in self.logsAvailable.items():
                if re.search(arg, key):
                    print(f'running {value}')
                    self.run_command_in_iterm(value)
                    continue
                print(f'unable to run command for {arg}')

    def get_active_containers(self):
        result = subprocess.run(["docker", "ps", "--format", "{{.Names}}"], capture_output=True, text=True)
        if result.returncode != 0:
            print("Can't retrieve active containers")
            return []

        active_containers = result.stdout.strip().split('\n')
        return active_containers
    
    def run_command_in_iterm(self, command):
        iterm_script = f"""
        tell application "iTerm"
            activate
            try
                set currentWindow to current window
            on error
                set currentWindow to (create window with default profile)
            end try
            tell currentWindow
                create tab with default profile
                tell the current session
                    write text "{command}"
                end tell
            end tell
        end tell
        """
        subprocess.run(["osascript", "-e", iterm_script], check=True)
    
    def update_active_containers(self):
        active_containers = self.get_active_containers()
        self.logsAvailable = {k: v for k, v in self.logsAvailable.items() if k in active_containers}