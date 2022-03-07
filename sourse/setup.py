from setuptools import setup

# -*- coding: utf-8 -*-
TOKEN = "5038288042:AAHIZfCj2HqCmUlTrVMt5oQU5TmHAL9Fcco"  # Insert your bot token here - required!
# Optionally use an anonymizing proxy (SOCKS/HTTPS) if you encounter Telegram access issues in your region
PROXY = ""

setup(
    name="Food_bot",
    version="0.9",
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
