#!/usr/bin/env python


app_name  = "LoCo Council Audit"
# This will tell LP what is running
# This should only be changed if that string is wrong.

output    = "./data/dataset"
# This will be combined with the team name to set up
# the output file ( output-team-name )


team_all  = "locoteams"
team_app  = "locoteams-approved"

##
## Don't edit below here unless you know what you are doing
############################################################

from launchpadlib.launchpad import Launchpad
from launchpadlib.errors import HTTPError

import time
import datetime
from datetime import date

import os
import json
import sys


server    = 'edge'
cachedir  = os.path.expanduser("~/.launchpadlib/cache")

launchpad = Launchpad.login_with(app_name, server)

approved_teams = {}
global_teams   = {}

all_teams = launchpad.people[team_all]
all_members = all_teams.members_details

for member in all_members:
	global_teams[member.member.name] = member.member.display_name

app_teams   = launchpad.people[team_app]
app_members = app_teams.members_details

for member in app_members:
	approved_teams[member.member.name] = member.member.display_name

print "Approved Teams: "
for team in approved_teams:
	try:
		print team + " ( " + approved_teams[team] + " ) "
	except UnicodeEncodeError:
		print team + " ( Non ascii display name ) "

print ""
print "Unapproved Teams"
for team in global_teams:
	try:
		trash = approved_teams[team]
	except KeyError:
		try:
			print team + " ( " + global_teams[team] + " ) "
		except UnicodeEncodeError:
			print team + " ( Non ascii display name )"


