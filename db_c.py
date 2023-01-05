import cx_Oracle
import tkinter as tk
from tkinter import *

# connecting directly to school database via cx_Oracle
conStr = "user/pass@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(Host=oracle.scs.ryerson.ca)(Port=1521))(CONNECT_DATA=(SID=orcl)))"
conn = cx_Oracle.connect(conStr)
# instantiating database object
cursor = conn.cursor()

# instantiating tkinter
ui = tk.Tk()
ui.geometry("1050x200")
ui.title("Movie Recommendation Database System")


main_label = Label(ui, font=("arial", 50, "bold"), text="Movie Recommendation Database System", bg="Ghost White")
main_label.grid(row=0,column=0,sticky=W)

text_label = Label(ui, font=("arial", 10, "bold"), text="USE THE DROPDOWN MENU ABOVE TO NAVIGATE", bg="Ghost White")
text_label.grid(padx=400,pady=50)


main_menu = Menu(ui)
ui.config(menu=main_menu)


def some_command():
    pass


def query1():
    main_label.grid_forget()
    text_label.grid_forget()
    ui.title("QUERY: Find no. of instances of each movie title associated with user lists and sort them in descending order.")
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(movie_list), movie_id FROM movie_list GROUP BY movie_id ORDER BY COUNT(movie_list) DESC")
    col = Label(ui, width=10, text='movie_id', borderwidth=2, relief='ridge', anchor='w')
    col.grid(row=0, column=0)
    col = Label(ui, width=10, text='list', borderwidth=2, relief='ridge', anchor='w')
    col.grid(row=0, column=1)

    i = 1
    for list in cursor:
        for j in range(2):
            e = Entry(ui, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, list[j])
        i = i + 1
    cursor.close()


def create_movie_title():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE movie_title ( \
    movie_id NUMBER PRIMARY KEY,\
    movie_name VARCHAR2(30) NOT NULL UNIQUE)")
    create_label = Label(ui, font=("arial", 10, "bold"), text="SUCCESSFULLY CREATED TABLE", bg="Ghost White")
    create_label.grid(padx=400, pady=50)
    text_label.grid(padx=400, pady=50)
    cursor.close()


def create_movie_att():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE movie_att (\
    movie_name VARCHAR2(30) NOT NULL UNIQUE,\
    movie_length NUMBER,\
    release_date DATE,\
    movie_actor VARCHAR2(40) NOT NULL,\
    movie_rating NUMBER NOT NULL)")
    create_label = Label(ui, font=("arial", 10, "bold"), text="SUCCESSFULLY CREATED TABLE", bg="Ghost White")
    create_label.grid(padx=400, pady=50)
    cursor.close()


def create_movie_sequel():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE movie_sequel (\
    movie_name REFERENCES movie_title(movie_name),\
    sequel_name VARCHAR2(30) NOT NULL)")
    create_label = Label(ui, font=("arial", 10, "bold"), text="SUCCESSFULLY CREATED TABLE", bg="Ghost White")
    create_label.grid(padx=400, pady=50)
    cursor.close()


def create_sequel_info():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE sequel_info (\
    next_sequel_id NUMBER PRIMARY KEY,\
    movie_id REFERENCES movie_title(movie_id),\
    movie_name REFERENCES movie_title(movie_name))")
    create_label = Label(ui, font=("arial", 10, "bold"), text="SUCCESSFULLY CREATED TABLE", bg="Ghost White")
    create_label.grid(padx=400, pady=50)
    cursor.close()


def create_movie_rating():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE movie_rating (\
    movie_id REFERENCES movie_title(movie_id),\
    rating_id NUMBER PRIMARY KEY,\
    movie_score NUMBER DEFAULT 0,\
    box_office_gross NUMBER, \
    movie_popularity NUMBER)")
    create_label = Label(ui, font=("arial", 10, "bold"), text="SUCCESSFULLY CREATED TABLE", bg="Ghost White")
    create_label.grid(padx=400, pady=50)
    cursor.close()


