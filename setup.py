from setuptools import setup, find_packages

setup(
    name='django-feed-imports',
    author='Yuri Prezument',
    author_email='yuri@modlinltd.com',
    version='0.1.1dev',
    packages=find_packages(),
    description='Import RSS and Atom feeds and save in the database.',
    long_description=open('README.rst').read(),
    install_requires=[
        'Django >= 1.4',
        'feedparser >= 5.1.2',
    ],
)
