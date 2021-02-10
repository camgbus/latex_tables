from setuptools import setup, find_packages

setup(
    name='latex_tables',
    version='0.1',
    description='Get tables in latex formats.',
    url='https://github.com/camgbus/latex_tables',
    keywords='python setuptools',
    packages=find_packages(include=['tab', 'tab.*']),
)