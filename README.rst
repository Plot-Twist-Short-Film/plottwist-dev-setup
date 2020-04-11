plottwist-dev-setup
============================================================

Repository that contains base scripts to setup development environment for Plot Twist project.

It contains code to automatize the clone of all the Plot Twist and ArtellaPipe repos available.

Requirements
################

* Windows 10
* `Python 2.7.16 <https://www.python.org/ftp/python/2.7.16/python-2.7.16.amd64.msi>`_: We are using this version of Python as our core version. Install it in your machine and make sure that you add it in your Windows system path.

* `virtualenv <https://virtualenv.pypa.io/en/latest//>`_: We will need it to create a virtualenv with proper requirements to launch our code.

Instructions
################

1. **Clone/Download** this repo in any folder in machine
2. Launch **clone_plottwist_repos.bat**. This batch file will create a new environment variable, will install all dependencies and will download all the Plot Twist available GitHub repositories inside this folder.
3. **Optional**. If you are going to work with ArtellaPipe related code you can download all ArtellaPipe repositories launching **clonde_artellapipe_repos.bat**.

