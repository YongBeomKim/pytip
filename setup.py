# find_packages
# https://setuptools.pypa.io/en/latest/setuptools.html#using-find-packages
# https://stackoverflow.com/questions/43253701/python-packaging-subdirectories-not-installed
from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name = 'pytip',
    version = '0.0.8',
    license = 'MIT',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'momukji lab',
    author_email = 'ybkim@momukji.com',
    url = 'https://github.com/YongBeomKim/pytip',
    packages = find_packages(),
    python_requires = '>=3',
    keywords = ['pytip'],
    install_requires=[
        'matplotlib',
        'termcolor',
        'requests',
        'pandas',
        'numpy',
        'tqdm',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
