/*This file is designed to read lines from the AFT.csv file and transfer them into the database table Audio_File. More lines may be added to AFT if desired, to include more instances of audio files. Superuser permissions must be activated for your account in order to use the Copy function*/
COPY AUDIO_FILE(FILE_NAME, AF_LINK, TRANSCRIPT_LINK, DATE_ORIGINATED) FROM '/home/lion/Documents/AFT.csv' DELIMITER ',' CSV HEADER;

/*
Maintenance: path to CSV file must be changed if using a different system or the files are in a different directory
Program works best if the files are in the main Documents folder

Primarily made by Summer Martin

Code derived from: https://www.postgresqltutorial.com/import-csv-file-into-posgresql-table/
*/
