#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict

import setuptools

with open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

name = "bcc_fe_exchange_model"
version = "0.1"
release = "0.1.0"

setuptools.setup(
    name=name,
    author="James K. Glasbrenner",
    author_email="jglasbr2@gmu.edu",
    license="Creative Commons Attribution-ShareAlike 4.0 International",
    version=release,
    project_urls=OrderedDict((
        ("Repo", "https://github.com/jkglasbrenner/bcc-fe-exchange-model"),
    )),
    description=(
        "A tutorial on how to obtain magnetic exchange parameters for BCC Fe "
        "using first-principles density functional theory calculations."
    ),
    long_description=readme,
    python_requires=">=3.6",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "jupyter >= 1.0",
        "matplotlib >= 2.0",
        "neighbormodels == 0.1.0",
        "numpy >= 1.14",
        "pandas >= 0.23",
        "pymatgen >= 2018.4.20",
        "scikit-learn >= 0.19",
        "statsmodels >= 0.9",
    ],
    extras_require={
        "dev": [
            "autopep8 == 1.3.5",
            "cython >= 0.28.4",
            "flake8 == 3.5.0",
            "importmagic == 0.1.7",
            "ipython >= 6.5",
            "jedi >= 0.12",
            "msgpack == 0.5.6",
            "monty >= 1.0",
            "nbdime >= 1.0",
            "pycodestyle == 2.3.1",
            "pydocstyle == 2.1.1",
            "pytest == 3.7.0",
            "rope == 0.10.7",
            "ruamel.yaml == 0.15.50",
            "yamllint == 1.11.1",
            "yapf == 0.22.0",
        ],
    },
)
