import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="unattended_upgrades_repos",
    version_config=True,
    author="Abhishek Bhatia",
    author_email="",
    description="Extract missing distro libraries for the unattended_upgrades package config",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abhigenie92/unattended_upgrades_repos",
    packages=setuptools.find_packages(exclude=["tests"]),
    install_requires=['distro>=1.6.0', 'pkce'],
    setup_requires=['setuptools-git-versioning'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
