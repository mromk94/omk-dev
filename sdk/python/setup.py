"""Setup script for OMK DEV Python SDK"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="omk-dev",
    version="1.0.0",
    author="OMK Hive Team",
    author_email="dev@omakhive.io",
    description="AI-powered autonomous development assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mromk94/omk-dev",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.10",
    install_requires=[
        "httpx>=0.25.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
        ],
    },
)
