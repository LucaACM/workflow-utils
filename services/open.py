import subprocess
import re
from const import projectsRootPath, projects

class OpenService:
    def __init__(self):
        self.root = projectsRootPath
        self.projects = projects

    def execute(self, args, flags):
        try:
            found = 0
            for arg in args:
                for project in self.projects:
                    if re.search(arg, project):
                        found = 1
                        print(f'open {project}')
                        subprocess.run(f'code {self.root}/{project}', shell=True, check=True)
                        break
                if found == 0:
                    print(f'No project found for {arg}')
                found = 0
        except Exception as e:
            print(f'Error running command, details: {e}')
            
        