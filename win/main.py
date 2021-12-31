import os
from tkinter import *
from tkinter import ttk
import subprocess

# reference https://stackoverflow.com/a/34466743
class CustomButton(Label):

    def __init__(self, *args, **kwargs):
        # TODO: Create a Frame for border https://www.geeksforgeeks.org/how-to-change-border-color-in-tkinter-widget/
        Label.__init__(self)
        self.bind("<Enter>", self.changeBGEnter)
        self.bind("<Leave>", self.changeBGLeave)
        self.bind("<Button-1>",kwargs.get('handleClick',self.handleClickDefault) )

        self.background = kwargs.get('background',"#1890ff")
        self.hoverBackground = kwargs.get('hoverBackground',"#40a9ff")
        self.foreground = kwargs.get('foreground',"#fff")
        self.fontsize = kwargs.get('fontsize',14) 
        self.fontfamily = kwargs.get('fontfamily',"微软雅黑") 
        self.text = kwargs.get('text',"Button") 
        self.width = kwargs.get('width',30) 
        self.padx = kwargs.get('padx',10) 
        self.pady = kwargs.get('pady',10) 
        self.relief = kwargs.get('relief','solid') 
        self.borderwidth = kwargs.get('borderwidth',1) 
        self.anchor = kwargs.get('anchor','center') 
        self.justify = kwargs.get('justify','center') 

        self.config(
            anchor=self.anchor,  # Where to anchor the text in the widget
            justify=self.justify,
            background=self.background,
            foreground=self.foreground,
            font=(self.fontfamily, self.fontsize),
            text=self.text,
            relief=self.relief,
            width=self.width,
            padx=self.padx,
            pady=self.pady,
            borderwidth=self.borderwidth
        )

    def changeBGEnter(self,event):
        self.config(background=self.hoverBackground,foreground=self.foreground)

    def changeBGLeave(self, event):
        self.config(background=self.background,foreground=self.foreground)
    
    def handleClickDefault(self, event):
        print('click')

class Win:
    def __init__(self,root):
        # path
        dirname = os.path.dirname(__file__)
        self.classic = os.path.join(dirname, 'bat/classic.bat')
        self.default = os.path.join(dirname, 'bat/default.bat')
        
        
        # set title
        root.title("Windows 11 Menu Editor")

        # screen width
        sw = root.winfo_screenwidth()
        # screen height
        sh = root.winfo_screenheight()
        # frame width
        ww = 380
        # frame height
        wh = 180
        x = (sw-ww) / 2
        y = (sh-wh) / 2 - 20

        root.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
        root.resizable(False, False)
        root.config(background="white")
        
        # create content frame
        mainFrame = ttk.Frame(root,padding='20 20 20 20')
        mainFrame.grid(column=0,row=0,sticky=(N,W,E,S))
        # The columnconfigure/rowconfigure bits tell Tk that the frame should expand to fill any extra space if the window is resized.
        root.columnconfigure(0,weight=1)
        root.rowconfigure(0,weight=1)

        # classic button
        classicButton = CustomButton(root, text="Change to Win10 Classic Menu",handleClick=self.useClassic)
        classicButton.grid(column=0, row=0, columnspan=2, sticky=(N, W), padx=5,pady=20)

        # default button
        defaultButton = CustomButton(root, text="Change to Win11 Default Menu",foreground='#1a1a1a',hoverBackground="#ede9e5",background='#fcfbfa',handleClick=self.useDefault)
        defaultButton.grid(column=0, row=1, columnspan=2, sticky=(N, W), padx=5,pady=20)
    # exec bat
    def useClassic(self,*args):

        # hide cmd window
        # reference https://stackoverflow.com/a/7006424
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        #si.wShowWindow = subprocess.SW_HIDE # default
        subprocess.call(self.classic, startupinfo=si)

    def useDefault(self,*args):

        # os.system(self.default)
        # subprocess.Popen(self.default)

        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        #si.wShowWindow = subprocess.SW_HIDE # default
        subprocess.call(self.default, startupinfo=si)

# sets up the main application window
root = Tk()
# init function
Win(root)
# necessary for everything to appear onscreen and allow users to interact with it.
root.mainloop()
