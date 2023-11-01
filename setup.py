import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'
REPO_NAME = 'mlops'
AUTHOR_USER_NAME = 'ahmadshah2103'
AUTHOR_EMAIL = 'ahmad1911491@gmail.com'
SRC_REPO = 'mlops'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for ML projects',
    long_description=long_description,
    long_description_content='text/markdown',
    url=f'https: //github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        'Bug Tracker': f'https: //github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src')
)
