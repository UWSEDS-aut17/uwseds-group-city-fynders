import sys
try:
    from setuptools import setup
except:
    from distutils.core import setup

if sys.version_info.major != 3:
    print('-----------------------------------------')
    print('  ERROR: cityfynders requires Python 3!')
    print('-----------------------------------------')
    exit(1)


opts = dict(name='cityfynders',
            description='A python package helping with finding the city to live in US',
            url='https://github.com/UWSEDS-aut17/uwseds-group-city-fynders',
            version='1.0',
            packages=['cityfynders'],
            install_requires=['numpy',
                              'pandas',
                              'geopy',
                              'dash',
                              'dash-renderer',
                              'dash-html-components',
                              'dash-core-components',
                              'plotly'
                              ]
            )


if __name__ == '__main__':
    setup(**opts)
