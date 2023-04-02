# find_packages
# https://setuptools.pypa.io/en/latest/setuptools.html#using-find-packages
# https://stackoverflow.com/questions/43253701/python-packaging-subdirectories-not-installed
from setuptools import setup, find_packages
with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

setup(
    name='pytip',
    version='0.0.4',
    description='useful tool and tips of python',
    author='momukji lab',
    author_email='saltman21@naver.com',
    url='https://github.com/YongBeomKim/pytip',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'termcolor',
        'requests',
        'pandas',
        'numpy',
        'tqdm',
    ],
)