def create_user_login():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE user_login( \
    username VARCHAR(100) PRIMARY KEY NOT NULL, \
    password_log VARCHAR(100) NOT NULL)")
    create_label = Label(ui, font=("arial", 10, "bold"), text="SUCCESSFULLY CREATED TABLE", bg="Ghost White")
    create_label.grid(padx=400, pady=50)
    cursor.close()


def create_user_info():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE user_info(\
    username REFERENCES user_login(username),\
    age NUMBER NOT NULL)")
    create_label = Label(ui, font=("arial", 10, "bold"), text="SUCCESSFULLY CREATED TABLE", bg="Ghost White")
    create_label.grid(padx=400, pady=50)
    cursor.close()


def create_user_list():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE user_list(\
    username REFERENCES user_login(username),\
    movie_list VARCHAR(100) PRIMARY KEY)")
    create_label = Label(ui, font=("arial", 10, "bold"), text="SUCCESSFULLY CREATED TABLE", bg="Ghost White")
    create_label.grid(padx=400, pady=50)
    cursor.close()


def create_movie_list():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE movie_list(\
    movie_id REFERENCES movie_title(movie_id),\
    movie_list REFERENCES user_list(movie_list))")
    create_label = Label(ui, font=("arial", 10, "bold"), text="SUCCESSFULLY CREATED TABLE", bg="Ghost White")
    create_label.grid(padx=400, pady=50)
    cursor.close()


def drop_movie_title():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("DROP TABLE movie_title")
    drop_label = Label(ui, font=("arial", 10, "bold"), text="SUCCESSFULLY DROPPED TABLE", bg="Ghost White")
    drop_label.grid(padx=400, pady=50)
    cursor.close()


def drop_movie_att():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("DROP TABLE movie_att")
    drop_label = Label(ui, font=("arial", 10, "bold"), text="SUCCESSFULLY DROPPED TABLE", bg="Ghost White")
    drop_label.grid(padx=400, pady=50)
    cursor.close()


def drop_movie_sequel():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("DROP TABLE movie_sequel")
    drop_label = Label(ui, font=("arial", 10, "bold"), text="SUCCESSFULLY DROPPED TABLE", bg="Ghost White")
    drop_label.grid(padx=400, pady=50)
    cursor.close()


def drop_sequel_info():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("DROP TABLE sequel_info")
    drop_label = Label(ui, font=("arial", 10, "bold"), text="SUCCESSFULLY DROPPED TABLE", bg="Ghost White")
    drop_label.grid(padx=400, pady=50)
    cursor.close()


def drop_movie_rating():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("DROP TABLE movie_rating")
    drop_label = Label(ui, font=("arial", 10, "bold"), text="SUCCESSFULLY DROPPED TABLE", bg="Ghost White")
    drop_label.grid(padx=400, pady=50)
    cursor.close()


def drop_user_login():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("DROP TABLE user_login")
    drop_label = Label(ui, font=("arial", 10, "bold"), text="SUCCESSFULLY DROPPED TABLE", bg="Ghost White")
    drop_label.grid(padx=400, pady=50)
    cursor.close()


def drop_user_info():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("DROP TABLE user_info")
    drop_label = Label(ui, font=("arial", 10, "bold"), text="SUCCESSFULLY DROPPED TABLE", bg="Ghost White")
    drop_label.grid(padx=400, pady=50)
    cursor.close()


def drop_user_list():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("DROP TABLE user_list")
    drop_label = Label(ui, font=("arial", 10, "bold"), text="SUCCESSFULLY DROPPED TABLE", bg="Ghost White")
    drop_label.grid(padx=400, pady=50)
    cursor.close()


def drop_movie_list():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute("DROP TABLE movie_list")
    drop_label = Label(ui, font=("arial", 10, "bold"), text="SUCCESSFULLY DROPPED TABLE", bg="Ghost White")
    drop_label.grid(padx=400, pady=50)
    cursor.close()


