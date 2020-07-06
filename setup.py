from setuptools import find_packages, setup
import os

# Get more https://pypi.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    # Indicate to who your project is directed
    "Environment :: Web Environment",
    "Framework :: Django",
    "Intended Audience :: Developers",
    # Indicate the used license (must match the "license")
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: OS Independent",
    # Indicate supported versions, Python 2, Python 3 or both.
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    "Topic :: Internet :: WWW/HTTP :: WSGI",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

EXCLUDE_FROM_PACKAGES = ["project","project.*"]

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

setup(
    name="dockermanager",
    version="0.1",
    description="Docker Manager app",
    long_description=read('README.rst'),
    classifiers=CLASSIFIERS,
    keywords="docker django",
    author="<>",
    author_email="test@gmail.net",
    maintainer="test",
    maintainer_email="test@gmail.com",
    url="https://github.com/a1/dockermanager",
    license="GPL",
    platforms="OS Independent",
    install_requires=["Django==2.2.3"],
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    zip_safe=False,
    project_urls={
        'Source': 'https://github.com/a1/dockermanager',
    },
)
