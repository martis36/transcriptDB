/*Ths file is used to drop all the tables and views in the database.
Type
./drop.sql 
and hit enter in your terminal to use. 
If you would like to delete the database also type 
\q 
and hit enter to remove yourself from the database and type
dropdb TrentonianaDB
which will delete the database from your system completely. You may also simply delete the whole database without having to drop everything in it. */

/* Primarily made by Kyla Ramos and Summer Martin */

DROP VIEW Creator;
DROP VIEW Audio_File_Tags;
DROP VIEW User_Comments;
DROP VIEW Audio_File_Comments;
DROP VIEW Suggest_File_Edit;
DROP TABLE CAN_SUGGEST_EDITS;
DROP TABLE DEFINES_CHARACTERISTIC_OF;
DROP TABLE COMMENT;
DROP TABLE USERS;
DROP TABLE TAG;
DROP TABLE AUDIO_FILE;
