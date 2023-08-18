from tkinter import *
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import imageio
import tkinter.messagebox as tmsg 
from tkinter.filedialog import askopenfilename, asksaveasfilename #for saving files in a directory
import pickle #save draw object in pickle file
from tkinter.colorchooser import askcolor #custom color palates
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from tkinter import messagebox
import pytweening
from win10toast import ToastNotifier
root= Tk()
root.state('zoomed')
toast = ToastNotifier()
toast.show_toast(
    "Adven Os",
    "Welcome to Adven Os",
    duration = 20,
    icon_path = "logoadven.png",
    threaded = True,
)
def writew():
    root = Tk()
    root.title('Write Experimental Version')
    text = Text(root, height=45)
    text.insert('1.0', '')
    text.pack()
def contacta():
    root2 = Tk()
    root2.title("Contacts")

    # Set geometry
    root2.geometry('400x500')

    # Information List
    datas = []

    # Add Information
    def add():
    	global datas
    	datas.append([Name.get(),Number.get(),address.get(1.0, "end-1c")])
    	update_book()

    # View Information
    def view():
    	Name.set(datas[int(select.curselection()[0])][0])
    	Number.set(datas[int(select.curselection()[0])][1])
    	address.delete(1.0,"end")
    	address.insert(1.0, datas[int(select.curselection()[0])][2])

    # Delete Information
    def delete():
    	del datas[int(select.curselection()[0])]
    	update_book()

    def reset():
    	Name.set('')
    	Number.set('')
    	address.delete(1.0,"end")

    # Update Information
    def update_book():
    	select.delete(0,END)
    	for n,p,a in datas:
    		select.insert(END, n)

    # Add Buttons, Label, ListBox
    Name = StringVar()
    Number = StringVar()

    frame = Frame()
    frame.pack(pady=10)

    frame1 = Frame()
    frame1.pack()

    frame2 = Frame()
    frame2.pack(pady=10)

    Label(frame, text = 'Name', font='arial 12 bold').pack(side=LEFT)
    Entry(frame, textvariable = Name,width=50).pack()

    Label(frame1, text = 'Phone No.', font='arial 12 bold').pack(side=LEFT)
    Entry(frame1, textvariable = Number,width=50).pack()

    Label(frame2, text = 'Address', font='arial 12 bold').pack(side=LEFT)
    address = Text(frame2,width=37,height=10)
    address.pack()

    Button(root,text="Add",font="arial 12 bold",command=add).place(x= 100, y=270)
    Button(root,text="View",font="arial 12 bold",command=view).place(x= 100, y=310)
    Button(root,text="Delete",font="arial 12 bold",command=delete).place(x= 100, y=350)
    Button(root,text="Reset",font="arial 12 bold",command=reset).place(x= 100, y=390)

    scroll_bar = Scrollbar(root, orient=VERTICAL)
    select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
    scroll_bar.config (command=select.yview)
    scroll_bar.pack(side=RIGHT, fill=Y)
    select.place(x=200,y=260)
def softup():
    root = Tk()
    root.title("Adven os")
    label = Label(root,
    			text ="A new software update is avalible for this device:", foreground='white')
    label.config(bg="black")
    label.pack(pady = 10)
    text = Text(root, height=30)
    text.pack()
    text.insert('1.0', 'Update to Adven Os Sierra In Windows 11, you decide when and how to get the latest updates to keep your device running smoothly and securely. To manage your options and see available updates, select Check for updates. Or select Start  > Settings  > Update . Here is some other info you might be looking for: If you get an error when trying to update, see Fix Update issues. If you are trying to activate, see Activate Windows for more info. If you are having trouble installing updates, see Troubleshoot problems updating. For answers to frequently asked questions, see Update: FAQ. To get the latest major update of Windows 11, see Get the latest Windows update. Check for Windows updates')
    text['state'] = 'disabled'
    label.pack(pady = 10)
def shut():
    # import modules
    import os


# user define function
    def shutdown():
      messagebox.showwarning("System", "The device will shut down")
      return os.system("shutdown /s /t 1")  
    def restart():
        messagebox.showwarning("System", "The device will restart")
        return os.system("shutdown /r /t 1")
	

    def logout():
        messagebox.showwarning("System", "You are being logged out")
        return os.system("shutdown -l")


# tkinter object
    master = Tk()
    master.configure(bg='black')
# background set to grey

