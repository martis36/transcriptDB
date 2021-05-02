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
from datetime import datetime
 
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



# handle form data
@app.route('/form-handler', methods=['POST'])
def handle_data():
    rows = connect(request.form['query'])
    
    # UI has a separte results page for audio file searches
    # substrings help to test if the query results will involve audio files,
    # will have a proper format or will be attempting to access restricted tables
    full = str(request.form['query'])
    full2 = full.lower()
    sub = "audio_file"
    sub2 = "select"
    sub3 = "from"
    sub4 = "defines_characteristic_of"
    sub5 = "suggest"
    sub6 = "users"
    sub7 = "creator"
    
    # if the query is not a select-from query an  error page is displayed
    if sub2 not in full2 or sub3 not in full2 or sub5 in full2 or sub6 in full2 or sub7 in full2:
        return render_template('error.html')
    # if the query involves audio files the the audio file results are displayed
    elif sub in full2 or sub4 in full2:
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
 
 
 
      
@app.route('/signinform', methods=['POST'])
def signinform():
    user = request.form['userid']
    password = request.form['pass']
    page = "No"
    
    conn = psycopg2.connect(dbname="TrentonianaDB", user="lion", password="lion")
    print('Connected.')
      
    # create a cursor
    cur = conn.cursor()
    
    # set the query to get the password
    isuser = "SELECT password FROM USERS WHERE userid = \'%s\';" % user
    # set the query to get the user type
    istypeuser = "SELECT user_type FROM USERS WHERE userid = \'%s\';" % user
    
    try:
        # run the query to get the password
        cur.execute(isuser)
        rows1 = cur.fetchall()
        # get the password associated with the given user name
        for row in rows1:
            p = row[0]
        
        # run the query to get the user type
        cur.execute(istypeuser)
        rows2 = cur.fetchall()
        # get the user type associated with the given user id
        for row in rows2:
            t = row[0]
        
        # if the password the user entered is correct and the 
        # user type is Admin pull up the Admin page
            
        if p == password and t == "Admin":
            return render_template('adminpage.html')
            cur.close()
        # if the password the user entered is correct and the 
        # user type is Moderator pull up the Admin page    
        elif p == password and t == "Moderator":
            return render_template('moderatorpage.html')
            cur.close()
        # if the user type is not Admin or Moderator, the password is 
        # incorrect or the userid doesn't exsist the pull up the error page
        else :
            # close the communication with the PostgreSQL
            cur.close()
            return render_template('sierror.html')
    except Exception as e:
        return  render_template('sierror.html')
        
    conn.close()    
        



@app.route('/view', methods=['POST'])
def view():
    file = request.form['view']
    
    conn = psycopg2.connect(dbname="TrentonianaDB", user="lion", password="lion")
    print('Connected.')
      
    # create a cursor
    cur = conn.cursor()
    
    if file == "loser":
        #sets the query to be executed
        add_view = "UPDATE Audio_File SET view_count = view_count + 1 WHERE file_name = 'Dr. Paul Loser';"
        page = render_template('transcripts/Dr. Paul Loser.html')
    elif file == "rose":
        add_view = "UPDATE Audio_File SET view_count = view_count + 1 WHERE file_name = 'Rosenthal, Minerva';"
        page = render_template('transcripts/Rosenthal, Minerva.html')
    
    elif file == "sam":
        add_view = "UPDATE Audio_File SET view_count = view_count + 1 WHERE file_name = 'JHS 55 Samuel Rudner';"
        page = render_template('transcripts/JHS 55, Samuel Rudner.html')
    
    elif file == "joel":
        add_view = "UPDATE Audio_File SET view_count = view_count + 1 WHERE file_name = 'Joel Millner';"
        page = render_template('transcripts/Joel Millner.html')
    
    elif file == "joeida": 
        add_view = "UPDATE Audio_File SET view_count = view_count + 1 WHERE file_name = 'Joe & Ida Klatzkin';"
        page = render_template('transcripts/Joe and Ida Klatzkin.html')
    
    else:
        add_view = "NULL"
    
    # executes the update query in the database, if the entries are within the database constraints then the update is entered into the databse.
    try:
        cur.execute(add_view)
        conn.commit()
        
        return page
    except Exception as e:
        return page
        
    conn.close()
 
 
 
    
