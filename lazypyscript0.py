from tkinter import*
from tkinter import messagebox
import socket, requests, webbrowser, os
from ip2geotools.databases.noncommercial import DbIpCity
from bs4 import BeautifulSoup

def commandLineConsole(): 
    if ip.get() == "":
        messagebox.showinfo("No INPUT", "INSERT A REAL DOMAIN NAME WITHOUT https://www LIKE google.com")
    else: 
        try:
            your_ip()
            ip_list()
            ip_lookup()
            website_header()
            geo_tool()
        except:
            pass

def your_ip():
    try:
        a = a = "\n\n[+][+][+][+] WEBSITE IP ADDRESS [+][+][+][+]\n\n"
        s = socket.gethostbyname(ip.get())
        var1 = str.upper(ip.get())+ ("\t") + ("IP ADDRESS:") + s + ("\n")
        commandLine.insert(END, a)
        commandLine.insert(END, var1)
    except:
        err = ("THIS DOMAIN NAME DOESN'T EXIST") + ("\n")
        commandLine.insert(END, err)
        messagebox.showerror("ERROR", "THIS DOMAIN NAME DOESN'T EXIST")
    
     
def ip_list():
    try:
        a = "\n\n[+][+][+][+] LIST OF IP FOR YOUR DOMAIN [+][+][+][+]\n\n"
        sx = socket.gethostbyname(ip.get())
        s = str(socket.gethostbyname_ex(sx)) 
        commandLine.insert(END, a)
        commandLine.insert(END, s)
    except:
        ip_list_err = ("NO IP LIST TO SHOW") + ("\n")
        commandLine.insert(END, ip_list_err)
        
def ip_lookup():
    try:
        a = "\n\n[+][+][+][+] WHOIS LOOKUP [+][+][+][+]\n\n"
        url = "https://www.ipvoid.com/whois/"
        hosty = str(ip.get())
        myobj = {'host': hosty}
        x = requests.post(url, data = myobj)
        soup = BeautifulSoup(x.text, 'html.parser')
        commandLine.insert(END, a)
        commandLine.insert(END, soup.textarea)
    except:
        ip_lookup_err = "CANNOT ACCESS IPVOID"
        commandLine.insert(END, ip_lookup_err)
        
def website_header():
    try:
        a = "\n\n[+][+][+][+] WEBSITE HEADER [+][+][+][+]\n\n"
        x = requests.head("https://"+ ip.get()) 
        commandLine.insert(END, a)
        commandLine.insert(END, x.headers)
    except:
        header_err = "COULD NOT GET THE WEBSITE'S HEADER"
        commandLine.insert(END, header_err)
        
def geo_tool():
    try:
        a = "\n\n[+][+][+][+] GEOLOCATION [+][+][+][+]\n\n"
        s = socket.gethostbyname(ip.get())
        response = DbIpCity.get(s, api_key='free')
        commandLine.insert(END, a)
        commandLine.insert(END, response)
    except:
        geo_err = "GEOLOCATION TOOL IS NOT WORKING"
        commandLine.insert(END, geo_err)
        
def open_goo_map():
    try:
        s = socket.gethostbyname(ip.get())
        response = DbIpCity.get(s, api_key='free')
        gMap = "https://www.google.com/maps/search/?api=1&query=" + str(response.latitude) + "," + str(response.longitude)
        webbrowser.open(gMap) #open google map on your default webbrowser
    except:
        open_goo_err = "GEOLOCATION TOOL IS NOT WORKING"
        commandLine.insert(END, open_goo_err)

def ipvoid_website(url,a):
    try:
        hosty = str(ip.get())
        myobj = {'host': hosty}
        x = requests.post(url, data = myobj)
        soup = BeautifulSoup(x.text, 'html.parser')
        commandLine.insert(END, a)
        commandLine.insert(END, soup.textarea)
    except:
        ip_lookup_err = "CANNOT ACCESS IPVOID"
        commandLine.insert(END, ip_lookup_err)
        
def mx_lookup():
    url = "https://www.ipvoid.com/mx-lookup/"
    a = "\n\n[+][+][+][+] MX LOOKUP [+][+][+][+]\n\n"
    ipvoid_website(url,a)
    
def traceroute():
    url = "https://www.ipvoid.com/traceroute/"
    a = "\n\n[+][+][+][+] TRACEROUTE [+][+][+][+]\n\n"
    ipvoid_website(url,a)
    
def ping_lookup():
    url = "https://www.ipvoid.com/ping/"
    a = "\n\n[+][+][+][+] PING LOOKUP [+][+][+][+]\n\n"
    ipvoid_website(url,a)
    
def hosting_lookup():
    url = "https://www.ipvoid.com/who-is-hosting-a-website/"
    a = "\n\n[+][+][+][+] HOSTING LOOKUP [+][+][+][+]\n\n"
    ipvoid_website(url,a)
    

root = Tk()
root.resizable(0,0)# removes the max button
root.title("LazyPyScript v0.1.0")
root.configure(background="#090909")
# root.iconbitmap('C://...//skull.ico')
#variable for ip
ip = StringVar()
label1 = Label(root, text="Domain Like: google.com", background= "#090909", foreground = "#00ff00")
entry1 = Entry(root ,background = "#2f2f2f", foreground = "#00ff00", textvariable = ip)
button1 = Button(root, text="GET IP", background= "#090909", foreground = "#00ff00", command = commandLineConsole)
frame1 = Frame(root)
commandLine = Text(frame1, height = 15, width = 70 ,background = "#2f2f2f", foreground = "#00ff00")
scrollbar = Scrollbar(frame1, command=commandLine.yview)
label2 = Label(root, text = "ZOKIKISYSTEM", background= "#090909", foreground = "#00ff00")

button2 = Button(root, text="WEB MAP", background= "#090909", foreground = "#00ff00", command = open_goo_map)
button3 = Button(root, text="MX LOOKUP", background= "#090909", foreground = "#00ff00", command = mx_lookup)
button4 = Button(root, text="TRACEROUTE", background= "#090909", foreground = "#00ff00", command = traceroute)
button5 = Button(root, text="PING LOOKUP", background= "#090909", foreground = "#00ff00", command = ping_lookup)
button6 = Button(root, text="HOSTING LOOKUP", background= "#090909", foreground = "#00ff00", command = hosting_lookup)

label1.pack()
entry1.pack()
button1.pack()
frame1.pack()
scrollbar.pack(side="right", fill=Y)
commandLine.pack()
commandLine['yscrollcommand'] = scrollbar.set

button2.pack(padx=5, pady=15, side=LEFT)
button3.pack(padx=5, pady=15, side=LEFT)
button4.pack(padx=5, pady=15, side=LEFT)
button5.pack(padx=5, pady=15, side=LEFT)
button6.pack(padx=5, pady=15, side=LEFT)

label2.pack(side=BOTTOM)
root.mainloop()