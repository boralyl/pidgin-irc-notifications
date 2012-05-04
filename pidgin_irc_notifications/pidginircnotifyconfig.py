from ConfigParser import SafeConfigParser
import os


class PidginIrcNotifyConfig(object):
    """
    Class for creating/reading/modifying config values for the app
    """

    def __init__(self):
        self.config_dir_path = os.path.expanduser('~/.pidgin-irc-notify/')
        self.config_file_path = os.path.join(self.config_dir_path,
            'settings.conf')
        self.parser = self.get_parser()

    def get_parser(self):
        """
        Returns the parser, and creates default config, if it doesn't exist
        """
        parser = SafeConfigParser({'channels': []})
        exists = parser.read(self.config_file_path)
        if not exists:
            self.create_default_config(parser)

        return parser

    def create_default_config(self, parser):
        """
        Creates a default bare-bones config file
        """
        parser.add_section('irc')
        parser.set('irc', 'channels', '')
        
        # create the full path, and the file
        try:
            os.makedirs(self.config_dir_path, mode=0700)
        except OSError:
            pass
        file_resource = open(self.config_file_path, 'w')
        parser.write(file_resource)

    def parse(self):
        """
        Parses the config file and returns the result
        """
        config = {}
        channels = self.parser.get('irc', 'channels')
        if channels == '':
            channels = []
        else:
            channels = channels.split(',')
        config['channels'] = channels
        return config


