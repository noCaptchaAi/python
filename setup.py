from setuptools import setup, find_packages

setup(
    name='nocaptchaai',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'Pillow'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A library for solving captchas using nocaptchaai',
    long_description=open('README.md').read(),
    url='https://github.com/yourusername/nocaptchaai',
)
