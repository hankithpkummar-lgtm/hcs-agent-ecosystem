"""
AutoDesigner Pro - Setup
========================
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="autodesigner-pro",
    version="2.0.0",
    author="AutoDesigner Team",
    description="Premium Website Design Agent - Automatically enhances any website with expert design",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-org/autodesigner-pro",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "autodesigner=designer_agent.__main__:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