@app.route('/like', methods=['POST'])
def like():
    file = request.form['like']

    conn = psycopg2.connect(dbname="TrentonianaDB", user="lion", password="lion")
    print('Connected.')
      
    # create a cursor
    cur = conn.cursor()
    
    if file == "loser":
        #sets the query to be executed
        add_like = "UPDATE Audio_File SET like_count = like_count + 1 WHERE file_name = 'Dr. Paul Loser';"
        page = render_template('transcripts/Dr. Paul Loser.html')
    
    elif file == "rose":
        add_like = "UPDATE Audio_File SET like_count = like_count + 1 WHERE file_name = 'Rosenthal, Minerva';"
        page = render_template('transcripts/Rosenthal, Minerva.html')
    
    elif file == "sam":
        add_like = "UPDATE Audio_File SET like_count = like_count + 1 WHERE file_name = 'JHS 55 Samuel Rudner';"
        page = render_template('transcripts/JHS 55, Samuel Rudner.html')
    
    elif file == "joel":
        add_like = "UPDATE Audio_File SET like_count = like_count + 1 WHERE file_name = 'Joel Millner';"
        page = render_template('transcripts/Joel Millner.html')
    
    elif file == "joeida": 
        add_like = "UPDATE Audio_File SET like_count = like_count + 1 WHERE file_name = 'Joe & Ida Klatzkin';"
        page = render_template('transcripts/Joe and Ida Klatzkin.html')
    
    else:
        add_like = "NULL"

    
    # executes the update query in the database, if the entries are within the database constraints then the update is entered into the databse.
    try:
        cur.execute(add_like)
        conn.commit()
        
        return page
    except Exception as e:
        return page
        
    conn.close()
 
 
 
    
@app.route('/make-comment', methods=['POST'])
def insert_comment():
    # this gets the input from the suggetion page to turn it into a query
    user = request.form['uname']
    file = request.form['filename']
    comment = request.form['comment']
    today = datetime.date(datetime.now())
    
    # connect to the PostgreSQL server
    conn = psycopg2.connect(dbname="TrentonianaDB", user="lion", password="lion")
    print('Connected.')
      
    # create a cursor
    cur = conn.cursor()
    
    #generates the query to be executed
    add_comment = "INSERT INTO COMMENT (User_Comment, Date_Created, UserID, File_Name) VALUES (%s, %s, %s, %s)"
    
    # executes the query in the database, if the entries are within the database constraints then the query is entered into the databse.
    try:
        cur.execute(add_comment, (comment, today, user, file))
        conn.commit()
    
        return render_template('comment.html')
    except Exception as e:
        return render_template('comment.html')
 
 
 
 
        
