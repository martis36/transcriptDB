# Audio-Transcript Database Implementation

CSC 315-01 - Database Systems  
Group 3  
Aly Maahs, [Jared Schmidt](https://github.com/schmij12), [Summer Martin](https://github.com/martis36), [Kyla Ramos](https://github.com/kyla0509), [Lalima Bhola](https://github.com/lalimabhola)   
Spring 2021

![TrentonianaTranscripts Logo](https://raw.githubusercontent.com/TCNJ-degoodj/stage-v-group-3/main/Code/static/img/logo2.png?token=ANWWE2OPVOLY2XR255MW5MDATBK2Q)

### Please see Installation Instructions blow, Installation Instructions document, or the Stage 5a wiki page before attempting to run the database files. 
File paths in some documents may need to be changed.

## Overview
The Audio & Visual section of the Trentoniana website is currently a work in progress, without a user friendly way to acccess transcripts. It is hard to navigate, with a lack of identifying labels and tags to help a user sort through the files, and is overall not intuitive to use. Our project aims to solve this by providing a more efficient and user friendly system for searching and finding audio files on the topics the user is looking for. 

## Table of Contents
- [Audio-Transcript Database Implementation](#audio-transcript-database-implementation)
  * [Overview](#overview)
  * [Our Objective](#our-objective)
  * [Project Description](#project-description)
  * [Installation](#installation)
  * [Usage](#usage)
  * [Credits](#credits)
  * [License](#license)

### Our Objective
The objective of our project is to create and provide a more efficient and user friendly system for searching and finding audio files on the topics the user is looking for. It is also our goal to combine the audio field and the transcripts so they are both accessible to the public and have the ability to view the transcript that corresponds to the audio file while the audio is playing. We want to provide a user friendly interface for searching, and viewing these files. Providing an straightforward way to interact with these files and a system that would allow for public users to submit new files to be transcribed would encourage interaction between the user and those behind the scenes to collaborate and improve upon existing systems. Better user interaction makes the user feel like their suggestions are valued and their interaction with our system is important. We also want those with higher access to the database to be able to improve and make changes, like adding relevant tags, information and new files, to the system more easily.

### Project Description
The audio-transcript files would be sorted and arranged in a neat, elegant user friendly user interface and would be tagged or labeled with topics, names, dates, and other relevant information so they would be able to be searched for more easily, made easy through tagging the files with relevant information. There would be a search bar at the top of the page so users could easily search for their desired topic or a specific year. If selected, the user would be taken to a different page where they could listen to the audio file and have the option to view the transcript. When viewing the transcript, the user would see the entire transcript at once, maybe with the current part highlighted. On the main page there would be a link to the transcript for each audio file in case the user would rather only view the transcript. There would be some feature on the main page which would be a submission box for new audio files, records, or suggestions. For example, if someone found an error in the transcript or wanted to make a suggestion for improvement or a new submission to be transcribed.

### Installation

- Download the contents of our repo. Within the file Code is where you will find the needed files it is best to move these files into your main Documents folder on your local machine.
- With psql installed, run these commands in the terminal to change your user permissions to super user:
-		sudo -u postgres psql
- 		alter role <your username> superuser
This allows you to use COPY in the CopyCSV.sql file.
- In the CopyCSV file, you may need to change the path specified for the FROM command. Also, in the run.sh file, you may need to change the path to each .sql file.
- Once your permissions and paths are set, create your database by typing the following commands:
-		chmod +x run.sh
- 		./run.sh
This is a script that completes the tasks of creating tables, as well as populating them with data. The script leaves you within the psql database and from there, you are able to begin using psql queries to do whatever you may need to do with the data!

To run and access the web interface, run the following commands
-		sudo apt update
- 		sudo apt install python3-pip
- install pyscopg2
- 		pip3 install psycopg2-binary
- install flask
- 		pip3 install flask

- logout, then login again to inherit new shell environment

To open the user interface run the following commands

- 		chmod +x run-web.sh
- 		./run-web.sh

- then browse to http://127.0.0.1:5000/

To drop the database. Run the command  
`\i drop.sql`  
in your psql database to drop all the views and tables. Enter  
`\q`  
to exit your database and enter  
`dropdb TrentonianaDB`  
to drop the entire database.

![UIhomePage](https://github.com/TCNJ-degoodj/stage-v-group-3/blob/main/Code/static/img/homepage.png)

### Usage
Use the navigation menu on the website to access our different pages.  
* Home Page -> Contains some brief information about the purpose of the website.
* About Page -> Contains information about our group, and what we have done with our project.
* Suggestion Page -> A page where a user can fill out a form to send any suggestion in.
* A link to Trentoniana's main website
* Search Page -> A page with simple to use toggleable filters to search for any information. PSQL is being used in the back end, but the front end hides that from a regular user.
* Advanced Search Page -> A page where a user with knowledge of PSQL can search for any information using PSQL commands in a textbox search field.
* Main Transcript page -> A page that holds links to every transcript's specific webpage in the database.
* Transcript Page -> Each transcript has been given it's own page as well, that contains the links to the audio file associated with it and has the transcription of the audio written on the page so a user can follow along while they listen.
* Comment Page -> A page where a user can fill out a form to comment on any specific transcript.
* Sign In Page -> Used for an admin or moderator to sign in and access special privileges.
* Admin Page -> A page dedicated with tools for an admin of the DB to use.
* Moderator Page -> A page dedicated with tools for a moderator of the DB to use.

### Credits
Authored by Aly Maahs, Jared Schmidt, Summer Martin, Kyla Ramos, Lalima Bhola
