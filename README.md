Requirements
============
* libnotify
* pynotify

Configuration
=============
Add any channel names you want to the APPROVED_CHANNELS tuple.  Make sure to include the hash tag (i.e. #django)

Running
=======
Make pidgin-irc-notify.py executable and start it up as a background process via `./pidgin-irc-notify.py &`

But How?
--------
This little script uses dbus to listen for events and fires off callbacks to functions.
