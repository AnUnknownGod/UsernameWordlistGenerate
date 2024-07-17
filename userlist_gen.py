#!/usr/bin/env python3

from datetime import datetime
import string
import sys

if len(sys.argv) < 2:
    print('Usage: python3 userlist_gen.py (file)->NAMES\nNAMES should contain user\'s name and surname')
    exit(-1)

dot = lambda a: '%s.%s' % (a[0], a[1])
underline = lambda a: '%s_%s' % (a[0], a[1])
concat = lambda a: '%s%s' % (a[0], a[1])


wordlist = ''
with open(sys.argv[1]) as file:
    for line in file:
        user = line.strip().lower()
        
        user = user.split(' ') # Example: John Doe -> johndoe or john.doe...
        user_sname = (user[0], user[1][0]) # Example: John Doe -> johnd or john.d... 
        user_ssurname = (user[0][0], user[1]) # Example: John Doe -> jdoe or j.doe...
        
        format_t = (user, user_sname, user_ssurname)
        
        dot_uname = map(dot, format_t)
        underline_uname = map(underline, format_t)
        concat_uname = map(concat, format_t)

        data = list(dot_uname)
        data += list(underline_uname)
        data += list(concat_uname)

        wordlist += '\n'.join(data) + '\n'

filename = '/tmp/' + datetime.now().strftime('%Y%m%d_%H%M%S_%f_userlist_gen.txt') 
with open(filename, 'w') as file:
    file.write(wordlist)

print('Wrote the output to %s' % filename)
