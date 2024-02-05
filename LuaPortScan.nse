#!/usr/bin/python3


# Script Name: Lua Port Scanning Script
# Author: Shay Crane
# Date of last revision: 11/18/2022
# Purpose: scan ports on a given target host
# To run script from terminal use the following syntax structure:  
#   "Nmap -sV --script [lua script name] [arguments if any] [hostame]"



-- HEAD --

description = [[
This is a custom script I made for Lab 35 that determines if a port is open.
]]

author = "Shay C."

-- RULE --

portrule = function(host, port)
	return port.protocol == "rdp"
		and port.state == "open"
end

-- ACTION --

action = function(host, port)
	return "This port is open!"
end
