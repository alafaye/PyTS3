PyTS3
-----

PyTS3 is a python module with classes to interact with the Teamspeak 3 Query 
Interface.

It is very easy to use
```````````````````````

For example to get a list of all virtualservers at the host server.
::

	import PyTS3
	server = PyTS3.ServerQuery('thelabmill.de', 10011)
	server.connect()
	serverlist = server.command('serverlist')
	for server in serverlist:
	    print server["virtualserver_name"]
	
Easy to install
```````````````

::

	$ easy_install PyTS3
	$ python virualservers.py

Links
`````

* `source repository <http://bitbucket.org/ChristophHeer/pyts3/>`_
* `documentation <http://bitbucket.org/ChristophHeer/pyts3/wiki/Home>`_