# takes input from the regular search page and executes them as queries
@app.route('/make-search', methods=['POST'])
def makesearch():
    value = str(request.form['searchby'])
    
    # connect to the PostgreSQL server
    conn = psycopg2.connect(dbname="TrentonianaDB", user="lion", password="lion")
    print('Connected.')
      
    # create a cursor
    cur = conn.cursor()
    
    #search all audio files
    if value == "all":
        search = "SELECT file_name, af_link, transcript_link, date_originated FROM AUDIO_FILE;"
    
        # executes the query in the database
        try:
            cur.execute(search)
            rows = cur.fetchall()

            # close the communication with the PostgreSQL
            cur.close()
                
            return render_template('audioresults.html', rows=rows)   
        except Exception as e:
            return render_template('error.html')
        
        conn.close()
    
    #search for a specific audio file
    elif value == "spec":
        fname = request.form['entry1']
        search = "SELECT file_name, af_link, transcript_link, date_originated FROM AUDIO_FILE WHERE file_name ILIKE \'%%%s%%\';" % fname
           
        # executes the query in the database
        try:
            cur.execute(search)
            
            rows = cur.fetchall()

            # close the communication with the PostgreSQL
            cur.close()
                
            return render_template('audioresults.html', rows=rows)   
        except Exception as e:
            return render_template('error.html')
        
        conn.close()
    
    #searches for a file with a specific year
    elif value == "year":
        year1 = request.form['date1']
        year2 = request.form['date2']
        search = "SELECT file_name, af_link, transcript_link, date_originated FROM AUDIO_FILE WHERE (date_originated > %s) AND (date_originated < %s);"
        
        # executes the query in the database
        try:
            cur.execute(search, (year1, year2))
            
            rows = cur.fetchall()

            # close the communication with the PostgreSQL
            cur.close()
                
            return render_template('audioresults.html', rows=rows)   
        except Exception as e:
            return render_template('error.html')
        
        conn.close()
    
    #searches for all tags    
    elif value == "tags":
        search = "SELECT * FROM Tag"
    
        # executes the query in the database
        try:
            cur.execute(search)
            rows = cur.fetchall()

            # close the communication with the PostgreSQL
            cur.close()
                
            return render_template('result.html', rows=rows)  
        except Exception as e:
            return render_template('error.html')
        
        conn.close()
        
    #searches for files associated with a specific tag
    elif value == "tag":
        tname = request.form['entry2']
        search = "SELECT file_name, af_link, transcript_link, date_originated FROM AUDIO_FILE_TAGS WHERE tag_name = \'%s\';" % tname
           
        # executes the query in the database
        try:
            cur.execute(search)
            
            rows = cur.fetchall()

            # close the communication with the PostgreSQL
            cur.close()
                
            return render_template('audioresults.html', rows=rows)   
        except Exception as e:
            return render_template('error.html')
        
        conn.close()
        
    #searches for files with a certain like count
    elif value == "like":
        ldirct = str(request.form['range'])
        lnum = request.form['number']
 

        if ldirct == "less":
            search = "SELECT file_name, like_count, af_link FROM Audio_File WHERE like_count < %s ORDER BY like_count DESC;" % lnum
        
        else:
            search = "SELECT file_name, like_count, af_link FROM Audio_File WHERE like_count > %s ORDER BY like_count DESC;" % lnum        
        
        # executes the query in the database
        try:
            cur.execute(search)
            
            rows = cur.fetchall()

            # close the communication with the PostgreSQL
            cur.close()
                
            return render_template('audioresults.html', rows=rows)   
        except Exception as e:
            return render_template('error.html')
        
        conn.close()
        
    elif value == "view":
        vdirct = request.form['range']
        vnum = request.form['number']
        if vdirct == "less":
            search = "SELECT file_name, view_count, af_link FROM Audio_File WHERE view_count < %s ORDER BY view_count DESC;" % vnum
            
        else:
            search = "SELECT file_name, view_count, af_link FROM Audio_File WHERE view_count > %s ORDER BY view_count DESC;" % vnum
                  
        # executes the query in the database
        try:
            cur.execute(search)
            
            rows = cur.fetchall()

            # close the communication with the PostgreSQL
            cur.close()
                
            return render_template('audioresults.html', rows=rows)   
        except Exception as e:
            return render_template('error.html')
        
        conn.close()    
            
    #searchs for all comments
    elif value == "comments":
        search = "SELECT file_name, user_comment, date_created, userid FROM Comment;"
    
        # executes the query in the database
        try:
            cur.execute(search)
            rows = cur.fetchall()

            # close the communication with the PostgreSQL
            cur.close()
                
            return render_template('result.html', rows=rows)  
        except Exception as e:
            return render_template('error.html')
        
        conn.close()
        
    #searches for all comments relating to a specific file
    elif value == "filecomment":
        com = request.form['entry3']
        search = "SELECT file_name, user_comment, date_created, userid, af_link FROM audio_file_comments WHERE file_name ILIKE \'%%%s%%\';" % com
           
        # executes the query in the database
        try:
            cur.execute(search)
            
            rows = cur.fetchall()

            # close the communication with the PostgreSQL
            cur.close()
                
            return render_template('audioresults.html', rows=rows)   
        except Exception as e:
            return render_template('error.html')
        
        conn.close()
                        
    else:
        return render_template('error.html')




