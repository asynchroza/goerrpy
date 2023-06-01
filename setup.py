from setuptools import setup

setup(
    name='goerrpy',
    version='1.0.3',
    author='Michael Bozhilov',
    author_email='michaelbozhilov@gmail.com',
    description="Decorator for simulating Golang's error handling in Python",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/asynchroza/goerrpy',
    packages=["goerrpy"],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
)