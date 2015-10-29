from setuptools import setup, find_packages

setup(
    name='django-feed-imports',
    author='Yuri Prezument',
    author_email='yuri@modlinltd.com',
    maintainer='Pavel Savchenko',
    maintainer_email='pavel@modlinltd.com',
    version='0.1.7',
    packages=find_packages(),
    description='Import RSS and Atom feeds and save in the database.',
    long_description=open('README.rst').read(),
    url='https://github.com/modlinltd/django_feed_imports',
    download_url='https://github.com/modlinltd/django_feed_imports/tarball/0.1.7',
    keywords='rss,atom,import,feed',
    install_requires=[
        'Django >= 1.4',
        'feedparser >= 5.1.2',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
)
