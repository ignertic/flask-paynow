from setuptools import setup

with open("README.md", 'r') as fh:
    README=fhread()

__version__ = "0.0.1" #change versioning
setup(
    name='Flask-paynow',
    version='0.0.1',
    url='http://admiremakusha.co.zw/flask-paynow/',
    license='BSD',
    author='Admire Makusha',
    author_email='hello@admiremakusha.co.zw',
    description='Paynow Flask Plugin',
    long_description_content_type="text/plain",
    long_description=README, #Update long description
    # if you would be using a package instead use packages instead
    # of py_modules:
    packages=['flaskpaynow'], #setuptools.find_packages() 
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask', 'paynow'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={"console_scripts" : ["flaskpaynow=flaskpaynow.__main__:main"]},
)