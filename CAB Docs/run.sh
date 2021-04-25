# This file was primarily made by Lalima Bhola and Summer Martin

#this line is to create a database named TrentonianaDB
createdb TrentonianaDB

#this line reads and runs an sql file named creates which creates all the tables and needed views in the database. The path to this file may need to be changed depending on where the file is kept on your system. 
psql -d TrentonianaDB -f /home/lion/Documents/creates.sql

#this line reads the sql file called CopyCSV. You must have superuser permissions in order for the Copy function to work. The CopyCSV file reads the values from AFT.csv which contains all the values needed for the Audio_File table and uses those values to populate the table. The path may need to be changed.
psql -d TrentonianaDB -f /home/lion/Documents/CopyCSV.sql

#this line reads the sql file called populate which contains all the sql commands and values to populate the remaining tables. The path to this file may need to be changed.
psql -d TrentonianaDB -f /home/lion/Documents/populate.sql

#The next line is currently commented out, but if you would like to work in the database to make changes or updates, this line can be uncommented out so that you will end up in the database system and all set to make changes.

#psql TrentonianaDB
