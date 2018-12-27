# nfiniity-utils
[![PyPI version](https://badge.fury.io/py/nfiniity-utils.svg)](https://badge.fury.io/py/nfiniity-utils)

Diverse python utilities by http://www.nfiniity.com

## Installation
### There are two ways to install nfiniity-utils:

Install nfiniity-utils from PyPI (recommended):
```
sudo pip install nfiniity-utils
```
If you are using a virtualenv, you may want to avoid using sudo:
```
pip install nfiniity-utils
```
### Alternatively: install nfiniity-utils from the GitHub source:
First, clone nfiniity-utils using `git`:
```
git clone https://github.com/apgeorg/nfiniity_utils.git
```
Then, cd to the nfiniity_utils folder and run the install command:
```
cd nfiniity_utils
sudo python setup.py install
```
## Getting started
### Timer
```python
import nfiniity_utils as n8

# Timer callback function
def timer_timeout():
  print("Hello!")

# Create a Timer which runs periodically 
t = n8.Timer(1, timer_timeout, oneshot=False)

# Start running
t.start()
```

You can now stop the timer:

```python
t.stop()
```