def display_movie_title():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute('select * from movie_title')
    col = Label(ui, width=10, text='movie_id', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=0)
    col = Label(ui, width=10, text='movie_name', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=1)

    i = 1
    for movie in cursor:
        for j in range(2):
            e = Entry(ui, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, movie[j])
        i = i+1
    cursor.close()


def display_movie_att():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute('select * from movie_att')
    col = Label(ui, width=10, text='movie_name', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=0)
    col = Label(ui, width=10, text='movie_length', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=1)
    col = Label(ui, width=10, text='release_date', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=2)
    col = Label(ui, width=10, text='movie_actor', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=3)
    col = Label(ui, width=10, text='movie_rating', borderwidth=2, relief='ridge', anchor='w')
    col.grid(row=0, column=4)

    i = 1
    for movie in cursor:
        for j in range(len(movie)):
            e = Entry(ui, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, movie[j])
        i = i+1
    cursor.close()


def display_movie_sequel():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute('select * from movie_sequel')
    col = Label(ui, width=10, text='movie_name', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=0)
    col = Label(ui, width=10, text='sequel_name', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0,column=1)
    i = 1
    for movie in cursor:
        for j in range(len(movie)):
            e = Entry(ui, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, movie[j])
        i = i+1
    cursor.close()


def display_sequel_info():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute('select * from sequel_info')
    col = Label(ui, width=10, text='next_sequel.id', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=0)
    col = Label(ui, width=10, text='movie_id', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=1)
    col = Label(ui, width=10, text='movie_name', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=2)
    i = 1
    for movie in cursor:
        for j in range(len(movie)):
            e = Entry(ui, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, movie[j])
        i = i+1
    cursor.close()


def display_movie_rating():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute('select * from movie_rating')
    col = Label(ui, width=10, text='movie_id', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=0)
    col = Label(ui, width=10, text='rating_id', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=1)
    col = Label(ui, width=10, text='movie_score', borderwidth=2, relief='ridge', anchor='w')
    col.grid(row=0, column=2)
    col = Label(ui, width=10, text='box_office_gross', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=3)
    col = Label(ui, width=10, text='movie_popularity', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=4)
    i = 1
    for movie in cursor:
        for j in range(len(movie)):
            e = Entry(ui, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, movie[j])
        i = i+1
    cursor.close()


def display_user_login():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute('select * from user_login')
    col = Label(ui, width=10, text='username', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=0)
    col = Label(ui, width=10, text='password', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=1)

    i = 1
    for user in cursor:
        for j in range(2):
            e = Entry(ui, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, user[j])
        i = i+1
    cursor.close()


def display_user_info():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute('select * from user_info')
    col = Label(ui, width=10, text='username', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=0)
    col = Label(ui, width=10, text='age', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=1)

    i = 1
    for user in cursor:
        for j in range(2):
            e = Entry(ui, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, user[j])
        i = i+1
    cursor.close()


def display_user_list():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute('select * from user_list')
    col = Label(ui, width=10, text='username', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=0)
    col = Label(ui, width=10, text='list', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=1)

    i = 1
    for user in cursor:
        for j in range(2):
            e = Entry(ui, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, user[j])
        i = i+1
    cursor.close()

def display_movie_list():
    main_label.grid_forget()
    text_label.grid_forget()
    conn = cx_Oracle.connect(conStr)
    # instantiating database object
    cursor = conn.cursor()
    cursor.execute('select * from movie_list')
    col = Label(ui, width=10, text='movie_id', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=0)
    col = Label(ui, width=10, text='list', borderwidth=2, relief='ridge',anchor='w')
    col.grid(row=0, column=1)

    i = 1
    for list in cursor:
        for j in range(2):
            e = Entry(ui, width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, list[j])
        i = i+1
    cursor.close()


