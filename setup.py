import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="terraenv",
    version="0.8",
    author="Aarat Nathwani",
    author_email="me@aarat.com",
    description="Terraform and Terragrunt Version Manager",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/aaratn/terraenv",
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=['terraenv'],
    install_requires=[
        "altgraph==0.16.1",
        "appdirs==1.4.3",
        "beautifulsoup4==4.8.1",
        "bs4==0.0.1",
        "certifi==2019.9.11",
        "chardet==3.0.4",
        "cssselect==1.1.0",
        "fake-useragent==0.1.11",
        "idna==2.8",
        "lxml==4.4.1",
        "macholib==1.11",
        "parse==1.12.1",
        "pyee==6.0.0",
        "pyppeteer==0.0.25",
        "pyquery==1.4.1",
        "python-dotenv==0.10.3",
        "requests==2.22.0",
        "requests-html==0.10.0",
        "six==1.13.0",
        "soupsieve==1.9.5",
        "tqdm==4.38.0",
        "urllib3==1.25.7",
        "w3lib==1.21.0",
        "websockets==8.1"
    ]
)