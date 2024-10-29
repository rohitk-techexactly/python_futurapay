from setuptools import setup, find_packages

setup(
    name="futurapay",
    version="0.3.4",
    packages=find_packages(include=["Futurapay", "Futurapay.*"]),
    install_requires=['cryptography'],
    author="Rohit kumar",
    author_email="rohitk.techexactly@gmail.com",
    description="A simple package for testing purposes",
    # long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Rohit-kumar-raja/pythonTestpackage.git",
    include_package_data=True,
   
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
