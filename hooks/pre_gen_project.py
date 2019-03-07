import subprocess

'''
Assumes that python and pip is installed and that
pyenv has been installed with the installer:
https://github.com/pyenv/pyenv-installer
'''

directory_name = '{{ cookiecutter.directory_name }}'
virtual_env_name = directory_name + '-env-3.6.8'

# Environment setup
subprocess.run(["pyenv", "install", "3.6.8"])
subprocess.run(["pyenv", "virtualenv", "3.6.8", virtual_env_name])
subprocess.run(["pyenv", "activate", virtual_env_name])
subprocess.run(["pyenv", "local", virtual_env_name], cwd='./' + directory_name)

# Install dependencies
subprocess.run(["pip", "install", "pytest-watch"])
subprocess.run(["pip", "install", "opencv-python"])
subprocess.run(["pip", "install", "numpy"])
subprocess.run(["pip", "freeze", ">", "requirements.txt"], cwd='./' + directory_name)
