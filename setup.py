import os
from setuptools import setup

#with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
#    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-inline-admin-extensions',
    version='0.1.1',
    packages=['inline_admin_extensions', 'inline_admin_extensions.templatetags'],
    include_package_data=True,
    license='BSD License',
    description='Django inline admin extras - pagination sortin.',
    #long_description=README,
    keywords = ['django', 'admin'],
    #url='http://django-admin-view-permission.readthedocs.org/',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'Django>=3.0.1'
    ],
)
