from setuptools import setup


setup(
    name='Pidgin IRC Notifications',
    version='0.2.0',
    url='https://bitbucket.org/boralyl/pidgin-irc-notifications',
    description='Enables notifications for specified IRC chats.',
    author='Aaron Godfrey',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
    packages=['pidgin_irc_notifications'],
    entry_points={
        'console_scripts': [
            'pidgin-irc-notify = pidgin_irc_notifications.plugin:main',
        ],
    }
)
