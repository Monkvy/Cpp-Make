import os
import json

def write_default_config():
    default_config = '''
    {
        "project-name": "main",
        "flags": [
            "-Wall"
        ],
        "source-directory": "src",
        "build-directory": "bin",
        "lib-directory": "libs",
        "libs": [
            "SDL2"
        ],
        "linker-flags": [
            "-lSDL2main",
            "-lSDL2"
        ]
    }
    '''

    with open('Make.json', 'w') as f:
        f.write(default_config)

# Create config file is not exist
if not os.path.isfile('Make.json'):
    write_default_config()

# Create config file new if config is empty
with open('Make.json', 'r') as f:
    if f.read() == '':
        write_default_config()

# Load config
with open('Make.json', 'r') as f:
    config = json.loads(f.read())

# Get all src files
src_files = []
for path, subdirs, files in os.walk(config['source-directory']):
    for name in files:
        if name.endswith('.cpp'):
            src_files.append(os.path.join(path, name))


# Build .exe file
src_str = ' '.join([src_file for src_file in src_files])
flags_str = ' '.join([flag for flag in config['flags']])
libs_str = ' '.join([f'-L{config["lib-directory"]}\\{lib}\\lib' for lib in config['libs']])
linker_str = ' '.join([linker for linker in config['linker-flags']])

cmd = f'g++ {flags_str} {src_str} -I{config["lib-directory"]}\\*\\include {libs_str} -obin\\{config["project-name"]} -lmingw32 {linker_str}'
os.system(cmd)
print(cmd)