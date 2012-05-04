Requirements
============
* libnotify
* pynotify

Install
=======
`sudo python setup.py install`

Configuration
=============
Upon the first run a config file will be created in your home directory named `~/.pidgin-irc-notify/settings.conf`

You can add default channels to monitor (instead of specifying them all individually at the command line) by suppying a comma seperated list of channels to the channels option:

    [irc]
    channels = #foo,#bar,#django

Running
=======
After installation run:

`pidgin-irc-notify '#mychannel' '#myotherchannel' &`

This will enable notifications in pidgin for the irc channels #mychannel and #myotherchannel, but no other channels you may have open.  For further documentation run:

`pidgin-irc-notify -h`

But How?
--------
This little script uses dbus to listen for events and fires off callbacks to functions.
