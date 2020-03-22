from setuptools import setup

def readme():
    with open('README.rst') as f:
        README = f.read()
    return README


setup(
    name="neattext",
    version="0.0.2",
    description="Neattext - a simple NLP package for cleaning text",
    long_description=readme(),
    long_description_content_type="text/x-rst",
    url="https://github.com/Jcharis/neattext",
    author="Jesse E.Agbe(JCharis)",
    author_email="jcharistech@gmail.com",
    license="MIT",
    keywords='neattext cleantext NLP tidytext textpreprocessing text cleaning jcharistech textify ',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    packages=["neattext"],
    include_package_data=True,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4'
    # install_requires=["collections"]
    
)