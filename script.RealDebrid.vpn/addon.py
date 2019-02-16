import xbmcaddon
import xbmcgui
import urllib2
import re
import sys

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')

req = urllib2.Request("https://real-debrid.com/vpn")
response = urllib2.urlopen(req)
lines = response.readlines()

line1 = ""
line2 = ""
line3 = ""

vpnInfo = False
for line in lines:
    line = line.strip(' \t\n\r')
    x = re.search("VPN Information", line)
    if not x == None:
       vpnInfo = True
    else:
       if vpnInfo and line != "":
         line1 = re.sub(r"\<[^>]+\>", "", line)
         vpnInfo = False

    x = re.search("Your IP Address:", line)
    if not x == None:
      line2 = re.sub(r"\<[^>]+\>", "", line)

    x = re.search("Your IP Reverse:", line)
    if not x == None:
      line3 = re.sub(r"\<[^>]+\>", "", line)

    if line1 != "" and line2 != "" and line3 != "":
      break

xbmcgui.Dialog().ok("https://real-debrid.com/vpn", line2, line3, line1)