def add_movie_title_helper():
    gui = tk.Tk()
    gui.geometry("800x500")
    gui.title("Add Records")

    def action():
        conn = cx_Oracle.connect(conStr)
        # instantiating database object
        cursor = conn.cursor()
        comm = cursor.execute("INSERT INTO movie_title (movie_id, movie_name) VALUES (:movie_id, :movie_name)",
                           {
                               'movie_id' :  movie_id.get(),
                               'movie_name' : movie_name.get()
                           }
        )
        conn.commit()
        conn.close()
        movie_id.delete(0,END)
        movie_name.delete(0,END)
        add_label = Label(gui, font=("arial", 10, "bold"), text="SUCCESSFULLY ADDED RECORD", bg="Ghost White")
        add_label.grid(row=6, column=5)
    movie_id = Entry(gui, width=20)
    movie_id.grid(row=0, column=1, padx=20, ipadx=20)
    movie_name = Entry(gui, width=20)
    movie_name.grid(row=1, column=1, padx=20, ipadx=20)

    movie_id_label = Label(gui, text="Movie ID", background="#d9d9d9")
    movie_id_label.grid(row=0, column=0)
    movie_name_label = Label(gui, text="Movie Name", background="#d9d9d9")
    movie_name_label.grid(row=1, column=0)

    add_record_btn = Button(gui, text="Add Record", command=action)
    add_record_btn.grid(row=2, column=2, pady=10, padx=10, ipadx=50)


def add_movie_att_helper():
    gui = tk.Tk()
    gui.geometry("800x500")
    gui.title("Add Records")

    def action():
        conn = cx_Oracle.connect(conStr)
        # instantiating database object
        cursor = conn.cursor()
        comm = cursor.execute("INSERT INTO movie_att (movie_name, movie_length, release_date, movie_actor, movie_rating) VALUES (:movie_name, :movie_length, TO_DATE(:release_date,'MM/DD/YY'), :movie_actor, :movie_rating)",
                              {
                                  'movie_name': movie_name.get(),
                                  'movie_length': movie_length.get(),
                                  'release_date': release_date.get(),
                                  'movie_actor': movie_actor.get(),
                                  'movie_rating': movie_rating.get()
                              }
                              )
        conn.commit()
        conn.close()
        movie_name.delete(0, END)
        movie_length.delete(0, END)
        release_date.delete(0, END)
        movie_actor.delete(0, END)
        movie_rating.delete(0, END)


    movie_name = Entry(gui, width=20)
    movie_name.grid(row=0, column=1, padx=20, ipadx=20)
    movie_length = Entry(gui, width=20)
    movie_length.grid(row=1, column=1, padx=20, ipadx=20)
    release_date = Entry(gui, width=20)
    release_date.grid(row=2, column=1, padx=20, ipadx=20)
    movie_actor = Entry(gui, width=20)
    movie_actor.grid(row=3, column=1, padx=20, ipadx=20)
    movie_rating = Entry(gui, width=20)
    movie_rating.grid(row=4, column=1, padx=20, ipadx=20)


    movie_name_label = Label(gui, text="Movie Name", background="#d9d9d9")
    movie_name_label.grid(row=0, column=0)
    movie_length_label = Label(gui, text="Movie Length", background="#d9d9d9")
    movie_length_label.grid(row=1, column=0)
    release_date_label = Label(gui, text="Release Date", background="#d9d9d9")
    release_date_label.grid(row=2, column=0)
    movie_actor_label = Label(gui, text="Movie Actor", background="#d9d9d9")
    movie_actor_label.grid(row=3, column=0)
    movie_rating_label = Label(gui, text="Movie Rating", background="#d9d9d9")
    movie_rating_label.grid(row=4, column=0)

    add_record_btn = Button(gui, text="Add Record", command=action)
    add_record_btn.grid(row=2, column=2, pady=10, padx=10, ipadx=50)


