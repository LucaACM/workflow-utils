from const import toolDockerComposeRoot, composeFiles, makeCommands, toolDockerPath, watchCommand, startCommand, projects
from ruamel.yaml import YAML
import os
import re
import subprocess

class WorkWith:
    def __init__(self):
        self.root = toolDockerComposeRoot
        self.services = projects
        self.files = composeFiles
        self.makeCommands = makeCommands
    
    def execute(self, args, flags):
        try:
            yaml = YAML()
            yaml.preserve_quotes = True

            for filename in self.files:
                file_path = os.path.join(self.root, filename)
                
                with open(file_path, 'r') as file:
                    compose_file = yaml.load(file)
                    
                for service_name, service_config in compose_file['services'].items():
                    found = False
                    
                    for arg in args:
                        if re.search(arg, service_name) and service_name in self.services:
                            found = True
                            break
                        
                    if found:
                        service_config['command'] = watchCommand
                    elif service_name in self.services:
                        service_config['command'] = startCommand

                with open(file_path, 'w') as file:
                    yaml.dump(compose_file, file)

                print("Docker Compose files have been updated.")
                
                os.chdir(toolDockerPath)
                subprocess.run(makeCommands[filename], shell=True)
            
        except Exception as e:
            print(f'Error running command, details: {e}')