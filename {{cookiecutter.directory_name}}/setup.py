from setuptools import setup, find_packages

setup(
    name = {{cookiecutter.directory_name}},
    author = 'dsul',
    author_email = 'dsul@users.noreply.github.com',
    setup_requires = ['pytest-runner'],
    tests_require = [
        'pytest',
        'pytest-datadir',
        'pytest-watch',
        'pytest-env',
        'pytest-describe',
        'pytest-mock'
    ],
    packages = find_packages(),
    zip_safe = False
)
