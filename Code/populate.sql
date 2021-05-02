/*This file contains all of the values and tuples we are inserting into each database table. You may add values into this file, but be sure to check for foreign keys and restrictions in the create.sql file which specifies the datatypes, and restrictions for each atrtibute value*/

/* Primarily made by Lalima Bhola, Summer Martin, Jared Schmidt, Kyla Ramos */

/*This line inserts sveral tag tuples into the Tag table*/
INSERT INTO TAG (Tag_Name) VALUES ('Trenton'), ('History'), ('Culture'), ('Photograph'), ('New Jersey'), ('Ewing'), ('Yearbook'), ('School'), ('Church'), ('Club'), ('Library'), ('Interview'), ('Old Trenton'), ('Neighborhood'), ('Sport'), ('Game'), ('Shooting'), ('Safety'), ('Crime'), ('Kids'), ('Art'), ('Music'), ('Money'), ('Law'), ('Rules'), ('Life'), ('Childhood'), ('Social'), ('Society'), ('Politics'), ('Economy'), ('TCNJ'), ('College'), ('Museum'), ('House'), ('Immigration'), ('Jewish'), ('Liquor'), ('Lawyer'), ('Family'), ('Business'), ('Philadelphia'), ('Immigrant'), ('Europe'), ('Development'), ('Youth'), ('Truck'), ('Improve');

/*The following lines inserts several user tuples into the Users table in the database. Notice it is not necessary to enter a userid because the database will give the user one automatically. The user_creator value also has a default so it does not necessarily have to be specified*/
INSERT INTO USERS (Password, User_Type) VALUES ('dfvjh348', 'Admin');

INSERT INTO USERS (Password, User_Type) VALUES ('vwlijd827', 'Moderator');

INSERT INTO USERS (Password, User_Type) VALUES ('cerulian298', 'Moderator');

INSERT INTO USERS (Password, User_Type) VALUES ('gernal9823', 'Guest');

INSERT INTO USERS (Password, User_Type) VALUES ('random2984', 'Guest');

/* The next lines are some examples of comment tuples which we insert in the database*/
INSERT INTO COMMENT (User_Comment, Date_Created, UserID, File_Name) VALUES ('this is an example comment', '2021-04-10', '100001', 'Joel Millner');

INSERT INTO COMMENT (User_Comment, Date_Created, UserID, File_Name) VALUES ('another comment text', '2021-04-20', '100000', 'Rosenthal, Minerva');

INSERT INTO COMMENT (User_Comment, Date_Created, UserID, File_Name) VALUES ('first comment', '2021-04-11', '100004', 'Joe & Ida Klatzkin');

/*The next command inserts several tuples into the defines characteristic of table which assigns some tags to each audio file. Note that both the audio file name and the tag name must be specified */
INSERT INTO DEFINES_CHARACTERISTIC_OF (File_Name, Tag_Name) VALUES ('Joel Millner', 'Immigration'), ('Joel Millner', 'Jewish'), ('Joel Millner', 'Truck'), ('Joel Millner', 'History'), ('JHS 55 Samuel Rudner', 'Immigration'), ('JHS 55 Samuel Rudner', 'Liquor'), ('JHS 55 Samuel Rudner', 'Lawyer'), ('JHS 55 Samuel Rudner', 'Jewish'), ('Rosenthal, Minerva', 'Immigration'), ('Rosenthal, Minerva', 'Family'), ('Rosenthal, Minerva', 'Business'), ('Rosenthal, Minerva', 'Jewish'), ('Joe & Ida Klatzkin', 'Philadelphia'), ('Joe & Ida Klatzkin', 'Immigrant'), ('Joe & Ida Klatzkin', 'Europe'), ('Joe & Ida Klatzkin', 'Ewing'), ('Dr. Paul Loser', 'Development'), ('Dr. Paul Loser', 'Improve'), ('Dr. Paul Loser', 'School'), ('Dr. Paul Loser', 'Youth');

/* The next lines are some examples of suggestion tuples which we insert in the database*/
INSERT INTO CAN_SUGGEST_EDITS (File_Name, UserID, Suggestion) VALUES('Joe & Ida Klatzkin', '100000', 'Line 42 should be changed');

INSERT INTO CAN_SUGGEST_EDITS (File_Name, UserID, Suggestion) VALUES('Rosenthal, Minerva', '100001', 'I heard this instead of that');

INSERT INTO CAN_SUGGEST_EDITS (File_Name, UserID, Suggestion) VALUES('Dr. Paul Loser', '100003', 'A cool suggestion');

