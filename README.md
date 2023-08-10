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
DEMONSTRATION

<img width="1512" alt="Screen Shot 2023-08-09 at 9 28 05 PM" src="https://github.com/yvkpatel/DoorDash-Clone/assets/47285332/7f8b1e02-1710-4e74-bf50-c762aea2bc75">

<img width="1512" alt="Screen Shot 2023-08-09 at 9 26 51 PM" src="https://github.com/yvkpatel/DoorDash-Clone/assets/47285332/f73e3374-11c7-4d07-bf17-c92e6cdca79c">

<img width="1512" alt="Screen Shot 2023-08-09 at 9 28 36 PM" src="https://github.com/yvkpatel/DoorDash-Clone/assets/47285332/6866599e-02d9-4f60-b089-027ba412f321">
