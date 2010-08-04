#!/usr/bin/env python
###
##
## MoinMoin stalking stuff for teams who have not
##  finished their damn reports. Use this wisely.
##

URL_PREFIX  = "https://wiki.ubuntu.com/"
URL_POSTFIX = "/TeamReports/Current?action=raw"


import re
import datetime
import urllib, urllib2

## This needs to produce the raw of the wiki

## timedate regexp

REGEXP_BABYMAKER        = "\(([^\)]*)\)"
REGEXP_BABYMAKER_SEARCH = "<<(.*)>>"

now = datetime.datetime.now()

pathspec = "TeamReports"
year     = now.strftime("%y") ## 09, 10, 11
month    = now.strftime("%B") ## Aug, Jul...

COMPAREPATH = "/" + pathspec + "/" + year +  "/" + month

##
##
##

teams = [
    "OhioTeam",
    "LoCoCouncil",
]

for team in teams:
	f = urllib.urlopen( URL_PREFIX + team + URL_POSTFIX )
	wikipage = f.read()
	lines = wikipage.split("\n");

	for line in lines:
		## print line
		if re.match(REGEXP_BABYMAKER_SEARCH, line):
			m = re.search(REGEXP_BABYMAKER, line)
			reportID = m.group(0)[1:-1]
	
			if reportID != team + COMPAREPATH:
				#print "Expected: " + team + COMPAREPATH
				#print "They are: " + reportID
				print team + "'s report is not current for the month of " + now.strftime("%B")
			else:
				print team + "'s report is current for the month of " + now.strftime("%B")


#for team in teams:
#	print URL_PREFIX + team + URL_POSTFIX;
	
