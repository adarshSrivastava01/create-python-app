import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='adarsh',
    version='0.1',
    scripts=['adarsh'],
    author="Adarsh Srivastava",
    author_email="adarshsrivastava.tech@gmail.com",
    description="A Test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adarshSrivastava01/create-python-app",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)
