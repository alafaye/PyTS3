from distutils.core import setup

setup(
    name="PyTS3",
    version="0.3",
    description="""A python modul to use the Teamspeak Query Interface.""",
	long_description=__doc__,
    author="Christoph Heer",
    author_email="Christoph.Heer@googlemail.com",
    license="MIT License",
    url="http://bitbucket.org/ChristophHeer/pyts3/",
    py_modules=["PyTS3"],
	platforms='any',
	classifiers=[
	        'Development Status :: 4 - Beta',
	        'Intended Audience :: Developers',
	        'License :: OSI Approved :: MIT License',
	        'Operating System :: OS Independent',
	        'Programming Language :: Python',
	        'Topic :: Communications',
	        'Topic :: Terminals :: Telnet'
	])
