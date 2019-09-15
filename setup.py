from setuptools import setup, find_namespace_packages

setup(
    name="opengl-api-registry-reader",
    author="Einar Forselv",
    author_email="eforselv@gmail.com",
    description="A simple tool for extracting information from the OpenGL API Registry",
    install_requires=[
        'requests<3',
    ],
)
