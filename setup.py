from setuptools import setup, find_packages

setup(
    name="turkeysms-python",
    version="4.0.0",
    description="Official TurkeySMS API V4 Python SDK",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="TurkeySMS Team",
    author_email="support@turkeysms.com.tr",
    url="https://github.com/turkeysms/python",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
