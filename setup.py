from setuptools import setup, find_packages

setup(
    name="auth-passwordless-kavenegar",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.0',
        'drfpasswordless>=1.5.9',
        'djangorestframework-simplejwt>=5.0.0',
        'kavenegar>=1.1.2',
    ],
    author="Mohammad Ali RAHIMI (MARKRAHIMI)",
    author_email="imarkrahimi@gmail.com",
    description="A Django app for passwordless authentication using Kavenegar SMS",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/markrahimi/auth-passwordless-kavenegar",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
