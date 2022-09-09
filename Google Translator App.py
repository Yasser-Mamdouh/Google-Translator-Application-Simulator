
""" Translator App Using Python GUI Tkinter """ 

from tkinter import *
from tkinter import ttk , messagebox
import googletrans 
import textblob


root = Tk()

root.title("Google Translator App")
root.geometry("1080x400")


# Function that set label to selected language 

def Change_Label():

    """ this funtion set label of current selected language """

    first_combobox = first_language_combobox.get()
    second_combobox = second_language_combobox.get()

    first_language_label.configure(text = first_combobox)
    second_language_label.configure(text = second_combobox)

    root.after(1000 , Change_Label)


# Translate Button Function 

def Translate():

    """ when translate button clicked this function will be worked  """

    global languages

    try :
        text_ = first_text_entry.get(1.0 , END)
        first_combobox = first_language_combobox.get()
        second_combobox = second_language_combobox.get()
        if(text_):
            words = textblob.TextBlob(text_)
            lan = words.detect_language()
            for i , j in languages.items():
                if(j == first_combobox):
                    lan_ = i
            words = words.translate(from_lang = lan , to= str(lan_))
            second_text_entry.delete(1.0 , END)
            second_text_entry.insert(END , words)

    except Exception as e :

        messagebox.showerror("google trans" , "please try again ?!")


# Title Icon "Google Icon"

google_icon = PhotoImage(file = "google.png")
root.iconphoto(False , google_icon)

# arrow icon that separate between text fields

arrow_icon = PhotoImage(file = "arrow.png")
arrow_label = Label(root , image = arrow_icon , width = 150)
arrow_label.place(x = 460 , y = 50)

languages = googletrans.LANGUAGES
languages_variable = list(languages.values())
first_language = languages.keys()

first_language_combobox = ttk.Combobox(root , values = languages_variable , font = ("Raleway",14) , state = "r")
first_language_combobox.place(x = 110 , y = 20)
first_language_combobox.set("English")


first_language_label = Label(root , text = "English" , font = ("Raleway",18) , bg = "#20bebe" , width = 18 , 
                             bd = 5 , relief = GROOVE)

first_language_label.place(x = 10 , y = 50)

first_frame = Frame(root , bg = "gray" , bd = 5)
first_frame.place(x = 10 , y = 118 , width = 440 , height = 210)

first_text_entry = Text(first_frame , font = ("Raleway" , 20) , bg = "White" , relief = GROOVE , wrap = WORD)
first_text_entry.place(x = 0 , y = 0 , width = 430, height = 200)

first_scrollbar = Scrollbar(first_frame)
first_scrollbar.pack(side = "right" , fill = "y")
first_scrollbar.configure(command = first_text_entry.yview)

first_text_entry.configure(yscrollcommand = first_scrollbar.set)

second_language_combobox = ttk.Combobox(root , values = languages_variable , font = ("Raleway" , 14) , state = "r")
second_language_combobox.place(x = 730 , y = 20)
second_language_combobox.set("Select Language")


second_language_label = Label(root , text = "English" , font = ("Raleway", 18) , bg = "#20bebe" , width = 18 , 
                             bd = 5 , relief = GROOVE)

second_language_label.place(x = 620  , y = 50)


second_frame = Frame(root , bg = "gray" , bd = 5)
second_frame.place(x = 620 , y = 118 , width = 440 , height = 210)

second_text_entry = Text(second_frame , font = ("Raleway" , 20) , bg = "White" , relief = GROOVE , wrap = WORD)
second_text_entry.place(x = 0 , y = 0 , width = 430, height = 200)

second_scrollbar = Scrollbar(second_frame)
second_scrollbar.pack(side = "right" , fill = "y")
second_scrollbar.configure(command = second_text_entry.yview)

second_text_entry.configure(yscrollcommand = second_scrollbar.set)


# Translator Button 

translate_button = Button(root , text = "Translate" , font = ("Raleway" , 15) , activebackground = " purple " , 
                   cursor = "hand2" , bd = 5 , bg = " black " , fg = " red " , command = Translate)

translate_button.place(x = 480 , y = 250)


Change_Label()

root.configure(bg="#ccddff")

root.mainloop()