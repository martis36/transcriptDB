/*The following commands create all the tables in our database. They specify the attributes and their datatypes, the primary key, foreign keys and what they refernce, any chacks necessary, default values, not NULL constraints and what to do ON DELETE and ON UPDATE */

/* Primarily made by Lalima Bhola, Summer Martin, Jared Schmidt, Kyla Ramos */

CREATE TABLE AUDIO_FILE (File_Name text, AF_Link varchar (2048), Transcript_Link varchar (2048), Date_Originated int CHECK ((Date_Originated > 1800) AND (Date_Originated < 2050)), View_Count int DEFAULT '0', Like_Count int DEFAULT '0', PRIMARY KEY (File_Name));

CREATE TABLE TAG (Tag_Name varchar (15) PRIMARY KEY);

CREATE TABLE USERS (UserID SERIAL PRIMARY KEY, Password varchar (255), User_Type varchar (9) CHECK (User_type in ('Admin', 'Moderator', 'Guest') ) DEFAULT 'Guest', User_Creator_ID int DEFAULT '100000', FOREIGN KEY (User_Creator_ID) REFERENCES USERS (UserID) ON DELETE SET DEFAULT ON UPDATE CASCADE);

ALTER SEQUENCE USERS_UserID_seq RESTART WITH 100000;
/* This line is used to insure that the automatic increment for SERIAL starts at 100000, instead of the default value of 1, which is the starting value for userid's in this database */

CREATE TABLE COMMENT (Comment_ID SERIAL PRIMARY KEY, User_Comment varchar (280) NOT NULL, Date_Created DATE, UserID int, File_Name text, FOREIGN KEY (UserID) REFERENCES USERS (UserID) ON DELETE SET NULL ON UPDATE CASCADE, FOREIGN KEY (File_Name) REFERENCES AUDIO_FILE (File_Name) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE DEFINES_CHARACTERISTIC_OF (File_Name text, Tag_Name varchar (15), FOREIGN KEY (Tag_Name) REFERENCES TAG(Tag_Name) ON DELETE CASCADE ON UPDATE CASCADE, FOREIGN KEY (File_Name) REFERENCES AUDIO_FILE (File_Name) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE CAN_SUGGEST_EDITS (Suggestion_ID SERIAL PRIMARY KEY, File_Name text, UserID int, Suggestion varchar (280), FOREIGN KEY (UserID) REFERENCES USERS (UserID) ON DELETE SET NULL ON UPDATE CASCADE, FOREIGN KEY (File_Name) REFERENCES AUDIO_FILE (File_Name) ON DELETE CASCADE ON UPDATE CASCADE);

/*The following commands create necessary views for our database. Users may want to view files, tags, users, etc. based on certain attributes where joining two tables in necessary to recieve the desired search results. The views provide a premade (by this file) "table" which are joins of other tables in the database to make searching easier*/
CREATE VIEW Audio_File_Tags AS SELECT * FROM AUDIO_FILE AS AF NATURAL JOIN DEFINES_CHARACTERISTIC_OF AS DC WHERE AF.File_Name = DC.File_Name;
/*joins audio files and tags based on the name of the audio file*/

CREATE VIEW User_Comments AS SELECT * FROM USERS AS U NATURAL JOIN COMMENT AS C WHERE U.UserID = C.UserID;
/*Joins comments and users based on userid*/

CREATE VIEW Audio_File_Comments AS SELECT * FROM AUDIO_FILE AS AF NATURAL JOIN COMMENT AS C WHERE AF.File_Name = C.File_Name;
/*joins audio files and comments based on the name of the audio file*/

CREATE VIEW Suggest_File_Edit AS SELECT * FROM AUDIO_FILE AS AF NATURAL JOIN CAN_SUGGEST_EDITS AS CSE WHERE AF.File_Name = CSE.File_Name;
/*joins suggestions and audio files based on the name of the audio file*/

CREATE VIEW Creator AS SELECT U.UserID, U.User_Type, U2.USERID AS CREATOR_id, U2.User_Type AS CREATOR_TYPE FROM USERS AS U JOIN USERS AS U2 ON U.User_Creator_ID = U2.UserID;
/*joins users and users. this view was created to allow you to see the user type of the creator of all the other users. this provieds and easy way to check that all created users are created by an admin*/
