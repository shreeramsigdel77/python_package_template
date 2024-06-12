from setuptools import setup, find_packages

setup(
    name="python_package_template",
    version="0.0.1",
    author="Shree Ram Sigdel",
    author_email="shreeramsigdel77@gmail.com",
    description="A sample example package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sampleproject",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.0",
        "setuptools>=42",
    ],
    project_urls={
        "Homepage": "https://github.com/sampleproject",
        "Issues": "https://github.com/sampleproject/issues",
    },
)