# creating a button using the widget
# Buttons that will call the submit function
    Button(master, text="Shutdown", command=shutdown).grid(row=0)
    Button(master, text="Restart", command=restart).grid(row=1)
    Button(master, text="Log out", command=logout).grid(row=2)

    mainloop()
def fiopen():
    # Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library

# import filedialog module
    from tkinter import filedialog

# Function for opening the
# file explorer window
    def browseFiles():
        filename = filedialog.askopenfilename(initialdir = "/",
    										title = "Select a File",
    										filetypes = (("Text files",
    														"*.txt*"),
    													("all files",
    														"*.*")))	# Change label contents
        label_file_explorer.configure(text="File Opened: "+filename)
	
	
																								
# Create the root window
    window = Tk()

# Set window title
    window.title('File Explorer')

# Set window size
    window.geometry("500x500")

#Set window background color
    window.config(background = "white")

# Create a File Explorer label
    label_file_explorer = Label(window,
							text = "File Explorer using Tkinter",
							width = 100, height = 4,
							fg = "blue")

	
    button_explore = Button(window,
						text = "Browse Files",
						command = browseFiles)

    button_exit = Button(window,
					text = "Exit",
					command = exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
    label_file_explorer.grid(column = 1, row = 1)

    button_explore.grid(column = 1, row = 2)

    button_exit.grid(column = 1,row = 3)

# Let the window wait for any events
    window.mainloop()
def fctres():
    root = Tk()
    root.title("Adven os")
    label = Label(root,
    			text ="", foreground='white')
    label.config(bg="black")
    label.pack(pady = 10)
def sytstart2():
    return os.system("shutdown /r /t 1")
def sytstart():
    root = Tk()
    root.title("Adven os")
    canvas = Canvas(width = 20, height = 50, bg = 'black')

    # pack the canvas into a frame/form
    canvas.pack(expand = YES, fill = BOTH)

    # load the .gif image file
    # put in your own gif file here, may need to add full path
    # like 'C:/WINDOWS/Help/Tours/WindowsMediaPlayer/Img/mplogo.gif'
    gif1 = PhotoImage(file = 'vs.png')

    # put gif image on canvas
    # pic's upper left corner (NW) on the canvas is at x=50 y=10
    canvas.create_image(500, 10, image = gif1, anchor = NW)
    label = Label(root,
    			text ="This option requires a restart", foreground='white')
    label.config(bg="black")
    label.pack(pady = 200)
    btn = Button(root,
    			text ="       Ok       ",
    			command = sytstart2)
    btn.pack(pady = 7)
    root.mainloop()
    
def chimage():
    root = Tk()
    root.title("Adven os")
    
    label = Label(root,
    			text ="Change sytem image", foreground='white')
    label.config(bg="black")
    label.pack(pady = 10)
    btn = Button(root,
    			text ="64 Bit Image",
    			command = sytstart)
    btn.pack(pady = 19)
    label = Label(root,
    			text ="Be careful not to change to unsupported image" , foreground='white')
    label.config(bg="black")
    label.pack(pady = 10)
    root.mainloop()
def eng():
    root = Tk()
    root.geometry("300x200")
    root.title("Engineering Mode")

    def kernin():
        messagebox.showinfo("Kernel info", "(64-bit)\Spyder (anaconda3).lnk")
    btn = Button(root,
    			text ="View Kernel",
    			command = kernin)
    btn.pack(pady = 19)
    def videot():
        root = Tk()
        root.title("Engineering Mode")
        text = Text(root, height=30)
        text.pack()
        text.insert('1.0', 'These Terms of Use apply when you use the products and services of Family hub, L.L.C. or our affiliates, including our application programming interface, software, tools, developer services, data, documentation, and website (“Services”). The Terms include our Service Terms, Sharing & Publication Policy, Usage Policies, and other documentation, guidelines, or policies we may provide in writing. By using our Services, you agree to these Terms. Our Privacy Policy explains how we collect and use personal information. You may not (i) use the Services in a way that infringes, misappropriates or violates any person’s rights; (ii) reverse assemble, reverse compile, decompile, translate or otherwise attempt to discover the source code or underlying components of models, algorithms, and systems of the Services (except to the extent such restrictions are contrary to applicable law); (iii) use the Services to develop foundation models or other large scale models that compete with Family Hub; (iv) use any method to extract data from the Services, including web scraping, web harvesting, or web data extraction methods, other than as permitted through the Family Hub; (v) represent that output from the Services was human-generated when it is not; or You will comply with any rate limits and other requirements in our documentation. You may use Services only in geographies currently supported by Family Hub. Any third party software, services, or other products you use in connection with the Services are subject to their own terms, and we are not responsible for third party products.')
    btn = Button(root,
    			text ="Change terms",
    			command = videot)
    btn.pack(pady = 19)
    def sev2():
       root = Tk()
       root.title("Engineering Mode")
       btn = Button(root,
           			text ="Change",
                       command = server)
       btn.pack(pady = 19)
    def server():
        messagebox.showwarning("Engineering Mode", "Warning, if you change the server all the data for this device will be lost. The device will revert to origanal programing.")
        root = Tk()
        root.title("Engineering Mode")
    btn = Button(root,
        			text ="Change Server",
                    command = sev2)
    btn.pack(pady = 19)
    def orig():
        messagebox.showwarning("Sid Moniters", " This will leave the Family Hub permanently. Reinstall drivers at https://www.samsung.com/us/")
        root = Tk()
        root.title("Sid Moniters")
        label = Label(root,
        			text ="Welcome to Sytem Configuration")
        label.pack(pady = 10)
        
    btn = Button(root,
        			text ="Revert Programming",
                    command = orig)
    btn.pack(pady = 19)
    def forceup():
        root = Tk()
        root.title("Engineering Mode")
        label = Label(root,
        			text ="Force update was activated so the device must update")
        label.pack(pady = 10)
        label = Label(root,
        			text ="Improvments(US only)")
        label.pack(pady = 10)
        text = Text(root, height=30)
        text.pack()
        text.insert('1.0', '1)Gets rid of annoying screen glitch 2)Adds kernel creater function 3)Removes unnecesary processing drivers')
        text['state'] = 'disabled'
        label.pack(pady = 10)
        label.pack(pady = 10)
        label = Label(root,
        			text ="Updating...")
        label.pack(pady = 10)
        time.sleep(3)
        label = Label(root,
        			text ="Installing...")
        label.pack(pady = 10)
        
    btn = Button(root,
        			text ="Force Update",
                    command = forceup)
    btn.pack(pady = 19)

    root.mainloop()
def help1():

    class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.browser = QWebEngineView()
            self.browser.setUrl(QUrl('https://sway.office.com/dvEuM9D9HW0rxhXi?ref=Link'))
            self.setCentralWidget(self.browser)
            self.showMaximized()
            navbar = QToolBar()
            self.addToolBar(navbar)

            back_btn = QAction('Back', self)
            back_btn.triggered.connect(self.browser.back)
            navbar.addAction(back_btn)

            forward_btn = QAction('Forward', self)
            forward_btn.triggered.connect(self.browser.forward)
            navbar.addAction(forward_btn)

            reload_btn = QAction('Reload', self)
            reload_btn.triggered.connect(self.browser.reload)
            navbar.addAction(reload_btn)

            home_btn = QAction('Home', self)
            home_btn.triggered.connect(self.navigate_home)
            navbar.addAction(home_btn)

            self.url_bar = QLineEdit()
            self.url_bar.returnPressed.connect(self.navigate_to_url)
            navbar.addWidget(self.url_bar)

            self.browser.urlChanged.connect(self.update_url)

        def navigate_home(self):
            self.browser.setUrl(QUrl('https://www.google.com'))

        def navigate_to_url(self):
            url = self.url_bar.text()
            self.browser.setUrl(QUrl(url))

        def update_url(self, q):
            self.url_bar.setText(q.toString())
    app = QApplication(sys.argv)
    QApplication.setApplicationName('')
    window = MainWindow()
    app.exec_()
def help2():
    class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.browser = QWebEngineView()
            self.browser.setUrl(QUrl('https://support.microsoft.com/en-us/meetwindows11'))
            self.setCentralWidget(self.browser)
            self.showMaximized()
            navbar = QToolBar()
            self.addToolBar(navbar)

            back_btn = QAction('Back', self)
            back_btn.triggered.connect(self.browser.back)
            navbar.addAction(back_btn)

            forward_btn = QAction('Forward', self)
            forward_btn.triggered.connect(self.browser.forward)
            navbar.addAction(forward_btn)

            reload_btn = QAction('Reload', self)
            reload_btn.triggered.connect(self.browser.reload)
            navbar.addAction(reload_btn)

            home_btn = QAction('Home', self)
            home_btn.triggered.connect(self.navigate_home)
            navbar.addAction(home_btn)

            self.url_bar = QLineEdit()
            self.url_bar.returnPressed.connect(self.navigate_to_url)
            navbar.addWidget(self.url_bar)

            self.browser.urlChanged.connect(self.update_url)

        def navigate_home(self):
            self.browser.setUrl(QUrl('https://www.google.com'))

        def navigate_to_url(self):
            url = self.url_bar.text()
            self.browser.setUrl(QUrl(url))

        def update_url(self, q):
            self.url_bar.setText(q.toString())
    app = QApplication(sys.argv)
    QApplication.setApplicationName('')
    window = MainWindow()
    app.exec_()
def help3():
    class MainWindow(QMainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.browser = QWebEngineView()
            self.browser.setUrl(QUrl('https://clipchamp.com/watch/HtrQGLJCKE8'))
            self.setCentralWidget(self.browser)
            self.showMaximized()
            navbar = QToolBar()
            self.addToolBar(navbar)

            back_btn = QAction('Back', self)
            back_btn.triggered.connect(self.browser.back)
            navbar.addAction(back_btn)

            forward_btn = QAction('Forward', self)
            forward_btn.triggered.connect(self.browser.forward)
            navbar.addAction(forward_btn)

            reload_btn = QAction('Reload', self)
            reload_btn.triggered.connect(self.browser.reload)
            navbar.addAction(reload_btn)

            home_btn = QAction('Home', self)
            home_btn.triggered.connect(self.navigate_home)
            navbar.addAction(home_btn)

            self.url_bar = QLineEdit()
            self.url_bar.returnPressed.connect(self.navigate_to_url)
            navbar.addWidget(self.url_bar)

            self.browser.urlChanged.connect(self.update_url)

        def navigate_home(self):
            self.browser.setUrl(QUrl('https://www.google.com'))

        def navigate_to_url(self):
            url = self.url_bar.text()
            self.browser.setUrl(QUrl(url))

        def update_url(self, q):
            self.url_bar.setText(q.toString())
    app = QApplication(sys.argv)
    QApplication.setApplicationName('')
    window = MainWindow()
    app.exec_()
def helpo():
    root = Tk()
    root.title("Adven os")
    label = Label(root,
    			text ="Get help here", foreground='white')
    label.config(bg="black")
    label.pack(pady = 10)
    btn = Button(root,
    			text ="Help",
    			command = help1)
    btn.pack(pady = 19)
    btn = Button(root,
    			text ="Help With This Device",
    			command = help2)
    btn.pack(pady = 19)
    btn = Button(root,
    			text ="Help With Install",
    			command = help3)
    btn.pack(pady = 19)
def deve():
    # Import the tkinter module
    import tkinter

# Create the default window
    root = tkinter.Tk()
    root.title("Developer Mode")
    root.geometry('700x500')

# Create the list of options
    options_list = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Variable to keep track of the option
# selected in OptionMenu
    value_inside = tkinter.StringVar(root)

# Set the default value of the variable
    value_inside.set("Select an Option")

# Create the optionmenu widget and passing
# the options_list and value_inside to it.
    question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
    question_menu.pack()

# Function to print the submitted option-- testing purpose


    def print_answers():
        print("Selected Option: {}".format(value_inside.get()))
        return None


# Submit button
# Whenever we click the submit button, our submitted
# option is printed ---Testing purpose
    submit_button = tkinter.Button(root, text='Submit', command=print_answers)
    submit_button.pack()

    root.mainloop()


def sett():
    root = Tk()
    root.title("Adven os")
    btn = Button(root,
     			text ="Software Update",
     			command = softup)
    btn.pack(pady = 19)
    btn = Button(root,
    			text ="Change Sytem Image",
    			command = chimage)
    btn.pack(pady = 19)
    btn = Button(root,
    			text ="Get Help",
    			command = helpo)
    btn.pack(pady = 19)
    btn = Button(root,
    			text ="Engineering Mode",
    			command = eng)
    btn.pack(pady = 19)
    btn = Button(root,
    			text ="Developer Mode",
    			command = deve)
    btn.pack(pady = 19)
def web():

    class MainWindow(QMainWindow):

    	# constructor
    	def __init__(self, *args, **kwargs):
    		super(MainWindow, self).__init__(*args, **kwargs)

    		# creating a tab widget
    		self.tabs = QTabWidget()

    		# making document mode true
    		self.tabs.setDocumentMode(True)

    		# adding action when double clicked
    		self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

    		# adding action when tab is changed
    		self.tabs.currentChanged.connect(self.current_tab_changed)

    		# making tabs closeable
    		self.tabs.setTabsClosable(True)

    		# adding action when tab close is requested
    		self.tabs.tabCloseRequested.connect(self.close_current_tab)

    		# making tabs as central widget
    		self.setCentralWidget(self.tabs)

    		# creating a status bar
    		self.status = QStatusBar()

    		# setting status bar to the main window
    		self.setStatusBar(self.status)

    		# creating a tool bar for navigation
    		navtb = QToolBar("Navigation")

    		# adding tool bar tot he main window
    		self.addToolBar(navtb)

    		# creating back action
    		back_btn = QAction("Back", self)

    		# setting status tip
    		back_btn.setStatusTip("Back to previous page")

    		# adding action to back button
    		# making current tab to go back
    		back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())

    		# adding this to the navigation tool bar
    		navtb.addAction(back_btn)

    		# similarly adding next button
    		next_btn = QAction("Forward", self)
    		next_btn.setStatusTip("Forward to next page")
    		next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
    		navtb.addAction(next_btn)

    		# similarly adding reload button
    		reload_btn = QAction("Reload", self)
    		reload_btn.setStatusTip("Reload page")
    		reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
    		navtb.addAction(reload_btn)

    		# creating home action
    		home_btn = QAction("Home", self)
    		home_btn.setStatusTip("Go home")

    		# adding action to home button
    		home_btn.triggered.connect(self.navigate_home)
    		navtb.addAction(home_btn)

    		# adding a separator
    		navtb.addSeparator()

    		# creating a line edit widget for URL
    		self.urlbar = QLineEdit()

    		# adding action to line edit when return key is pressed
    		self.urlbar.returnPressed.connect(self.navigate_to_url)

    		# adding line edit to tool bar
    		navtb.addWidget(self.urlbar)

    		# similarly adding stop action
    		stop_btn = QAction("Stop", self)
    		stop_btn.setStatusTip("Stop loading current page")
    		stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
    		navtb.addAction(stop_btn)

    		# creating first tab
    		self.add_new_tab(QUrl('http://www.google.com'), 'Homepage')

    		# showing all the components
    		self.show()

    		# setting window title
    		self.setWindowTitle("Dynamic Web")

    	# method for adding new tab
    	def add_new_tab(self, qurl = None, label ="Blank"):

    		# if url is blank
    		if qurl is None:
    			# creating a google url
    			qurl = QUrl('http://www.google.com')

    		# creating a QWebEngineView object
    		browser = QWebEngineView()

    		# setting url to browser
    		browser.setUrl(qurl)

    		# setting tab index
    		i = self.tabs.addTab(browser, label)
    		self.tabs.setCurrentIndex(i)

    		# adding action to the browser when url is changed
    		# update the url
    		browser.urlChanged.connect(lambda qurl, browser = browser:
    								self.update_urlbar(qurl, browser))

    		# adding action to the browser when loading is finished
    		# set the tab title
    		browser.loadFinished.connect(lambda _, i = i, browser = browser:
    									self.tabs.setTabText(i, browser.page().title()))

    	# when double clicked is pressed on tabs
    	def tab_open_doubleclick(self, i):

    		# checking index i.e
    		# No tab under the click
    		if i == -1:
    			# creating a new tab
    			self.add_new_tab()

    	# when tab is changed
    	def current_tab_changed(self, i):

    		# get the curl
    		qurl = self.tabs.currentWidget().url()

    		# update the url
    		self.update_urlbar(qurl, self.tabs.currentWidget())

    		# update the title
    		self.update_title(self.tabs.currentWidget())

    	# when tab is closed
    	def close_current_tab(self, i):

    		# if there is only one tab
    		if self.tabs.count() < 2:
    			# do nothing
    			return

    		# else remove the tab
    		self.tabs.removeTab(i)

    	# method for updating the title
    	def update_title(self, browser):

    		# if signal is not from the current tab
    		if browser != self.tabs.currentWidget():
    			# do nothing
    			return

    		# get the page title
    		title = self.tabs.currentWidget().page().title()

    		# set the window title
    		self.setWindowTitle("% s - Dynamic Web" % title)

    	# action to go to home
    	def navigate_home(self):

    		# go to google
    		self.tabs.currentWidget().setUrl(QUrl("http://www.google.com"))

    	# method for navigate to url
    	def navigate_to_url(self):

    		# get the line edit text
    		# convert it to QUrl object
    		q = QUrl(self.urlbar.text())

    		# if scheme is blank
    		if q.scheme() == "":
    			# set scheme
    			q.setScheme("http")

    		# set the url
    		self.tabs.currentWidget().setUrl(q)

    	# method to update the url
    	def update_urlbar(self, q, browser = None):

    		# If this signal is not from the current tab, ignore
    		if browser != self.tabs.currentWidget():

    			return

    		# set text to the url bar
    		self.urlbar.setText(q.toString())

    		# set cursor position
    		self.urlbar.setCursorPosition(0)

    # creating a PyQt5 application
    app = QApplication(sys.argv)

    # setting name to the application
    app.setApplicationName("Geek PyQt5")

    # creating MainWindow object
    window = MainWindow()

    # loop
    app.exec_()
def adv():
    root = Tk()
    root.title("Av Ai")

    BG_GRAY = "#ABB2B9"
    BG_COLOR = "#17202A"
    TEXT_COLOR = "#EAECEE"

    FONT = "Helvetica 14"
    FONT_BOLD = "Helvetica 13 bold"

    # Send function
    def send():
        send = "You -> " + e.get()
        txt.insert(END, "\n" + send)

        user = e.get().lower()

        if (user == "hello"):
            txt.insert(END, "\n" + "Av Ai -> Hi there, how can I help?")

        elif (user == "hi" or user == "hii" or user == "hiiii"):
            txt.insert(END, "\n" + "Av Ai -> What can I do for you?")

        elif (user == "how are you"):
            txt.insert(END, "\n" + "Av Ai -> fine! and you")

        elif (user == "fine" or user == "i am good" or user == "i am doing good"):
            txt.insert(END, "\n" + "Av Ai -> Great! how can I help you.")

        elif (user == "thanks" or user == "thank you" or user == "now its my time"):
            txt.insert(END, "\n" + "Av Ai -> My pleasure !")

        elif (user == "what do you sell" or user == "what kinds of items are there" or user == "have you something"):
            txt.insert(END, "\n" + "Av Ai -> We have coffee and tea")

        elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
            txt.insert(
    			END, "\n" + "Av Ai -> What did the buffalo say when his son left for college? Bison.! ")

        elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
            txt.insert(END, "\n" + "Av Ai -> Have a nice day!")
            
        elif (user == "directions to home" or user == "home" or user == "to home"):
            txt.insert(END, "\n" + "Av Ai -> Getting directions. Go to https://www.geeksforgeeks.org/gui-chat-application-using-tkinter-in-python/")
       
        else:
            txt.insert(END, "\n" + "Av Ai -> Sorry! I didn't understand that")

        e.delete(0, END)


    lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
    	row=0)

    txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
    txt.grid(row=1, column=0, columnspan=2)

    scrollbar = Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)

    e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
    e.grid(row=2, column=0)

    send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
    			command=send).grid(row=2, column=1)
def jk():
    root= Tk()
    root.title("Adven os")
    btn = Button(root,
    			text ="Writer app",
    			command = writew)
    btn.pack(pady = 19)
    btn = Button(root,
    			text ="Contacts",
    			command = contacta)
    btn.pack(pady = 19)
    btn = Button(root,
    			text ="Av Ai",
    			command = adv)
    btn.pack(pady = 19)
    btn = Button(root,
     			text ="Computer",
     			command = shut)
    btn.pack(pady = 19)
    btn = Button(root,
     			text ="View Files",
     			command = fiopen)
    btn.pack(pady = 19)
    btn = Button(root,
     			text ="Sytem Prefrences",
     			command = sett)
    btn.pack(pady = 19)
    btn = Button(root,
     			text ="Dynamic Web",
     			command = web)
    btn.pack(pady = 19)


#Set the geometry of frame
root.geometry("600x250")

photo = PhotoImage(file = r"34.png")

Button(root,image= photo, text= "Button-3",height=50, width=50, command= jk).pack(side = LEFT, anchor=S, padx=[0,5])

root.mainloop()