from setuptools import setup

current_version = '0.2'

setup(
    name = 'true50',
    version = current_version,
    description = 'Script to open true5050 links',
    long_description = open('README.md').read(),
    author = 'Jimmy Mayoukou',
    author_email = 'Bhullnatik@gmail.com',
    license = 'MIT',
    url = 'https://github.com/Bhullnatik/true50',
    download_url = 'https://github.com/Bhullnatik/true50/tarball/' + current_version,
    install_requires = [
        'beautifulsoup4',
        'requests',
    ],
    packages = ['true50'],
    entry_points = {
        'console_scripts' : ['true50 = true50.main:main']
    },
    keywords = ['true5050', 'true50', 'script', 'utility', 'FiftyFifty', 'reddit'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        ],
)
