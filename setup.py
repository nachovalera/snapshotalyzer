from setuptools import setup

setup(
    name='snapshotalyzer',
    version='0.1',
    author="Nacho Valera",
    author_email="nacho.valera@icloud.com",
    description="SnapshotAlyther is a tool to manage spanshots",
    packages=['shotty'],
    url="https://github.com/nachovalera/snapshotalyzer",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_proints='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)