# nsml: lym7505/nsml_jvm:latest

from distutils.core import setup

setup(
    name='kaist-korquad-test',
    version='1.0',
    install_requires=[
        'boto3', 'regex', 'sacremoses', 'filelock', 'tokenizers',
        'tqdm', 'konlpy', 'sentencepiece', 'dataclasses', 'konlpy'
    ]
)
