import setuptools

VERSION = "0.0.1"  # PEP-440

NAME = "TruckersMP-async"

INSTALL_REQUIRES = [
    "aiohttp",
]


setuptools.setup(
    name=NAME,
    version=VERSION,
    description="An asynchronous TruckersMP API wrapper for grabbing data.",
    url="https://github.com/RainzDev/TruckersMP.py/",
    project_urls={
        "Source Code": "https://github.com/RainzDev/TruckersMP.py/",
    },
    author="Jess",
    author_email="jessrblx16@gmail.com",
    license="MIT License",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.10",
    ],
    # Snowpark requires Python 3.8
    python_requires=">=3.8",
    # Requirements
    install_requires=INSTALL_REQUIRES,
    packages=["TruckersMP-async"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