@app.route("/adminpg", methods=['POST'])
def adminpg():
    # doesadmin want to search, update, insert or delete
    value = request.form['querytype']
    
    # connect to the PostgreSQL server
    conn = psycopg2.connect(dbname="TrentonianaDB", user="lion", password="lion")

    # create a cursor
    cur = conn.cursor()
    
    if value == "see":
        # what table does admin want to see
        file = request.form['xn0']

        search = "SELECT * FROM %s;" % file
        
        # executes the query in the database
        try:
            cur.execute(search)

            rows = cur.fetchall()

            # close the communication with the PostgreSQL
            cur.close()
                
            return render_template('adminresults.html', rows=rows)   
        except Exception as e:
            return render_template('adminpage.html')
        
        conn.close()
        
    elif value == "insert":
        #what table does the admin want to insert in
        value2 = request.form['intype']
        # if they want to insert a file
        if value2 == "newfile":
            #get values admin entered
            file = request.form['xn1']  # get name of new file
            link1 = request.form['xl1'] # get audio link
            link2 = request.form['xl2'] # get transcript link
            date = request.form['xda']  # get date origiated
            
            search = "INSERT INTO Audio_File(file_name, af_link, transcript_link, date_originated) VALUES (%s, %s, %s, %s);"
            
            #insert into database
            try:
                cur.execute(search, (file, link1, link2, date))

                conn.commit()
                # close the communication with the PostgreSQL
                cur.close()
                
                return render_template('adminpage.html')   
            except Exception as e:

                return render_template('adminpage.html')
        
            conn.close()

            
        #if admin wants to enter a new tag
        elif value2 == "newtag":
            #get tag admin entered
            tag = request.form['xt1']
            search = "INSERT INTO Tag(tag_name) VALUES (\'%s\');" % tag
            
            # insert into databse
            try:
                cur.execute(search)

                conn.commit()
                # close the communication with the PostgreSQL
                cur.close()
                
                return render_template('adminpage.html')   
            except Exception as e:
                return render_template('adminpage.html')
        
            conn.close()
            
        # if admin wants to assign a new tag to a file
        elif value2 == "newpair":
            # get the file name and tag
            file = request.form['xn2']
            tag = request.form['xt2']
            
            search = "INSERT INTO DEFINES_CHARACTERISTIC_OF (file_name, tag_name) VALUES (%s, %s);"

            # insert into database
            try:
                cur.execute(search, (file, tag))

                conn.commit()

                # close the communication with the PostgreSQL
                cur.close()
                
                return render_template('adminpage.html')   
            except Exception as e:
                return render_template('adminpage.html')
        
            conn.close()
            
        # if admin wants to enter a new user
        elif value2 == "newuser":
            #get password, user type and admin userid
            password = request.form['xp1']
            types = request.form['xty1']
            create = request.form['xu1']
            
            search = "INSERT INTO Users (password, user_type, user_creator_ID) VALUES (%s, %s, %s);"
            
            # insert into database
            try:
                cur.execute(search, (password, types, create))

                conn.commit()

                # close the communication with the PostgreSQL
                cur.close()
                
                return render_template('adminpage.html')   
            except Exception as e:
                return render_template('adminpage.html')
        
            conn.close()
            
        else:
            return render_template('adminpage.html')
            
    # if admin wants to delete a tuple
    elif value == "remove":
        # get table they want to delete from
        value3 = request.form['deltype']
        #if they want to remove a file
        if value3 == "rmfile":
            #get file name admin entered
            file = request.form['xn3']
            delt = "DELETE FROM AUDIO_FILE WHERE File_Name = \'%s\';" % file
            # delete from databse
            try:
                cur.execute(delt)

                conn.commit()

                # close the communication with the PostgreSQL
                cur.close()
                
                return render_template('adminpage.html')   
            except Exception as e:
                return render_template('adminpage.html')
        
            conn.close()
            
        # if they want to delete a comment
        elif value3 == "rmcomment":
            # get comment id admin entered
            com = request.form['xc1']
            delt = "DELETE FROM COMMENT WHERE Comment_ID = '%s';" % com
            # delete from databse
            try:
                cur.execute(delt)

                conn.commit()

                # close the communication with the PostgreSQL
                cur.close()
                
                return render_template('adminpage.html')   
            except Exception as e:
                return render_template('adminpage.html')
        
            conn.close()
            
        # if they want to delete a suggestion
        elif value3 == "rmsug":
            # get suggestion id admin entered
            sug = request.form['xs1']
            delt = "DELETE FROM CAN_SUGGEST_EDITS WHERE Suggestion_ID = \'%s\';" % sug
            try:
                cur.execute(delt)

                conn.commit()

                # close the communication with the PostgreSQL
                cur.close()
                
                return render_template('adminpage.html')   
            except Exception as e:
                return render_template('adminpage.html')
        
            conn.close()
            
        # if they want to remove a tag
        elif value3 == "rmtag":
            # get the tag name admin entered
            tag = request.form['xt3']
            delt = "DELETE FROM TAG WHERE Tag_Name = \'%s\';" % tag
            # delete from databse
            try:
                cur.execute(delt)

                conn.commit()

                # close the communication with the PostgreSQL
                cur.close()
                
                return render_template('adminpage.html')   
            except Exception as e:
                return render_template('adminpage.html')
        
            conn.close()
            
        # if they want to remove a user
        elif value3 == "rmuser":
            # get the user id admin entered
            uid = request.form['xu2']
            delt = "DELETE FROM USERS WHERE UserID = \'%s\';" % uid
            # delete from database
            try:
                cur.execute(delt)

                conn.commit()

                # close the communication with the PostgreSQL
                cur.close()
                
                return render_template('adminpage.html')   
            except Exception as e:
                return render_template('adminpage.html')
        
            conn.close()
            
        else:
            return render_template('adminpage.html')
        
    # if admin wants to update a value
    elif value == "update":
        # does admin want to update a user or an audio file
        value4 = request.form['tabtype']
        # if admin wants to update a user
        if value4 == "changeu":
            # get the user id and do they want to change the password or the user type
            user = request.form['xu3']
            value5 = request.form['utype']
            
            # if they want to chnage the users password
            if value5 == "changeup":
                # get the new password
                password = request.form['xu4']
                update = "UPDATE Users SET password = %s WHERE userid = %s;"
                
                # update in database
                try:
                    print("trying")
                    cur.execute(update, (password, user))
                    print("yes")

                    conn.commit()

                    # close the communication with the PostgreSQL
                    cur.close()
                
                    return render_template('adminpage.html')   
                except Exception as e:
                    return render_template('adminpage.html')
        
                conn.close()
            
            # if they want ot chnage the user type    
            elif value5 == "changety":
                # get the new type
                types = request.form['xu5']
                update = "UPDATE Users SET user_type = %s WHERE userid = %s;"
                # update in database
                try:
                    cur.execute(update, (types, user))

                    conn.commit()

                    # close the communication with the PostgreSQL
                    cur.close()
                
                    return render_template('adminpage.html')   
                except Exception as e:
                    return render_template('adminpage.html')
        
                conn.close()
                            
        # if they want to change and audio file
        elif value4 == "changeaf":
            # get which file and which attribute they want to change
            file = request.form['xn4']
            types = request.form['ftype']
            
            # if they want to chnage the name
            if types == "changefn":
                # get the new name
                name = request.form['xf5']
                update = "UPDATE Audio_File SET file_name = %s WHERE file_name = %s;"
                # update in the database
                try:
                    cur.execute(update, (name, file))

                    conn.commit()

                    # close the communication with the PostgreSQL
                    cur.close()
                
                    return render_template('adminpage.html')   
                except Exception as e:
                    return render_template('adminpage.html')
        
                conn.close()
            # if they want to chnage an audio file link
            elif types == "changeal":
                # get the new link
                link = request.form['xa1']
                update = "UPDATE Audio_File SET af_link = %s WHERE file_name = %s;"
                # update into database
                try:
                    cur.execute(update, (link, file))

                    conn.commit()

                    # close the communication with the PostgreSQL
                    cur.close()
                
                    return render_template('adminpage.html')   
                except Exception as e:
                    return render_template('adminpage.html')
        
                conn.close()
                # if they want to change a transcript link
            elif types == "changetl":
                # get the new link
                link = request.form['xa2']
                update = "UPDATE Audio_File SET transcript_link = %s WHERE file_name = %s;"
                #update into databse
                try:
                    cur.execute(update, (link, file))

                    conn.commit()

                    # close the communication with the PostgreSQL
                    cur.close()
                
                    return render_template('adminpage.html')   
                except Exception as e:
                    return render_template('adminpage.html')
        
                conn.close()
            # if they want to chnage th edate originated
            elif types == "changeda":
                # get the new date
                date = request.form['xda2']
                update = "UPDATE Audio_File SET date_originated = %s WHERE file_name = %s;"
                # update in databse
                try:
                    cur.execute(update, (date, file))

                    conn.commit()

                    # close the communication with the PostgreSQL
                    cur.close()
                
                    return render_template('adminpage.html')   
                except Exception as e:
                    return render_template('adminpage.html')
        
                conn.close()
            else:
                return render_template('adminpage.html')
        else:
            return render_template('adminpage.html')
    else:
        return render_template('adminpage.html')
    
    
    
    
