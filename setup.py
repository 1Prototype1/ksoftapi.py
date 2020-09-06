from setuptools import setup

def get_requirements():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    return requirements

version = '0.2.5'

if not version:
    raise RuntimeError('Version is not set')

with open('README.md') as f:
    readme = f.read()

setup(
    name='ksoftapi',
    packages=['ksoftapi', 'ksoftapi.apis'],
    version=version,
    description='The unofficial modded KSoft.SI API Wrapper',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='1Prototype1',
    author_email='astonlopes1999@gmail.com',
    url='https://github.com/1Prototype1/ksoftapi.py',
    keywords=['ksoftapi'],
    install_requires=get_requirements(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
