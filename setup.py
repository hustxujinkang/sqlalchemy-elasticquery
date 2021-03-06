import os
from setuptools import setup


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='sqlalchemy-elasticquery',
    version='0.0.3',
    description='Use ElasticSearch query search in SQLAlchemy.',
    url='https://github.com/loverajoel/sqlalchemy-elasticquery',
    license='MIT',
    author='Joel Lovera',
    author_email='joelalover@gmail.com',
    packages=['sqlalchemy_elasticquery'],
    include_package_data=True,
    install_requires=[
        'Flask>=0.10',
        'SQLAlchemy>=0.7.8',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database'
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
