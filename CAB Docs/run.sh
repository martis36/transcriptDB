createdb TrentonianaDB
psql -d TrentonianaDB -f /home/lion/Documents/creates.sql
psql -d TrentonianaDB -f /home/lion/Documents/CopyCSV.sql
psql -d TrentonianaDB -f /home/lion/Documents/populate.sql
psql TrentonianaDB
