<p>
    <img src="https://img.shields.io/badge/coverage-100%25-brightgreen.svg"/>
    <img src="https://img.shields.io/badge/python-%3E%3D3.7.1-blue.svg"/>
</p>

# Python Practice

This side project was made to begin focusing on common functions in python while also experimenting with best practices for unit testing and code / test coverage. Also focusing more on moving away from python 2.7 and learning python3 features.

## Getting Started

To get started, grab the https link above and clone this repo to your local machine
```
git clone https://github.com/thebenhurley/python-practice.git
```

Then run the test suite from inside the python-practice directory (-v verbose flag is optional)
```
python3 -m unittest discover -v
```

To see code coverage, run with compare (again, -v verbose flag and -m missing flags are optional)
```
coverage run -m unittest discover -v
coverage report -m
```

## Prerequisites

In order to clone and run the project, you will need the following:
1. Python 3 (Install with [homebrew](https://docs.brew.sh/Homebrew-and-Python), or download directly from their [website](https://www.python.org/downloads/))
2. [Coverage](https://coverage.readthedocs.io/en/latest/install.html) (optional for code coverage).

## Functions
* [FizzBuzz](func/fizzbuzz.py)
* [FizzBuzzJazz](func/fizzbuzz.py)

## Testing

Testing is currently being completed with [unittest](https://docs.python.org/3/library/unittest.html). 

## Acknowledgments

Corey Schafer - [Python Tutorial: Unit Testing Your Code with the unittest Module](https://www.youtube.com/watch?v=6tNS--WetLI&t=417s)

Shane Exterkamp - [Python Data Structures](https://github.com/exterkamp/Python-Data-Structures/blob/master/README.md)
