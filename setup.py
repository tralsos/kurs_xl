import setuptools

setuptools.setup(
    name = 'xl',
    packages = ['xl'],
    version = "0.0.2",
    requirements = ['pandas','xlrd'],
    entry_points = {"console_scripts" : ["xl=xl:main"]},

)