def add_movie_sequel_helper():
    gui = tk.Tk()
    gui.geometry("800x500")
    gui.title("Add Records")

    def action():
        conn = cx_Oracle.connect(conStr)
        # instantiating database object
        cursor = conn.cursor()
        comm = cursor.execute("INSERT INTO movie_sequel (movie_name, sequel_name) VALUES (:movie_name, :sequel_name)",
                           {
                               'movie_name':  movie_name.get(),
                               'sequel_name': sequel_name.get()
                           }
        )
        conn.commit()
        conn.close()
        movie_name.delete(0,END)
        sequel_name.delete(0,END)
    movie_name = Entry(gui, width=20)
    movie_name.grid(row=0, column=1, padx=20, ipadx=20)
    sequel_name = Entry(gui, width=20)
    sequel_name.grid(row=1, column=1, padx=20, ipadx=20)

    movie_name_label = Label(gui, text="Movie Name", background="#d9d9d9")
    movie_name_label.grid(row=0, column=0)
    sequel_name_label = Label(gui, text="Sequel Name", background="#d9d9d9")
    sequel_name_label.grid(row=1, column=0)

    add_record_btn = Button(gui, text="Add Record", command=action)
    add_record_btn.grid(row=2, column=2, pady=10, padx=10, ipadx=50)


def add_sequel_info_helper():
    gui = tk.Tk()
    gui.geometry("800x500")
    gui.title("Add Records")

    def action():
        conn = cx_Oracle.connect(conStr)
        # instantiating database object
        cursor = conn.cursor()
        comm = cursor.execute("INSERT INTO sequel_info (next_sequel_id, movie_id, movie_name) VALUES (:next_sequel_id, :movie_id, :movie_name)",
                           {
                               'next_sequel_id': next_sequel_id.get(),
                               'movie_id': movie_id.get(),
                               'movie_name':  movie_name.get(),
                           }
        )
        conn.commit()
        conn.close()
        next_sequel_id.delete(0,END)
        movie_id.delete(0,END)
        movie_name.delete(0, END)
    next_sequel_id = Entry(gui, width=20)
    next_sequel_id.grid(row=0, column=1, padx=20, ipadx=20)
    movie_id = Entry(gui, width=20)
    movie_id.grid(row=1, column=1, padx=20, ipadx=20)
    movie_name = Entry(gui, width=20)
    movie_name.grid(row=2, column=1, padx=20, ipadx=20)

    next_sequel_id_label = Label(gui, text="Next Sequel ID", background="#d9d9d9")
    next_sequel_id_label.grid(row=0, column=0)
    movie_id_label = Label(gui, text="Movie ID", background="#d9d9d9")
    movie_id_label.grid(row=1, column=0)
    movie_name_label = Label(gui, text="Movie Name", background="#d9d9d9")
    movie_name_label.grid(row=2, column=0)

    add_record_btn = Button(gui, text="Add Record", command=action)
    add_record_btn.grid(row=2, column=2, pady=10, padx=10, ipadx=50)


