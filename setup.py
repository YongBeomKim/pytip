# find_packages
# https://setuptools.pypa.io/en/latest/setuptools.html#using-find-packages
# https://stackoverflow.com/questions/43253701/python-packaging-subdirectories-not-installed
from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name    = 'pytip',
    version = '0.0.12',
    license = 'MIT',
    description = "Personally tiny useful Python tips",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/YongBeomKim/pytip',
    author = 'momukji lab',
    author_email = 'ybkim@momukji.com',
    keywords = ['pytip'],
    python_requires = '>=3',
    include_package_data = True,
    # https://setuptools.pypa.io/en/latest/userguide/package_discovery.html
    package_data = {'': ['json/*.json']}, # 파일추가
    # package_dir = {'': ['json/*.json']},
    packages = find_packages(
        exclude = ['jupyter', 'backup', '.vscode', '.ipynb_checkpoints']
    ),
    install_requires=[
        # 'xlrd',
        # 'openpyxl',
        'termcolor',
        'requests',
        'pandas',
        # 'numpy',
        'tqdm',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
