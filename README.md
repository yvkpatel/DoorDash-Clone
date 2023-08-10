# NTTF
No Time To Fry

## Python Development Environment Setup

Create a python virtual environment using your preferred method, standard python module venv is demonstrated below. Note that your
python alias may be different. 

```
# Create python virtual environment called .venv
python -m venv .venv

# Activate the environment (linux / git bash) 
source .venv/Scripts/activate 

# Activate the environment (windows)
.\.venv\Scripts\Activate
```

Pip install the required third party packages and the NTTF package which will have
each module as a subpackage. This will greatly simplify imports. Be sure to use -e 
to use development mode so changes to files are immediately reflected in your install
of the package.

```
# Third-party dependencies
pip install -r requirements.txt

# Local package
pip install -e .
```
