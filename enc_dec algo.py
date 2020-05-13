
#import statements
from tkinter import *
from Functions import *
from tkinter import filedialog
import random

#Global variables intialized
mainWindow = None
dEntry = None
eEntry = None
keyLabel = None
eEntry2 = None
dEntry2 = None
text = None
filename = None
edisplay = None
ddisplay = None

#Functions
def GUIMain():
    '''This is the main GUI function for the user interface'''
    global mainWindow
    global keyLabel
    global eEntry2
    global eEntry
    global dEntry
    global dEntry2
    global edisplay
    global ddisplay
    mainWindow = Tk()
    mainWindow.title("Encrypt and Decrypt using a onetime Cipher")
    mainWindow.config(bg = "lightblue")
    keyButton = Button(mainWindow,text="Generate Key",command=keyGenerate)
    keyButton.grid(row=0,column=1)
    keyLabel = Label(mainWindow,text="",bg='lightblue')
    keyLabel.grid(row=0,column=2)
    encryptLabel = Label(mainWindow,text="Encrypt:",bg="lightblue",font="Arial 12 bold")
    encryptLabel.grid(row=2,column=1)
    decryptLabel = Label(mainWindow,text="Decrypt:",bg="lightblue",font="Arial 12 bold")
    decryptLabel.grid(row=7,column=1)
    #Encrypting section of GUI
    eLabel = Label(mainWindow, text="Key:",bg="lightblue")
    eLabel_2 = Label(mainWindow, text="Message:",bg="lightblue")
    eLabel_3 = Label(mainWindow, text = "Or:",bg="lightblue")
    eLabel_4 = Label(mainWindow,text="(Leave blank if you wish to upload file)",bg='lightblue')
    edisplay = Label(mainWindow, text="", bg='lightblue')
    edisplay.grid(row=6, column=2)
    eEntry = Entry(mainWindow)
    eEntry2 = Entry(mainWindow)
    eLabel_2.grid(row=4, column=1)
    eLabel_3.grid(row=5, column=1)
    eLabel_4.grid(row=4, column=3)
    eEntry.grid(row=3, column=2)
    eEntry2.grid(row=4, column=2)
    euploadButton = Button(mainWindow, text="Upload File", command=euploadCallback)
    euploadButton.grid(row=5, column=2)
    efinishButton = Button(mainWindow, text="Finish", command=efinishCallback)
    efinishButton.grid(row=6, column=1)
    eLabel.grid(row=3, column=1)
    #Decrypting Section of GUI
    dLabel_1 = Label(mainWindow, text="Key:",bg='lightblue')
    dLabel_2 = Label(mainWindow, text="Ciphertext:",bg='lightblue')
    dLabel_3 = Label(mainWindow,text,text='Or:',bg='lightblue')
    dLabel_4 = Label(mainWindow, text="(Leave blank if you wish to upload file)", bg='lightblue')
    ddisplay = Label(mainWindow, text="", bg='lightblue')
    ddisplay.grid(row=11, column=2)
    dEntry = Entry(mainWindow)
    dEntry2 = Entry(mainWindow)
    dLabel_1.grid(row=8, column=1)
    dLabel_2.grid(row=9, column=1)
    dLabel_3.grid(row=10, column=1)
    dLabel_4.grid(row =9,column=3)
    dEntry.grid(row=8, column=2)
    dEntry2.grid(row=9, column=2)
    duploadButton = Button(mainWindow, text="Upload File", command=duploadCallback)
    duploadButton.grid(row=10, column=2)
    dfinishButton = Button(mainWindow, text="Finish", command=dfinishCallback)
    dfinishButton.grid(row=11, column=1)

    mainWindow.mainloop()

#Callback Functions
def keyGenerate():
    '''Callback function for the key generate button'''
    global mainWindow
    global keyLabel
    length = random.randrange(5,16,1)
    key = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(length):
        pos = random.randrange(0,52,1)
        letter = alphabet[pos]
        key = key + letter
    keyLabel.config(text=key)

def euploadCallback():
    '''Callback for the file upload button in the encrypt section of the GUI'''
    global mainWindow
    global eEntry2
    global text
    global filename
    filename = filedialog.askopenfilename(title = "Select File",filetypes= (("text files","*.txt"),("all files","*.*")),initialdir = "/")
    text = readDoc(filename)
    uploadLabel = Label(mainWindow, text="Document Uploaded",bg='yellow')
    uploadLabel.grid(row=5,column=3)

def duploadCallback():
    '''Callback for the file upload button in the decrypt section of the GUI'''
    global mainWindow
    global eEntry2
    global text
    global filename
    filename = filedialog.askopenfilename(title = "Select File",filetypes= (("text files","*.txt"),("all files","*.*")),initialdir = "/")
    text = readDoc(filename)
    uploadLabel = Label(mainWindow, text="Document Uploaded",bg='yellow')
    uploadLabel.grid(row=10, column=3)


def efinishCallback():
    '''Called when the Finish button for encrypting is pressed'''
    global eEntry
    global eEntry2
    global mainWindow
    global text
    global filename
    global edisplay
    key = eEntry.get()
    edisplay.config(text="")
    if eEntry2.get() != "":
        plaintext = eEntry2.get()
        ciphertext = eMain2(key,plaintext)
        edisplay.config(text=ciphertext)
    else:
        docText = text
        texttowrite = eMain(key,docText)
        toWrite = open(filename[:-4]+'_encrypted.txt','w')
        for char in texttowrite:
            toWrite.write(char)
        toWrite.close()
        display = Label(mainWindow, text= "Encrypted Document Exported to file dirrectory",bg='orange')
        display.grid(row=6, column=3)
    print("Finished Encrypting!")



def dfinishCallback():
    '''Called when the Finish button for decrypting is pressed'''
    global dEntry
    global dEntry2
    global mainWindow
    global text
    global filename
    global ddisplay
    ddisplay.config(text="")
    key = dEntry.get()
    if dEntry2.get() != "":
        ciphertext = dEntry2.get()
        message = dMain2(key,ciphertext)
        ddisplay.config(text=message)
    else:
        docText = text
        texttowrite = dMain(key, docText)
        toWrite = open(filename[:-4] +'_decrypted.txt', 'w')
        for char in texttowrite:
            toWrite.write(char)
        toWrite.close()
        display = Label(mainWindow, text= "Decrypted Document Exported to file directory",bg='orange')
        display.grid(row=11,column=3)
    print("Finished Decrypting!")

#Main function call
GUIMain()