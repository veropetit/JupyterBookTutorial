from setuptools import setup

setup(
    name='ExamplePackage',
    version='0.0.0',    
    description='A example of JupyterBook and packaging',
    url='https://github.com/veropetit/JupyterBookTutorial',
    author='Veronique Petit',
    author_email='vpetit@udel.edu',
    license=' BSD-3-Clause license',
    packages=['ExamplePackage'],
    install_requires=['numpy',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
    ],
)