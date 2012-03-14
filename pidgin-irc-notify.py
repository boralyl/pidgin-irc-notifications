#!/usr/bin/env python
import dbus
from dbus.mainloop.glib import DBusGMainLoop
import gobject
import pynotify


# Add approved channels here
APPROVED_CHANNELS = (
    #'#django',
)

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus()
obj = bus.get_object("im.pidgin.purple.PurpleService",
"/im/pidgin/purple/PurpleObject")
purple = dbus.Interface(obj, "im.pidgin.purple.PurpleInterface")


def received_chat_msg_callback(account, sender, message, conversation, flags):
    """
    Creates a notification for IRC channel message if in one of the
    approved channels.
    """
    try:
        # username in format user@irc.someserver.net
        username = purple.PurpleAccountGetUsername(account).split('@')[0]
    except IndexError:
        print "Whoops...username wasn't in expected format..."
        return
    channel = purple.PurpleConversationGetTitle(conversation)
    if channel in APPROVED_CHANNELS and username != sender:
        msg = "%s said: %s" % (sender, message)
        n = pynotify.Notification(channel, msg).show()


def main():
    """
    Runs main loop and sets up listener
    """
    pynotify.init('Initializing IRC Notifications...')

    bus.add_signal_receiver(received_chat_msg_callback,
        dbus_interface="im.pidgin.purple.PurpleInterface",
        signal_name="ReceivedChatMsg")
    
    loop = gobject.MainLoop()
    loop.run()


if __name__ == "__main__":
    main()
