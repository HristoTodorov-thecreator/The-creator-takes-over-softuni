from tkinter import Button,Entry
from canv import window,frame
from help import clean_screen
from json import loads,dump
from buy_page import display_products


def render_entry():
    # create the buttons
    reguster_button = Button(
        window,
        text = 'Register',
        bg='blue',
        fg='white',
        width=20,
        height=3,
        font=("Georgia"),
        command=register # call the function
    )

    login_button = Button(
        text='Login',
        bg='red',
        fg='white',
        width=20,
        height=3,
        font=("Georgia"),
        command=login

    )
    # place the buttons on this positions
    frame.create_window(350,250,window=reguster_button)
    frame.create_window(350, 330, window=login_button)


def logging():
    if check_logging(): # check if the user with pass is valid
        print('start')

        display_products() # show the products

    else:

        frame.create_text(160,200,text='Invalid user or pass')

def check_logging():
    info_data = get_users_data()


    user_username = username_box.get() # get the user
    user_password = pass_box.get() # get the pass


    for record in info_data: # get the username and pass from the data
        record_username = record['Username']
        record_password = record['Pass']

        if user_username == record_username and user_password == record_password: # check if they are the same
            return True

    return False

def get_users_data():
    info_data = []

    try:
        with open("db/users_information.txt", "r") as users_file: # take the info from db
            for line in users_file:
                info_data.append(loads(line)) # save the line like json
    except (FileNotFoundError, ValueError):
        pass

    return info_data
def login():
    clean_screen()
    # create the text displaying user and pass
    frame.create_text(100,50,text='Username')
    frame.create_text(100, 100, text='Password')

     # create field to put the data
    frame.create_window(200,50,window=username_box)
    frame.create_window(200, 100,window=pass_box)

    #button for login
    login_button = Button(
        window,text='Login',bg='black',fg='blue',command=logging
    )
    frame.create_window(250,150,window=login_button)


def register():
    clean_screen()

    # fields with text

    frame.create_text(100,50,text='First name:')
    frame.create_text(100, 100,text='Last name:')
    frame.create_text(100, 150,text='Username:')
    frame.create_text(100, 200,text='Password:')

    # creating fields to enter the data
    frame.create_window(200,50,window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=pass_box)

    # create the button
    reguster_button = Button(
        window,
        text='Register',
        bg='black',
        fg='white',

        font=("Georgia"),
        command=registration
    )
    frame.create_window(300,250,window=reguster_button)

def registration():
    # take the info
    info = {
        'First name':first_name_box.get(),
        'Last name':last_name_box.get(),
        'Username':username_box.get(),
        'Pass':pass_box.get()
    }

    if check_registration(info):
        with open('db/users_information.txt', 'a') as users_file:
            dump(info, users_file) #save the info in the file
            users_file.write('\r\n') # new row
            display_products() # show the products





def check_registration(info):
    frame.delete('error') # delete recent error
    for key,value in info.items():
        if not value.strip():
            frame.create_text(
                300,300,text=f'{key} cannot be empty',fill='red',tags='error',
            )
            return False

    info_data = get_users_data() # take the info

    for record in info_data:
        if record['Username'] == info['Username']:
            frame.create_text(
                300, 300, text=f'Username is already taken', fill='red', tags='error',
            )
            return False

    return True


# create data entry field
first_name_box = Entry(window)
last_name_box = Entry(window)
username_box = Entry(window)
pass_box = Entry(window,show='*')