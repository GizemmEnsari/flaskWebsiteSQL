from setuptools import setup
"""
This code below uses setup from setuptools module to install all of my mainCode requirements into a
virtual environment. It creates an entry point so that after installation, the server can be started
with the command "start-server" while in the virtual environment.
"""


# Run "pip install -e ." in an activated virtual environment to run setup.py
# and install the mainCode package

setup(
    name="mainCode",
    version="1.0.0",
    author="Gizem Ensari",
    description="mainCode for my python interpreter on a website project",
    url="https://github.com/GizemmEnsari/flaskWebsiteSQL",

    install_requires=[
        "Flask",
        "flask_sqlalchemy"

    ],
    package_data={
        "":["*.txt","*.pdf","*.py"],
        "mainCode":["docs/*","tests/*","static/*"],

    },

    # Creates a command that can be executed from inside the virtual environment
    # to launch the server
    py_modules=["flaskWebsiteSQL.serverStorage"],
    entry_points={
        "console_scripts":[
            "start-server=flaskWebsiteSQL.mainCode.mainCode:main"
        ]
    }
)



