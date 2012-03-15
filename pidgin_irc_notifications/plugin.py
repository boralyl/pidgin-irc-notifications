#!/usr/bin/env python
import argparse
import dbus
from dbus.mainloop.glib import DBusGMainLoop
import gobject
import pynotify


class IRCNotificationPlugin(object):
    """
    Pidgin IRC Notification 'plugin'
    """
    
    def __init__(self, args):
        self.channels = args.channels
        
        bus = dbus.SessionBus()
        # Add sginal receiver for irc chat msg
        bus.add_signal_receiver(self.received_chat_msg_callback,
            dbus_interface="im.pidgin.purple.PurpleInterface",
            signal_name="ReceivedChatMsg")
        
        # Get the pidgin purple interface
        obj = bus.get_object("im.pidgin.purple.PurpleService",
            "/im/pidgin/purple/PurpleObject")
        self.purple = dbus.Interface(obj, "im.pidgin.purple.PurpleInterface")

    def received_chat_msg_callback(self, account, sender, message, conversation, flags):
        """
        Creates a notification for IRC channel message if in one of the
        approved channels.
        """
        try:
            # username in format user@irc.someserver.net
            username = self.purple.PurpleAccountGetUsername(account).split('@')[0]
        except IndexError:
            print "Whoops...username wasn't in expected format..."
            return
        channel = self.purple.PurpleConversationGetTitle(conversation)
        if channel in self.channels and username != sender:
            msg = "%s said: %s" % (sender, message)
            n = pynotify.Notification(channel, msg).show()

        
def parse_args():
    parser = argparse.ArgumentParser(description="Enables notifications in"
        " irc channels provided in Pidgin.")
    parser.add_argument("channels", nargs="+", help="Channel names (i.e. '#django' '#ubuntu')")
    return parser.parse_args()
        

def main():
    """
    Runs main loop and sets up listener
    """
    # Get command line args
    args = parse_args()

    # Initialize pynotify
    pynotify.init('Initializing IRC Notifications...')

    # Setup dbus glib mainloop
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    
    # Init plugin
    IRCNotificationPlugin(args)

    # Obtain main loop and run it
    gobject.MainLoop().run()


if __name__ == "__main__":
    main()
