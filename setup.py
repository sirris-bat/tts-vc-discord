from setuptools import setup

setup(
    name="tts-vc-discord",
    version="0.1",
    packages=["tts-vc-discord"],
    entry_points={
        "console_scripts"; [
            "tts-vc-discord = tts-vc-discord.__main__:main"
        ]
    }
)
