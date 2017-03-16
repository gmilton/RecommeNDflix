#!/bin/sh

# Grace Milton
# CSE 20312 Lab 06
# test_pp.sh
#
# Part of evidence of execuatble code I have checked into our repository.
#
# Test program for python_practice.py
# Should display a schedule of alternating episodes of:
#	Season 4 of Stargate SG-1 under name 'SG-1'
#	Season 6 of Hawaii Five-0 under name 'H50'
#	Season 1 of Merlin
#	Season 1 of Luke Cage under name 'Luke'
#	Season 1 of Robin Hood under name 'Robin'

./python_practice.py -n 5 'Stargate SG-1' -s 4 -a 'SG-1' 'Hawaii Five-0' -s 6 -a 'H50' 'Merlin' 'Luke Cage' -a 'Luke' 'Robin Hood' -a 'Robin'
