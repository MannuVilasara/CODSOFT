# NOTE: Making it a python package for cli purpose

from setuptools import setup, find_packages

setup(
    name="passgen",
    author="MannuVilasra",
    author_email="mannuvilasara@gmail.com",
    description="A simple cli-based password generator",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["colorama", "pyperclip"],
    entry_points="""
        [console_scripts]
        passgen=passgen.main:main
    """,
)
