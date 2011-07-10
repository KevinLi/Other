#!/usr/bin/env python
__module_name__ = "invitespam.py"
__module_version__ = "1.0.0.0"
__module_description__ = "Joins a user to a specified number of randomly \
						 named channels, invites a different user to them, \
						 and parts the first user from all of them."
__module_author__ = "Kevin Li"

import xchat
import random

channels = []
random.seed()

def main(word, word_eol, userdata):
	if int(word[2]) <= 15:
		create_channels(int(word[2]))
		for i in channels:
			xchat.command("JOIN {0}".format(i))			
			xchat.command("INVITE {0} {1}".format(word[1], i))
			xchat.command("PART {0}".format(i))
		del channels[:]
	return None
	
def create_channels(number):
	for i in range(number):
		channels.append("#" + str(int(random.random() * pow(10, 11))))

#xchat.hook_print('Channel Message', msgparse)
xchat.hook_command('invitespam', main, help="/invitespam user number")
print("Loaded {0}, version {1}".format(__module_name__, __module_version__))
