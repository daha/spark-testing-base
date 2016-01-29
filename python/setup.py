from setuptools import setup

setup(
    name='sparktestingbase',
    version='0.0.7',
    author='Holden Karau',
    author_email='holden@pigscanfly.ca',
    packages=['sparktestingbase', 'sparktestingbase.test'],
    url='https://github.com/daha/spark-testing-base',
    license='LICENSE.txt',
    description='Spark testing for python',
    long_description='',
    install_requires=[
        'findspark',
        'pytest',
        'hypothesis'
    ],
    tests_require=[
        'nose',
        'coverage',
        'unittest'
    ],
)
