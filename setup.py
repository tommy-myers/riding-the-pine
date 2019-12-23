import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="riding-the-pine-YOUR-USERNAME-HERE",  # replace user name
    version="0.0.1",
    author='Thomas Myers',
    author_email='tom.myers2@yahoo.com',
    description='No more slow code with Python, use ride the pine to benchmark',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='SOME GIT HUB',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.8',
)
