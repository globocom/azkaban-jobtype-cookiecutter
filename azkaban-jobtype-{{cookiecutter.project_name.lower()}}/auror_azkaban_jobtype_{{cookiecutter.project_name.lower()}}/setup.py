# encoding: utf-8

from setuptools import setup, find_packages

with open("version.txt") as version_file:
    version = version_file.read().strip()

setup(
    name="auror_azkaban_jobtype_{{cookiecutter.project_name.lower()}}",
    version=version,
    description="{{cookiecutter.project_name}} jobtype for Azkaban Auror",
    author="Big Data",
    author_email="bigdata@corp.globo.com",
    license='MIT',
    install_requires=[
        "auror-core>=1.0.0,<2.0.0"
    ],
    packages=find_packages(),
)
