#! /usr/bin/python3

# app.py created using base code from Professor DeGood. Additions primarily added by Summer Martin and Jared Schmidt.

# Please see below for maintenence information

"""
ONE-TIME SETUP

# set the postgreSQL password for user 'lion'
sudo -u postgres psql
    ALTER USER lion PASSWORD 'lion';
    \q

# install pip for Python 3
sudo apt update
sudo apt install python3-pip

# install psycopg2
pip3 install psycopg2-binary

# install flask
pip3 install flask

# logout, then login again to inherit new shell environment

# usage
export FLASK_APP=app.py 
flask run

# then browse to http://127.0.0.1:5000/

Purpose:
Connects to the TrentonianaDB database

For psycopg documentation:
https://www.psycopg.org/

This example code is derived from:
https://www.postgresqltutorial.com/postgresql-python/
https://scoutapm.com/blog/python-flask-tutorial-getting-started-with-flask
https://www.geeksforgeeks.org/python-using-for-loop-in-flask/
"""

import psycopg2
from config import config
from flask import Flask, render_template, request, url_for
 
def connect(query):
    """ Connect to the PostgreSQL database server """
    conn = None
    
    # substrings are used to test what type of query is being entered. In this case we only want select-from queries
    substring = "SELECT"
    substring2 = "FROM"
    fullstring = query
    
    # if the query does not have SELECT or FROM in it, then display the error page    
    if substring2 not in fullstring or substring2 not in fullstring:
        return render_template('error.html')
    # otherwise connect to the database
    else:        
        try:
            # connect to the PostgreSQL server
            conn = psycopg2.connect(dbname="TrentonianaDB", user="lion", password="lion")
            print('Connected.')
      
            # create a cursor
            cur = conn.cursor()
        
            # execute a query using fetchall()
            cur.execute(query)
            rows = cur.fetchall()

            # close the communication with the PostgreSQL
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')
         # return the query result from fetchall()
        return rows
 
# app.py

app = Flask(__name__)

# connects to the static folder
app.static_folder='static'


# serve form web page
@app.route("/")
def form():
    return render_template('search.html')

# handle form data
@app.route('/form-handler', methods=['POST'])
def handle_data():
    rows = connect(request.form['query'])
    
    # UI has a separte results page for audio file searches
    # substrings help to test if the query results will involve audio files 
    fullstring = str(request.form['query'])
    substring = "Audio_File"
    substring2 = "SELECT"
    substring3 = "FROM"
    substring4 = "DEFINES_CHARACTERISTIC_OF"
    
    # if the query is not a select-from query an  error page is displayed
    if substring2 not in fullstring or substring3 not in fullstring:
        return render_template('error.html')
    # if the query involves audio files the the audio file results are displayed
    elif substring in fullstring or substring4 in fullstring:
        return render_template('audioresults.html', rows=rows)
    # for other queries a regualr results page is displayed
    else:
        return render_template('result.html', rows=rows)
    
# handle suggestion insertion
@app.route('/suggest-edit', methods=['POST'])
def insert_suggestion():
    # this gets the input from the suggetion page to turn it into a query
    userid = request.form['firstname']
    filename = request.form['lastname']
    suggestion = request.form['message']
    
    # connect to the PostgreSQL server
    conn = psycopg2.connect(dbname="TrentonianaDB", user="lion", password="lion")
    print('Connected.')
      
    # create a cursor
    cur = conn.cursor()
    
    #generates the query to be executed
    add_suggestion = "INSERT INTO CAN_SUGGEST_EDITS (File_Name, UserID, Suggestion) VALUES (%s, %s, %s)"
    
    # executes the query in the database, if the entries are within the database constraints then the query is entered into the databse.
    try:
        cur.execute(add_suggestion, (filename, userid, suggestion))
        conn.commit()
    
        return render_template('suggest.html')
    except Exception as e:
        return render_template('suggest.html')
        
    conn.close()
      
# renders pages
@app.route('/index')
def index(): 
    return render_template('index.html')

@app.route('/search')
def search(): 
    return render_template('search.html')

@app.route('/about')
def about(): 
    return render_template('about.html')
    
@app.route('/suggest')
def suggest(): 
    return render_template('suggest.html')
    
@app.route('/transcripts')
def transcripts(): 
    return render_template('transcripts.html')
    
# renders the transcript pages
@app.route('/Loser')
def Loser(): 
    return render_template('transcript/Dr. Paul Loser.html')

@app.route('/Rosenthal')
def Rosenthal(): 
    return render_template('transcript/Rosenthal, Minerva.html')
    
@app.route('/Rudner')
def Rudner(): 
    return render_template('transcript/JHS 55, Samuel Rudner.html')
    
@app.route('/Millner')
def Millner(): 
    return render_template('transcript/Joel Millner.html')

@app.route('/Klatzkin')
def Klatzkin(): 
    return render_template('transcript/Joe & Ida Klatzkin.html')

if __name__ == '__main__':
    app.run(debug = True)
