from setuptools import setup

setup(
    name = 'hashicon',
    packages = ['hashicon'],
    version = '0.1.1',
    description = 'Create minimalistic icons from a string',
    author = 'Alex Cabrera',
    author_email = 'alex.cabrera@gmail.com',
    url = 'https://github.com/cabreraalex/hashicon',
    download_url = 'https://github.com/cabreraalex/hashicon/tarball/0.1',
    license='MIT',
    install_requires=['Pillow']
    keywords = ['icon', 'PIL', 'hash', 'picture', 'Pillow'],
    classifiers = [],
    entry_points = {'console_scripts': [
        'hashicon = hashicon.hashicon:main',
        ]
    }
)


