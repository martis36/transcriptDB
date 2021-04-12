/*Select Queries*/
SELECT * FROM Audio_File WHERE Date_Originated > 1960;

SELECT * FROM Tag;

SELECT * FROM Users WHERE User_Type = 'Moderator';

SELECT File_Name, View_Count FROM Audio_File WHERE (View_Count > 100) AND (View_Count < 300) ORDER BY View_Count DESC;

SELECT File_Name, Tag_Name FROM Audio_File_Tags WHERE File_Name = 'Joel Millner';

SELECT File_Name FROM Audio_File WHERE Like_Count > 100;

SELECT File_Name FROM Audio_File WHERE Date_Originated = '1955';

SELECT COUNT (*) FROM Audio_File_Comments WHERE File_Name = 'Joe & Ida Klatzkin';

SELECT SUM(View_Count) FROM AUDIO_FILE;

SELECT * FROM COMMENT WHERE File_Name = 'Joe & Ida Klatzkin';

SELECT User_Comment FROM COMMENT WHERE Date_Created > '1995-12-31';

SELECT File_Name FROM Audio_File WHERE File_Name ILIKE 'Dr%';

SELECT min(Date_Originated) FROM Audio_File;

SELECT * FROM Audio_File ORDER BY View_Count;

SELECT File_Name FROM Audio_File WHERE NOT EXISTS (SELECT * FROM Audio_File WHERE Date_Originated = '2021');

SELECT File_Name, Like_Count FROM Audio_File WHERE Like_Count > ALL (SELECT Like_Count FROM Audio_File WHERE File_Name = 'Joel Millner');

SELECT *  FROM Audio_File_Comments WHERE File_Name =  'Joe & Ida Klatzkin';

SELECT File_Name, Transcript_Link, Suggestion FROM Suggest_File_Edit WHERE View_Count > 100;

SELECT User_ID, User_Type FROM Creator WHERE Creator_ID = '100000';

/*Update Queries*/

UPDATE USERS 
SET User_Type = 'Guest'
WHERE User_ID = '100001';

UPDATE AUDIO_FILE 
SET Transcript_Link = 'https://docs.google.com/document/d/1eSGVzOzxXYplQy9XhMs_Vh-7xg0ME6I_jfVLxC0U8b8/edit' 
WHERE File_Name = 'Rosenthal, Minerva';
/*This updates the Transcript to the wrong link. It is just to demonstrate that it can be updated*/

UPDATE USERS
SET Password = 'soccer05' 
WHERE User_ID = '100001';

UPDATE CAN_SUGGEST_EDITS 
SET Suggestion = 'shorten this transcript because there is redundant info' 
WHERE Suggestion_ID = '1';

UPDATE COMMENT 
SET User_Comment = 'excellent interview' 
WHERE Comment_ID = '3';


/*Delete Queries*/
DELETE FROM COMMENT WHERE Comment_ID = '2';

DELETE FROM AUDIO_FILE WHERE File_Name = 'JHS 55 Samuel Rudner';

DELETE FROM TAG WHERE Tag_Name = 'Europe';

DELETE FROM USERS WHERE User_ID = '100002';

DELETE FROM CAN_SUGGEST_EDITS WHERE Suggestion_ID = '1';

DELETE FROM COMMENT WHERE User_ID = '100003';
/*deletes all comments for a user*/

DELETE FROM COMMENT WHERE File_Name = 'Dr. Paul Loser';

DELETE FROM COMMENT WHERE Comment_ID = '3';

DELETE FROM DEFINES_CHARACTERISTIC_OF WHERE File_Name = 'Dr. Paul Loser';

