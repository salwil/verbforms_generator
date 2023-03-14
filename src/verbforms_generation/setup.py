import setuptools

setuptools.setup(name='verbforms_generation',
version='1.0',
description='Verbforms generation package',
url='https://github.com/salwil/verbforms_generator',
author='Jana Hofmann, Salome Wildermuth',
python_requires='>=3.8',
install_requires=[],
entry_points={
        'console_scripts': [
            'verbforms_start = verbforms_generation.main:main']
    },
author_email='jana.hofmann@uzh.ch, salome.wildermuth@uzh.ch',
packages=setuptools.find_packages())