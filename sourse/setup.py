from setuptools import setup

# -*- coding: utf-8 -*-
TOKEN = ""  # Insert your bot token here - required!
# Optionally use an anonymizing proxy (SOCKS/HTTPS) if you encounter Telegram access issues in your region
PROXY = ""

setup(
    name="food_bot",
    version="0.1",
    description="",
    url="",
    author="",
    author_email="",
    license="",
    packages=[""],
    install_requires=[
        "telegram",
        "pymysql",
    ],
    entry_points={
        "console_scripts": [
            "",
        ]
    },
)
