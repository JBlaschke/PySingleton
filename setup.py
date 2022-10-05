import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="PySingleton",
    version="1.0.0",
    author="Johannes Blaschke",
    author_email="jpblaschke@lbl.gov",
    description="Singleton classes for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JBlaschke/PySingleton",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],
    extra_requires={}
)
