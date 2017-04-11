#!/usr/bin/env python2.7


/* Thoughts on priority given JSON data:
    >runtime comes first
    >genre comes second (depending on time of day)
        >comedy, family in the morning
        >biography, western, documentary, sport, war during the afternoon
        >adventure, action, horror, sci-fi, thriller at night
*/
import sys
import os
import re
import json

TIME = 10

def usage(status = 0):
    print '''Usage: {0} [-r TIME ]
    -t TIME  Time (in minutes) allotted for free time '''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)
    
args = sys.argv[1:]
while len(args) and args[0].startswith('-') and len(ags[0]) > 1:
    arg = args.pop(0)
    if arg == '-t':
        TIME = args.pop(0)
    elif arg == '-h':
        usage(0)
    else:
        usage(1)


url = 'https
/* vim: set sts=4 sw=4 ts=8 expandtab ft=c: */
