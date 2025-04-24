from tkinter import Button

from help import clean_screen
from json import load, dump
from PIL import Image, ImageTk
from canv import frame, window

images = [] # tkinter will delete the images if there is no save

def display_products():

    clean_screen() # empty the screen before loading the products

    display_stock() # show the products
def display_stock():


    with open("db\products_data.json","r") as stock:
        info = load(stock) # loading the products from json

    x,y = 150,50

    for item_name,item_info in info.items():
        item_img = ImageTk.PhotoImage(Image.open(item_info['image'])) # loading the image
        images.append(item_img) # save it

        frame.create_text(x,y,text=item_name) # name product
        frame.create_image(x,y+100,image=item_img) # image product
        color = 'green'
        text =f'In stock - {item_info["quantity"]}'

        if item_info['quantity'] > 0:
            item_button = Button(window,text='Buy',bg='green',fg = 'black',width = 5,command=lambda x=item_name,y=info: buy_product(x,y))

            frame.create_window(x,y+230,window=item_button)
        else:
            color ='red'
            text = 'Out of stock'

        frame.create_text(x,y+180,text=text,fill=color)

        x += 200

        if x > 550:
            y += 260
            x= 150

def buy_product(product,info):
    info[product]['quantity'] -=1

    with open('db/products_data.json','w') as stock: # save the quantity
        dump(info,stock)

    display_products() # renew the display

