#!/usr/bin/env python

app_name  = "LoCo Council Audit"
# This will tell LP what is running
# This should only be changed if that string is wrong.

lp_teams = "locoteams"

##
## Don't edit below here unless you know what you are doing
############################################################

from launchpadlib.launchpad import Launchpad
from launchpadlib.errors import HTTPError

import string  # For the split
import os
import iso_codes

server    = 'production'
cachedir  = os.path.expanduser("~/.launchpadlib/cache")

print "Connecting to Launchpad..."

launchpad = Launchpad.login_with(app_name, server)

print "Fetching Teams"

locoteams = launchpad.people[lp_teams]
members = locoteams.members_details

print "[review]"

for member in members:
	try:
		team_id = member.member.name
		team_chunks = string.split(team_id, "-") # ubuntu-us
		length = len( team_chunks )

		if length > 1:
			# This ensures format foo-bar(-....)
			if team_chunks[0].lower() == "ubuntu":
				# OK, good. We have the team name in the
				# ubuntu-bar format.
				team_iso_code = team_chunks[1].upper()
				success = False

				for code in iso_codes.ISO_IDS: # Fixme
					if code[1] == team_iso_code:
						print "N: " + team_id + " is from " + code[0] + ". Good."
						success = True
						break
				if not success:
					print "E: " + team_id + " : Has a non ISO code second set id"
			else:
				print "E: " + team_id  + " : Wrong ubuntu-bar-baz format"
		else:
			print "E: " + team_id + " : Wrong foo-bar-baz format."

	except HTTPError, e:
		pass

