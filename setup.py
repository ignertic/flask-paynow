from setuptools import setup


setup(
    name='Flask-paynow',
    version='0.1',
    url='http://admiremakusha.co.zw/flask-paynow/',
    license='BSD',
    author='Admire Makusha',
    author_email='hello@admiremakusha.co.zw',
    description='Very short description',
    long_description=__doc__,
    py_modules=[''],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
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
    ]
)