def add_movie_rating_helper():
    gui = tk.Tk()
    gui.geometry("800x500")
    gui.title("Add Records")

    def action():
        conn = cx_Oracle.connect(conStr)
        # instantiating database object
        cursor = conn.cursor()
        comm = cursor.execute("INSERT INTO movie_rating (movie_id, rating_id, movie_score, box_office_gross, movie_popularity) VALUES (:movie_id, :rating_id, :movie_score, :box_office_gross, :movie_popularity)",
                              {
                                  'movie_id': movie_id.get(),
                                  'rating_id': rating_id.get(),
                                  'movie_score': movie_score.get(),
                                  'box_office_gross': box_office_gross.get(),
                                  'movie_popularity': movie_popularity.get()
                              }
                              )
        conn.commit()
        conn.close()
        movie_id.delete(0, END)
        rating_id.delete(0, END)
        movie_score.delete(0, END)
        box_office_gross.delete(0, END)
        movie_popularity.delete(0, END)


    movie_id = Entry(gui, width=20)
    movie_id.grid(row=0, column=1, padx=20, ipadx=20)
    rating_id = Entry(gui, width=20)
    rating_id.grid(row=1, column=1, padx=20, ipadx=20)
    movie_score = Entry(gui, width=20)
    movie_score.grid(row=2, column=1, padx=20, ipadx=20)
    box_office_gross = Entry(gui, width=20)
    box_office_gross.grid(row=3, column=1, padx=20, ipadx=20)
    movie_popularity = Entry(gui, width=20)
    movie_popularity.grid(row=4, column=1, padx=20, ipadx=20)


    movie_id_label = Label(gui, text="Movie ID", background="#d9d9d9")
    movie_id_label.grid(row=0, column=0)
    rating_id_label = Label(gui, text="Rating Id", background="#d9d9d9")
    rating_id_label.grid(row=1, column=0)
    movie_score_label = Label(gui, text="Movie Score", background="#d9d9d9")
    movie_score_label.grid(row=2, column=0)
    box_office_gross_label = Label(gui, text="Box Office Gross", background="#d9d9d9")
    box_office_gross_label.grid(row=3, column=0)
    movie_popularity_label = Label(gui, text="Movie Popularity", background="#d9d9d9")
    movie_popularity_label.grid(row=4, column=0)

    add_record_btn = Button(gui, text="Add Record", command=action)
    add_record_btn.grid(row=2, column=2, pady=10, padx=10, ipadx=50)


def add_user_login_helper():
    gui = tk.Tk()
    gui.geometry("800x500")
    gui.title("Add Records")

    def action():
        conn = cx_Oracle.connect(conStr)
        # instantiating database object
        cursor = conn.cursor()
        comm = cursor.execute("INSERT INTO user_login (username, password_log) VALUES (:username, :password)",
                           {
                               'username':  username.get(),
                               'password': password.get()
                           }
        )
        conn.commit()
        conn.close()
        username.delete(0,END)
        password.delete(0,END)
    username = Entry(gui, width=20)
    username.grid(row=0, column=1, padx=20, ipadx=20)
    password = Entry(gui, width=20)
    password.grid(row=1, column=1, padx=20, ipadx=20)

    username_label = Label(gui, text="Username", background="#d9d9d9")
    username_label.grid(row=0, column=0)
    password_label = Label(gui, text="Password", background="#d9d9d9")
    password_label.grid(row=1, column=0)

    add_record_btn = Button(gui, text="Add Record", command=action)
    add_record_btn.grid(row=2, column=2, pady=10, padx=10, ipadx=50)


def add_user_info_helper():
    gui = tk.Tk()
    gui.geometry("800x500")
    gui.title("Add Records")

    def action():
        conn = cx_Oracle.connect(conStr)
        # instantiating database object
        cursor = conn.cursor()
        comm = cursor.execute("INSERT INTO user_info (username, age) VALUES (:username, :age)",
                           {
                               'username':  username.get(),
                               'age': age.get()
                           }
        )
        conn.commit()
        conn.close()
        username.delete(0,END)
        age.delete(0,END)
    username = Entry(gui, width=20)
    username.grid(row=0, column=1, padx=20, ipadx=20)
    age = Entry(gui, width=20)
    age.grid(row=1, column=1, padx=20, ipadx=20)

    username_label = Label(gui, text="Username", background="#d9d9d9")
    username_label.grid(row=0, column=0)
    age_label = Label(gui, text="Age", background="#d9d9d9")
    age_label.grid(row=1, column=0)

    add_record_btn = Button(gui, text="Add Record", command=action)
    add_record_btn.grid(row=2, column=2, pady=10, padx=10, ipadx=50)


