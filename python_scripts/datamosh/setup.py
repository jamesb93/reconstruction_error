import setuptools

setuptools.setup(
    name='datamosh',
    version='1.0',
    author='James Bradbury',
    author_email='jamesbradbury93@gmail.com',
    description='A package containing recipes used in a creative data moshing project',
    packages=['datamosh'],
    install_requires=[
        'PyYAML',
        'python-rapidjson',
        'SoundFile',
        'simpleaudio'
    ]
)