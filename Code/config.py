#!/usr/bin/python3

# This code was taken from Professor DeGood's example and was unchanged.
# There is no maintenance information.
"""
This code is from:
https://www.postgresqltutorial.com/postgresql-python/
"""

from configparser import ConfigParser
 
 
def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return db