def add_user_list_helper():
    gui = tk.Tk()
    gui.geometry("800x500")
    gui.title("Add Records")

    def action():
        conn = cx_Oracle.connect(conStr)
        # instantiating database object
        cursor = conn.cursor()
        comm = cursor.execute("INSERT INTO user_list (username, movie_list) VALUES (:username, :movie_list)",
                           {
                               'username':  username.get(),
                               'movie_list': movie_list.get()
                           }
        )
        conn.commit()
        conn.close()
        username.delete(0,END)
        movie_list.delete(0,END)
    username = Entry(gui, width=20)
    username.grid(row=0, column=1, padx=20, ipadx=20)
    movie_list = Entry(gui, width=20)
    movie_list.grid(row=1, column=1, padx=20, ipadx=20)

    username_label = Label(gui, text="Username", background="#d9d9d9")
    username_label.grid(row=0, column=0)
    movie_list_label = Label(gui, text="Movie List", background="#d9d9d9")
    movie_list_label.grid(row=1, column=0)

    add_record_btn = Button(gui, text="Add Record", command=action)
    add_record_btn.grid(row=2, column=2, pady=10, padx=10, ipadx=50)



def add_movie_list_helper():
    gui = tk.Tk()
    gui.geometry("800x500")
    gui.title("Add Records")

    def action():
        conn = cx_Oracle.connect(conStr)
        # instantiating database object
        cursor = conn.cursor()
        comm = cursor.execute("INSERT INTO movie_list (movie_id, movie_list) VALUES (:movie_id, :movie_list)",
                           {
                               'movie_id':  movie_id.get(),
                               'movie_list': movie_list.get()
                           }
        )
        conn.commit()
        conn.close()
        movie_id.delete(0,END)
        movie_list.delete(0,END)
    movie_id = Entry(gui, width=20)
    movie_id.grid(row=0, column=1, padx=20, ipadx=20)
    movie_list = Entry(gui, width=20)
    movie_list.grid(row=1, column=1, padx=20, ipadx=20)

    username_label = Label(gui, text="Movie ID", background="#d9d9d9")
    username_label.grid(row=0, column=0)
    movie_list_label = Label(gui, text="Movie List", background="#d9d9d9")
    movie_list_label.grid(row=1, column=0)

    add_record_btn = Button(gui, text="Add Record", command=action)
    add_record_btn.grid(row=2, column=2, pady=10, padx=10, ipadx=50)





# create table menu
create_menu = Menu(main_menu)
main_menu.add_cascade(label="Create Table", menu=create_menu)
create_menu.add_command(label="Movie Title Table", command=create_movie_title)
create_menu.add_separator()
create_menu.add_command(label="Movie Attributes Table", command=create_movie_att)
create_menu.add_separator()
create_menu.add_command(label="Movie Rating Table", command=create_movie_rating)
create_menu.add_separator()
create_menu.add_command(label="Movie Sequel Table", command=create_movie_sequel)
create_menu.add_separator()
create_menu.add_command(label="Sequel Information Table", command=create_sequel_info)
create_menu.add_separator()
create_menu.add_command(label="User Login Table", command=create_user_login)
create_menu.add_separator()
create_menu.add_command(label="User Information Table", command=create_user_info)
create_menu.add_separator()
create_menu.add_command(label="User List Table", command=create_user_list)
create_menu.add_separator()
create_menu.add_command(label="Movie List Table", command=create_movie_list)
create_menu.add_separator()
create_menu.add_command(label="Exit", command=ui.quit)


# drop table menu
drop_menu = Menu(main_menu)
main_menu.add_cascade(label="Drop Table", menu=drop_menu)
drop_menu.add_command(label="Movie Title Table", command=drop_movie_title)
drop_menu.add_separator()
drop_menu.add_command(label="Movie Attributes Table", command=drop_movie_att)
drop_menu.add_separator()
drop_menu.add_command(label="Movie Rating Table", command=drop_movie_rating)
drop_menu.add_separator()
drop_menu.add_command(label="Movie Sequel Table", command=drop_movie_sequel)
drop_menu.add_separator()
drop_menu.add_command(label="Sequel Information Table", command=drop_sequel_info)
drop_menu.add_separator()
drop_menu.add_command(label="User Login Table", command=drop_user_login)
drop_menu.add_separator()
drop_menu.add_command(label="User Information Table", command=drop_user_info)
drop_menu.add_separator()
drop_menu.add_command(label="User List Table", command=drop_user_list)
drop_menu.add_separator()
drop_menu.add_command(label="Movie List Table", command=drop_movie_list)
drop_menu.add_separator()
drop_menu.add_command(label="Exit", command=ui.quit)