@app.route("/modpage", methods=['POST'])
def modpage():    
    # doesadmin want to search, update, insert or delete
    value = request.form['querytype']
    
    # connect to the PostgreSQL server
    conn = psycopg2.connect(dbname="TrentonianaDB", user="lion", password="lion")

    # create a cursor
    cur = conn.cursor()
    
    if value == "see":
        # what table does admin want to see
        file = request.form['xn0']

        search = "SELECT * FROM %s;" % file
        
        # executes the query in the database
        try:
            cur.execute(search)

            rows = cur.fetchall()

            # close the communication with the PostgreSQL
            cur.close()
                
            return render_template('adminresults.html', rows=rows)   
        except Exception as e:
            return render_template('moderatorpage.html')
        
        conn.close()
        
    elif value == "insert":
        #what table does the admin want to insert in
        value2 = request.form['intype']
        
        # if they want to insert a tag
        if value2 == "newtag":
            #get tag admin entered
            tag = request.form['xt1']
            search = "INSERT INTO Tag(tag_name) VALUES (\'%s\');" % tag
            
            # insert into databse
            try:
                cur.execute(search)

                conn.commit()
                # close the communication with the PostgreSQL
                cur.close()
                
                return render_template('moderatorpage.html')   
            except Exception as e:
                return render_template('moderatorpage.html')
        
            conn.close()
            
        # if admin wants to assign a new tag to a file
        elif value2 == "newpair":
            # get the file name and tag
            file = request.form['xn2']
            tag = request.form['xt2']
            
            search = "INSERT INTO DEFINES_CHARACTERISTIC_OF (file_name, tag_name) VALUES (%s, %s);"

            # insert into database
            try:
                cur.execute(search, (file, tag))

                conn.commit()

                # close the communication with the PostgreSQL
                cur.close()
                
                return render_template('moderatorpage.html')   
            except Exception as e:
                return render_template('moderatorpage.html')
        
            conn.close()
            
        else:
            return render_template('moderatorpage.html')
            
    # if admin wants to delete a tuple
    elif value == "remove":
        # get table they want to delete from
        value3 = request.form['deltype']
        
        #if they want to remove a comment
        if value3 == "rmcomment":
            # get comment id admin entered
            com = request.form['xc1']
            delt = "DELETE FROM COMMENT WHERE Comment_ID = '%s';" % com
            # delete from databse
            try:
                cur.execute(delt)

                conn.commit()

                # close the communication with the PostgreSQL
                cur.close()
                
                return render_template('moderatorpage.html')   
            except Exception as e:
                return render_template('moderatorpage.html')
        
            conn.close()
            
        # if they want to delete a suggestion
        elif value3 == "rmsug":
            # get suggestion id admin entered
            sug = request.form['xs1']
            delt = "DELETE FROM CAN_SUGGEST_EDITS WHERE Suggestion_ID = \'%s\';" % sug
            try:
                cur.execute(delt)

                conn.commit()

                # close the communication with the PostgreSQL
                cur.close()
                
                return render_template('moderatorpage.html')   
            except Exception as e:
                return render_template('moderatorpage.html')
        
            conn.close()
            
        # if they want to remove a tag
        elif value3 == "rmtag":
            # get the tag name admin entered
            tag = request.form['xt3']
            delt = "DELETE FROM TAG WHERE Tag_Name = \'%s\';" % tag
            # delete from databse
            try:
                cur.execute(delt)

                conn.commit()

                # close the communication with the PostgreSQL
                cur.close()
                
                return render_template('moderatorpage.html')   
            except Exception as e:
                return render_template('moderatorpage.html')
        
            conn.close()
            
        else:
            return render_template('moderatorpage.html')
        
    # if admin wants to update a value
    elif value == "update":
        # does admin want to update a user or an audio file
        value4 = request.form['tabtype']
        # if admin wants to update a user
        if value4 == "changeu":
            # get the user id and do they want to change the password
            user = request.form['xu3']
            value5 = request.form['utype']
            
            # if they want to chnage the users password
            if value5 == "changeup":
                # get the new password
                password = request.form['xu4']
                update = "UPDATE Users SET password = %s WHERE userid = %s;"
                
                # update in database
                try:
                    print("trying")
                    cur.execute(update, (password, user))
                    print("yes")

                    conn.commit()

                    # close the communication with the PostgreSQL
                    cur.close()
                
                    return render_template('moderatorpage.html')   
                except Exception as e:
                    return render_template('moderatorpage.html')
        
                conn.close()
            
            else:
                return render_template('moderatorpage.html')
                            
        # if they want to change and audio file
        elif value4 == "changeaf":
            # get which file and which attribute they want to change
            file = request.form['xn4']
            types = request.form['ftype']
            
            # if they want to chnage the name
            if types == "changefn":
                # get the new name
                name = request.form['xf5']
                update = "UPDATE Audio_File SET file_name = %s WHERE file_name = %s;"
                # update in the database
                try:
                    cur.execute(update, (name, file))

                    conn.commit()

                    # close the communication with the PostgreSQL
                    cur.close()
                
                    return render_template('moderatorpage.html')   
                except Exception as e:
                    return render_template('moderatorpage.html')
        
                conn.close()
            # if they want to chnage an audio file link
            elif types == "changeal":
                # get the new link
                link = request.form['xa1']
                update = "UPDATE Audio_File SET af_link = %s WHERE file_name = %s;"
                # update into database
                try:
                    cur.execute(update, (link, file))

                    conn.commit()

                    # close the communication with the PostgreSQL
                    cur.close()
                
                    return render_template('moderatorpage.html')   
                except Exception as e:
                    return render_template('moderatorpage.html')
        
                conn.close()
                # if they want to change a transcript link
            elif types == "changetl":
                # get the new link
                link = request.form['xa2']
                update = "UPDATE Audio_File SET transcript_link = %s WHERE file_name = %s;"
                #update into databse
                try:
                    cur.execute(update, (link, file))

                    conn.commit()

                    # close the communication with the PostgreSQL
                    cur.close()
                
                    return render_template('moderatorpage.html')   
                except Exception as e:
                    return render_template('moderatorpage.html')
        
                conn.close()
            # if they want to chnage th edate originated
            elif types == "changeda":
                # get the new date
                date = request.form['xda2']
                update = "UPDATE Audio_File SET date_originated = %s WHERE file_name = %s;"
                # update in databse
                try:
                    cur.execute(update, (date, file))

                    conn.commit()

                    # close the communication with the PostgreSQL
                    cur.close()
                
                    return render_template('moderatorpage.html')   
                except Exception as e:
                    return render_template('moderatorpage.html')
        
                conn.close()
            else:
                return render_template('moderatorpage.html')
        else:
            return render_template('moderatorpage.html')
    else:
        return render_template('moderatorpage.html')



# serve form web page
@app.route("/")
def form():
    return render_template('index.html')
    
# renders pages
@app.route("/admin")
def admin():
    return render_template('adminpage.html')

@app.route("/moderator")
def moderator():
    return render_template('moderatorpage.html')

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
    
@app.route('/regsearch')
def regsearch():
    return render_template('regsearch.html')
    
@app.route('/comment')
def comment():
    return render_template('comment.html')
    
@app.route('/signin')
def signin():
    return render_template('signin.html')
    
# renders the transcript pages
@app.route('/Loser')
def Loser(): 
    return render_template('transcripts/Dr. Paul Loser.html')

@app.route('/Rosenthal')
def Rosenthal(): 
    return render_template('transcripts/Rosenthal, Minerva.html')
    
@app.route('/Rudner')
def Rudner(): 
    return render_template('transcripts/JHS 55, Samuel Rudner.html')
    
@app.route('/Millner')
def Millner(): 
    return render_template('transcripts/Joel Millner.html')

@app.route('/Klatzkin')
def Klatzkin(): 
    return render_template('transcripts/Joe and Ida Klatzkin.html')

if __name__ == '__main__':
    app.run(debug = True)
