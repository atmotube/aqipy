from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='aqipy-atmotech',
    packages=find_packages(include=['aqipy']),
    version='0.1.1',
    description='AQI calculation library',
    author='Atmotech Inc.',
    author_email='info@atmotube.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache-2.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    python_requires='>=3.6',
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)
