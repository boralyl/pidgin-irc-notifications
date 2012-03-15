Requirements
============
* libnotify
* pynotify

Install
=======
`sudo python setup.py install`

Running
=======
After installation run:

`pidgin-irc-notify '#mychannel' '#myotherchannel' &`

This will enable notifications in pidgin for the irc channels #mychannel and #myotherchannel, but no other channels you may have open.  For further documentation run:

`pidgin-irc-notify -h`

But How?
--------
This little script uses dbus to listen for events and fires off callbacks to functions.
