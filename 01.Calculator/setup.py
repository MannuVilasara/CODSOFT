# NOTE: Making it a python package for cli purpose

from setuptools import setup, find_packages

setup(
    name="calc",
    author="MannuVilasra",
    author_email="mannuvilasara@gmail.com",
    description="A simple cli-based calculator",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["colorama", "inquirer", "pyfiglet", "typer", "yaspin"],
    entry_points="""
        [console_scripts]
        calc=calc.calc:app
    """,
)
