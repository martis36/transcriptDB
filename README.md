# Audio-Transcript Database Implementation

CSC 315-01 - Database Systems  
Group 3  
Aly Maahs, Jared Schmidt, Kyla Ramos, Lalima Bhola, Summer Martin  
Spring 2021

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

- Download the contents of our repo. Within the file CAB DOCS is the file Database Documents where you will find the needed files.
- With psql installed, run these commands to change your user permissions to super user:
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
-	install pyscopg2
- 		pip3 install psycopg2-binary
- install flask
- 		pip3 install flask

- logout, then login again to inherit new shell environment

- then browse to http://127.0.0.1:5000/

To drop the database. Run the command  
`\i drop.sql`  
in your psql database to drop all the views and tables. Enter  
`\q`  
to exit your database and enter  
`dropdb TrentonianaDB`  
to drop the entire database.

### Usage
Wip

### Credits
Authored by Aly Maahs, Jared Schmidt, Kyla Ramos, Lalima Bhola, Summer Martin
