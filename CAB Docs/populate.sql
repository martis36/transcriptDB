INSERT INTO TAG (Tag_Name) VALUES ('Trenton'), ('History'), ('Culture'), ('Photograph'), ('New Jersey'), ('Ewing'), ('Yearbook'), ('School'), ('Church'), ('Club'), ('Library'), ('Interview'), ('Old Trenton'), ('Neighborhood'), ('Sport'), ('Game'), ('Shooting'), ('Safety'), ('Crime'), ('Kids'), ('Art'), ('Music'), ('Money'), ('Law'), ('Rules'), ('Life'), ('Childhood'), ('Social'), ('Society'), ('Politics'), ('Economy'), ('TCNJ'), ('College'), ('Museum'), ('House'), ('Immigration'), ('Jewish'), ('Liquor'), ('Lawyer'), ('Family'), ('Business'), ('Philadelphia'), ('Immigrant'), ('Europe'), ('Development'), ('Youth'), ('Truck'), ('Improve');

/*crypt('CAT', gen_salt('bf'))*/

INSERT INTO USERS (User_ID, Password, User_Type) VALUES ('100000', 'CAT', 'Admin');

INSERT INTO USERS (User_ID, Password, User_Type) VALUES ('100001', 'BAT', 'Moderator');

INSERT INTO USERS (User_ID, Password, User_Type) VALUES ('100002', 'MAT', 'Moderator');

INSERT INTO USERS (User_ID, Password, User_Type) VALUES ('100003', 'PAT', 'Guest');

INSERT INTO USERS (USER_ID, Password, User_Type) VALUES ('100004', 'HAT', 'Guest');

INSERT INTO COMMENT (User_Comment, Date_Created, User_ID, File_Name) VALUES ('this is an example comment', '2021-04-10', '100001', 'Joel Millner');

INSERT INTO COMMENT (User_Comment, Date_Created, User_ID, File_Name) VALUES ('another comment text', '2021-04-20', '100000', 'Rosenthal, Minerva');

INSERT INTO COMMENT (User_Comment, Date_Created, User_ID, File_Name) VALUES ('first comment', '2021-04-11', '100004', 'Joe & Ida Klatzkin');

INSERT INTO DEFINES_CHARACTERISTIC_OF (File_Name, Tag_Name) VALUES ('Joel Millner', 'Immigration'), ('Joel Millner', 'Jewish'), ('Joel Millner', 'Truck'), ('Joel Millner', 'History'), ('JHS 55 Samuel Rudner', 'Immigration'), ('JHS 55 Samuel Rudner', 'Liquor'), ('JHS 55 Samuel Rudner', 'Lawyer'), ('JHS 55 Samuel Rudner', 'Jewish'), ('Rosenthal, Minerva', 'Immigration'), ('Rosenthal, Minerva', 'Family'), ('Rosenthal, Minerva', 'Business'), ('Rosenthal, Minerva', 'Jewish'), ('Joe & Ida Klatzkin', 'Philadelphia'), ('Joe & Ida Klatzkin', 'Immigrant'), ('Joe & Ida Klatzkin', 'Europe'), ('Joe & Ida Klatzkin', 'Ewing'), ('Dr. Paul Loser', 'Development'), ('Dr. Paul Loser', 'Improve'), ('Dr. Paul Loser', 'School'), ('Dr. Paul Loser', 'Youth');


INSERT INTO CAN_SUGGEST_EDITS (File_Name, User_ID, Suggestion) VALUES('Joe & Ida Klatzkin', '100000', 'Line 42 should be changed');

INSERT INTO CAN_SUGGEST_EDITS (File_Name, User_ID, Suggestion) VALUES('Rosenthal, Minerva', '100001', 'I heard this instead of that');

INSERT INTO CAN_SUGGEST_EDITS (File_Name, User_ID, Suggestion) VALUES('Dr. Paul Loser', '100002', 'A cool suggestion');

