### Experiments with Python

***

Preparations for Ubuntu:
```bash
sudo apt-get update
sudo apt-get install python-pip python-dev build-essential
sudo pip install -U pip setuptools virtualenv
virtualenv --clear .venv && source .venv/bin/activate
pip install -U -r requirements.txt
py.test -vv
```
To run *only* Code Style checks:
```bash
flake8 experiments/
pylint experiments/
```
