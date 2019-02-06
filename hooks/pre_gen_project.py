import conda.cli
import subprocess

# Install opencv3 & numpy
conda.cli.main('conda', 'install', '-y', 'opencv')

# Install pytest-watch
subprocess.run(["pip", "install", "pytest-watch"])