# populate table menu
pop_menu = Menu(main_menu)
main_menu.add_cascade(label="Populate Table", menu=pop_menu)
pop_menu.add_command(label="Movie Title Table", command=add_movie_title_helper)
pop_menu.add_separator()
pop_menu.add_command(label="Movie Attributes Table", command=add_movie_att_helper)
pop_menu.add_separator()
pop_menu.add_command(label="Movie Rating Table", command=add_movie_rating_helper)
pop_menu.add_separator()
pop_menu.add_command(label="Movie Sequel Table", command=add_movie_sequel_helper)
pop_menu.add_separator()
pop_menu.add_command(label="Sequel Information Table", command=add_sequel_info_helper)
pop_menu.add_separator()
pop_menu.add_command(label="User Login Table", command=add_user_login_helper)
pop_menu.add_separator()
pop_menu.add_command(label="User Information Table", command=add_user_info_helper)
pop_menu.add_separator()
pop_menu.add_command(label="User List Table", command=add_user_list_helper)
pop_menu.add_separator()
pop_menu.add_command(label="Movie List Table", command=add_movie_list_helper)
pop_menu.add_separator()
pop_menu.add_command(label="Exit", command=ui.quit)

# query table menu
query_menu = Menu(main_menu)
main_menu.add_cascade(label="Query", menu=query_menu)
query_menu.add_command(label="Movie Title Table", command=some_command)
query_menu.add_separator()
query_menu.add_command(label="Movie Attributes Table", command=some_command)
query_menu.add_separator()
query_menu.add_command(label="Movie Rating Table", command=some_command)
query_menu.add_separator()
query_menu.add_command(label="Movie Sequel Table", command=some_command)
query_menu.add_separator()
query_menu.add_command(label="Sequel Information Table", command=some_command)
query_menu.add_separator()
query_menu.add_command(label="User Login Table", command=some_command)
query_menu.add_separator()
query_menu.add_command(label="User Information Table", command=some_command)
query_menu.add_separator()
query_menu.add_command(label="User List Table", command=some_command)
query_menu.add_separator()
query_menu.add_command(label="Movie List Table", command=query1)
query_menu.add_separator()
query_menu.add_command(label="Exit", command=ui.quit)

# display table menu
display_menu = Menu(main_menu)
main_menu.add_cascade(label="Display Table", menu=display_menu)
display_menu.add_command(label="Movie Title Table", command=display_movie_title)
display_menu.add_separator()
display_menu.add_command(label="Movie Attributes Table", command=display_movie_att)
display_menu.add_separator()
display_menu.add_command(label="Movie Rating Table", command=display_movie_rating)
display_menu.add_separator()
display_menu.add_command(label="Movie Sequel Table", command=display_movie_sequel)
display_menu.add_separator()
display_menu.add_command(label="Sequel Information Table", command=display_sequel_info)
display_menu.add_separator()
display_menu.add_command(label="User Login Table", command=display_user_login)
display_menu.add_separator()
display_menu.add_command(label="User Information Table", command=display_user_info)
display_menu.add_separator()
display_menu.add_command(label="User List Table", command=display_user_list)
display_menu.add_separator()
display_menu.add_command(label="Movie List Table", command=display_movie_list)
display_menu.add_separator()
display_menu.add_command(label="Exit", command=ui.quit)


ui.mainloop()

cursor.close()
conn.close()
