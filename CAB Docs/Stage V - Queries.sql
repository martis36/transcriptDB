/*This file contains numerous Select, Update, and Delete queries that the user may need or want to implement. The creation of these queries was a group effort and each was tested twice to ensure they were correct, relevent and that the result did not contain suerious tuples. The values of the queries may be changed depending on what you're interesting in doing, in what table, and based on what value. There are several complex queries as well as more relatively simple ones. Below each query is a */

/* Primarily made by Lalima Bhola, Summer Martin, Jared Schmidt, Kyla Ramos */

/*** THESE ARE ONLY EXAMPLES PLEASE DO NOT EXECUTE THE ENTIRE FILE AT ONCE. THANK YOU. ***/

/*These are some exampels of Select Queries*/

SELECT * FROM Audio_File WHERE Date_Originated > 1960;
/*fins all the audio files created before a certian year*/

SELECT * FROM Tag;
/*allows you to see all the tags available. Note that some may not be used within the database to describe an audio file*/

SELECT * FROM Users WHERE User_Type = 'Moderator';
/* result displays all the users of a certain clearance level*/

SELECT File_Name, View_Count FROM Audio_File WHERE (View_Count > 100) AND (View_Count < 300) ORDER BY View_Count DESC;
/* displays the name and view count of an audio file based on a certain range of view and sorts the result in order from highest to lowest*/

SELECT File_Name, Tag_Name FROM Audio_File_Tags WHERE File_Name = 'Joel Millner';
/*Gives all the tags for some audio file given a audio file name*/

SELECT File_Name FROM Audio_File WHERE Like_Count > 100;
/*finds audio files with a certain like count*/

SELECT File_Name FROM Audio_File WHERE Date_Originated = '1955';
/*finds audio files that originate in a specific year*/

SELECT COUNT (*) FROM Audio_File_Comments WHERE File_Name = 'Joe & Ida Klatzkin';
/*gives the number of comments an audio file has had*/

SELECT SUM(View_Count) FROM AUDIO_FILE;
/*gives the total number of views for all audio files*/

SELECT * FROM COMMENT WHERE File_Name = 'Joe & Ida Klatzkin';
/*finds all the comments made on some audio file*/

SELECT User_Comment FROM COMMENT WHERE Date_Created > '1995-12-31';
/*finds all the user comments made before a certain date*/

SELECT File_Name FROM Audio_File WHERE File_Name ILIKE 'Dr%';
/*finds all the audio files where the name of the file starts with DR*/

SELECT min(Date_Originated) FROM Audio_File;
/*find the audio file with the smallest(earliest) origination date*/

SELECT * FROM Audio_File ORDER BY View_Count;
/*order all the audio files by the number of views*/

SELECT File_Name FROM Audio_File WHERE NOT EXISTS (SELECT * FROM Audio_File WHERE Date_Originated = '2021');
/*select all the audio files that did not originate in 2021*/

SELECT File_Name, Like_Count FROM Audio_File WHERE Like_Count > ALL (SELECT Like_Count FROM Audio_File WHERE File_Name = 'Joel Millner');
/*Get all the audio files who have a like count greater the the like count of the Joel Millner* file/

SELECT *  FROM Audio_File_Comments WHERE File_Name =  'Joe & Ida Klatzkin';
/*select all the tuples from the audio file comments view for a given audio file*/

SELECT File_Name, Transcript_Link, Suggestion FROM Suggest_File_Edit WHERE View_Count > 100;
/*returns the specified attributes from suggest file edits on files that have a view count higher then 100. This is good to deal with suggestions of more popular files first. You can also order the results by view count in decending order to get the suggestions for the most viewed files first*/

SELECT UserID, User_Type FROM Creator WHERE Creator_ID = '100000';
/*get the id and types of all the users a creator has ever made*/


/*These are some examples of Update Queries*/

UPDATE USERS 
SET User_Type = 'Guest'
WHERE UserID = '100001';

UPDATE AUDIO_FILE 
SET Transcript_Link = 'https://docs.google.com/document/d/1eSGVzOzxXYplQy9XhMs_Vh-7xg0ME6I_jfVLxC0U8b8/edit' 
WHERE File_Name = 'Rosenthal, Minerva';
/*This updates the Transcript to the wrong link. It is just to demonstrate that it can be updated*/

UPDATE USERS
SET Password = 'soccer05' 
WHERE UserID = '100001';
/*This updates a users password*/

UPDATE CAN_SUGGEST_EDITS 
SET Suggestion = 'shorten this transcript because there is redundant info' 
WHERE Suggestion_ID = '1';
/*this updates/edits a specific suggestion*/

UPDATE COMMENT 
SET User_Comment = 'excellent interview' 
WHERE Comment_ID = '3';
/*This edits/updates a certain comment*/



/*These are some examples of Delete Queries*/

DELETE FROM COMMENT WHERE Comment_ID = '2';

DELETE FROM AUDIO_FILE WHERE File_Name = 'JHS 55 Samuel Rudner';
/*deletes a file with a certain name*/

DELETE FROM TAG WHERE Tag_Name = 'Europe';
/*deletes a tag*/

DELETE FROM USERS WHERE UserID = '100002';
/*deletes a user given a userid*/

DELETE FROM CAN_SUGGEST_EDITS WHERE Suggestion_ID = '1';
/*deletes a suggestion given a suggestion_id number*/

DELETE FROM COMMENT WHERE UserID = '100003';
/*deletes all comments for a user*/

DELETE FROM COMMENT WHERE File_Name = 'Dr. Paul Loser';
/*deletes an audio file given an audio file name*/

DELETE FROM COMMENT WHERE Comment_ID = '3';
/*deletes a comment given a comment id*/

DELETE FROM DEFINES_CHARACTERISTIC_OF WHERE File_Name = 'Dr. Paul Loser';
/*deletes all tuples which relate a tag to an audio file given the name of the audio file*/

