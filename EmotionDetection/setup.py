from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='1.0',
    packages=find_packages(),
    author='RW',
    author_email='fake@email.com',
    description='Watson sentiment analyzer',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    install_requires=["requests"],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)