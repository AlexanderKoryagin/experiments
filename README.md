### Experiments with Python

***

Preparations for Ubuntu:
```bash
sudo apt-get update
sudo apt-get install python-pip python-dev build-essential
sudo pip install -U pip setuptools virtualenv
virtualenv --clear .venv && source .venv/bin/activate
pip install -U -r requirements.txt
```
Preparations for Windows:
```
1. Download latest Python 2.x from www.python.org.
2. During installation enable action 'Add python.exe to Path'.
3. In CMD:
> python -m pip install -U pip setuptools virtualenv
> virtualenv --clear .venv
> .venv\Scripts\activate
> pip install -U -r requirements.txt
```
To run *only* Code Style checks:
```bash
flake8 experiments/
pylint experiments/
```
