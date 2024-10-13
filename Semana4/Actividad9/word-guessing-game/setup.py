from setuptools import setup, find_packages

setup(
    name='juego-adivinanza-palabras',
    version='1.0.0',
    description='Un juego de adivinanza de palabras donde el jugador intenta adivinar una palabra secreta letra por letra.',
    author='Daniela',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'behave==1.2.6',      #
        'parse==1.20.2',
        'parse_type==0.6.4',
        'dill==0.3.9',        
        'six==1.16.0',       
    ],
    entry_points={
        'console_scripts': [
            'wordgame =src.main:main',  
        ],
    },
)
