from tkinter import *
from tkinter import filedialog
import PyPDF2
import pyttsx3

# making windows
root = Tk()
root.geometry('320x525')
root.title('AUDIO BOOK')
root.config(bg='black')

# sest image on bg
canvas = Canvas(root, bg='black')
canvas.pack()
img = PhotoImage(file='download.png')
canvas.create_image(45, 0, anchor=NW, image=img)
# defina label for app name
Label(root, text='AUDIO BOOK', font='Verdana 20 bold', fg='white', bg='black').pack()
Label(root, text='BY HARSH MISHRA', font='Verdana 10 bold', fg='white', bg='black').pack()

# variable for asl image width and height
page_no = IntVar()
page_no_ToStop=IntVar()
# taking page no
Label(root, text='ENTER PAGE', font='Verdana 10 bold', fg='black', bg='gold').place(x=10, y=410)
Label(root, text='ENTER PAGE TO STOP', font='Verdana 10 bold', fg='black', bg='gold').place(x=10, y=440)
# Entry box

Entry(root, textvariable=page_no, font='Verdana 10 bold', fg='black', bg='gold', borderwidth=3, width=9).place(x=190, y=410)
Entry(root, textvariable=page_no_ToStop, font='Verdana 10 bold', fg='black', bg='gold',borderwidth=3, width=9).place(x=190, y=440)
# function for select file for browser
def ChooseFile() :
    global filename
    # browser file
    filename = filedialog.askopenfilename(initialdir="/", title="Select a file",filetype=(('PDF File', '*.pdf*'), ('All Files', '*.*')))
    # change label contents
    label_file_explorer.configure(text='File:' + filename)


# function for start speak
def StartSpeak() :
    global speak
    path = open(filename, 'rb')
    pdfreader = PyPDF2.PdfFileReader(path)
    from_page = pdfreader.getPage(page_no.get())

    for i in range(page_no.get(),page_no_ToStop.get()):

        text = from_page.extractText()

        speak = pyttsx3.init()
        voices = speak.getProperty('voices')
        speak.setProperty('voice', voices[1].id)
        speak.say(text)
        speak.runAndWait()


#function to stop speaking
def StopSpeak():
    speak.stop()

# label for file explore
label_file_explorer = Label(root, text="File", font='Verdana 10 bold', fg='black', bg='gold', width=50, height=2)
label_file_explorer.pack()
# design button for call to function
Button(root, text='Choose File', font='Verdana 10 bold', fg='black', bg='gold', command=ChooseFile).place(x=10, y=480)
Button(root, text='Start', font='Verdana 10 bold', fg='black', bg='gold', command=StartSpeak).place(x=150, y=480)
Button(root, text='Stop', font='Verdana 10 bold', fg='black', bg='gold', command=StopSpeak).place(x=240, y=480)


root.mainloop()
