[![PyPi](https://img.shields.io/pypi/v/true50.svg?style=flat)](https://pypi.python.org/pypi/true50)
[![Python versions](https://img.shields.io/pypi/pyversions/true50.svg?style=flat)](https://www.python.org/)

# True50

True50 is a Python script to open [true5050.com] links. It supports both Python 2 and 3.

### Installation

The code is available on [PyPi], you should be able to install using

```sh
$ pip install true50
```
or
```sh
$ easy_install true50
```

### Usage

Straightforward :
```sh
true50 <true5050.com url>
```

### Tech

True50 uses a number of open source Python libraries:

* [Requests] : Make easy HTTP requests
* [BeautifulSoup] : Web scrapping python library

More informations on the versions used are available in [requirements.txt](./requirements.txt).

### Help

This is a small project, but help is more than welcome!

Don't hesitate to open an issue or pull request, I'll get to it ASAP.


[true5050.com]:http://true5050.com
[PyPi]:https://pypi.python.org/pypi
[Requests]:http://docs.python-requests.org/en/latest/
[BeautifulSoup]:http://www.crummy.com/software/BeautifulSoup/
