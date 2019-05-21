import requests
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
#api key = 4fbdb839ea039705de57736d6c9b33a1

class forcast:
    date = []
    temp = []
    hum = []
    weather = []
    des = []
    wind = []
    code=''
    cont=''
    def __init__(self,city):
        self.city=city
        #print("main city ",self.city)
    def getData(self):
        try:
            self.response = requests.get("http://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&APPID=4fbdb839ea039705de57736d6c9b33a1".format(self.city))
            print("Response is",self.response.text)
        except requests.exceptions.ConnectionError:
            tkinter.messagebox.showinfo("Alert", "Connection error ")
        self.json = self.response.json()
        self.code = self.json["cod"]

        if self.code == "404":
            tkinter.messagebox.showinfo("Alert", "City Not Found")
        elif self.code =="202":
            pass
        elif self.code == '400':
            tkinter.messagebox.showinfo("Alert", "Please enter the city name")
        self.cont = self.json["city"]["country"]
        self.list = self.json["list"]

        for data in self.list:
            self.date.append(data["dt_txt"])
            self.temp.append(data["main"]["temp"])
            self.hum.append(data["main"]["humidity"])
            self.weather.append(data["weather"][0]["main"])
            self.des.append(data["weather"][0]["description"])
            self.wind.append(data["wind"]["speed"])


    def showData(self):
        print(self.date)
        print("Current Temperaute - ", self.temp, "C")
        print("humidity - ",self.hum)
        print("weather - ", self.weather)
        print("description - ", self.des)
        print("wind speed - ", self.wind)

class GUI(forcast):

    def __init__(self,master):
        self.city=''

        self.cityimg = PhotoImage(file="city.png")
        self.cityimg = self.cityimg.subsample(8,8)
        self.img = PhotoImage(file="img_183020.png")
        self.img = self.img.subsample(30,30)
        self.title = Label(master,text="Weather Forecasting", font=("Helvetica", 30, "bold"), foreground='yellow', bg='#33E6FF')
        self.title.grid(row=0,column=2,columnspan=5)
        self.City = Label(master,text="Enter city name", font=("Helvetica", 18, "bold"), bg="#33E6FF")
        self.City.grid(row=1,column=4,rowspan=2)
        self.City.config(image=self.cityimg, compound=RIGHT)
        self.entryCity = ttk.Combobox(master, font=("Helvetica", 8, "bold"), textvariable = self.city)
        self.entryCity['values']=()
        #self.entryCity = Entry(master, font=("Helvetica", 8, "bold"))
        self.entryCity.grid(row=3,column=4)
        self.button = Button(master,text="Submit",command=self.onClick,pady=5,font=("Helvetica",10,"bold"),bg="yellow")
        self.button.grid(row=4,column=4,rowspan=2)
        self.button.config(image=self.img,compound=RIGHT)
        self.button.bind("<Enter>", self.on_enter)
        self.button.bind("<Leave>", self.on_leave)

    def on_enter(self,e):
        self.button['background'] = 'green'

    def on_leave(self,e):
        self.button['background'] = 'yellow'


    def onClick(self):
        self.city = self.entryCity.get().title()

        f=forcast(self.city)
        g.getData()
        #g.showData()
        if self.code=="200":
            g.disp(root)
            #self.entryCity['values'] = self.entryCity['values'] + (self.city,)
            if self.city in self.entryCity['values']:
                pass
            else:
                self.entryCity['values'] = self.entryCity['values'] + (self.city,)

        self.date.clear()
        self.temp.clear()
        self.hum.clear()
        self.weather.clear()
        self.des.clear()
        self.wind.clear()

    def disp(self,master):
        if self.code =="200":
            self.frame = Frame(root,width=700,height=60,relief=SUNKEN,pady=10,padx=10,background="#33E6FF")
            self.frame.grid(row=6,column=4)

            self.sun = PhotoImage(file="sun.png")
            self.sun = self.sun.subsample(20, 20)
            self.cloud = PhotoImage(file="cloud.png")
            self.cloud = self.cloud.subsample(20, 20)
            self.rain = PhotoImage(file="rain.png")
            self.rain = self.rain.subsample(20, 20)
            self.snowing = PhotoImage(file="snowing.png")
            self.snowing = self.snowing.subsample(20, 20)
            self.celsius = PhotoImage(file="celsius.png")
            self.celsius = self.celsius.subsample(25, 25)

            self.lblCity = Label(self.frame, text="City", width=13, bg='#FFDA33',font=("Arial",10,"bold"))
            self.lblCity.grid(row=0,column=2)
            self.lblCity = Label(self.frame, text=self.city+"("+self.cont+")", width=13, bd=2, bg='#FFDA33',font=("Arial",10,"bold"))
            self.lblCity.grid(row=0,column=3)
            self.lbldate = Label(self.frame, text="Date & Time", width=15,bd=2,relief=SUNKEN,bg='#FFDA33')
            self.lbldate.grid(row=1, column=0)
            self.lbltemp = Label(self.frame, text="Temprature", width=105,height=15,bd=2,relief=SUNKEN,bg='#FFDA33')
            self.lbltemp.grid(row=2, column=0)
            self.lbltemp.config(image=self.celsius, compound=RIGHT)
            self.lblhumd = Label(self.frame, text="Humidity", width=15,bd=2,relief=SUNKEN,bg='#FFDA33')
            self.lblhumd.grid(row=3, column=0)
            self.lblweat = Label(self.frame, text="Weather", width=15,bd=2,relief=SUNKEN,bg='#FFDA33')
            self.lblweat.grid(row=4, column=0)
            self.lbldescrip = Label(self.frame, text="Description", width=15,bd=2,relief=SUNKEN,bg='#FFDA33')
            self.lbldescrip.grid(row=5, column=0)
            self.lblwind = Label(self.frame, text="Wind(m/s)", width=15,bd=2,relief=SUNKEN,bg='#FFDA33')
            self.lblwind.grid(row=6, column=0)

            for i in range(1,6):
                self.lbldate = Label(self.frame, text=self.date[i-1], width=15,bd=1,relief=SUNKEN,bg='yellow')
                self.lbldate.grid(row=1, column=i)
            for j in range(1,6):
                self.lbltemp = Label(self.frame, text=self.temp[j-1], width=15,bd=1,relief=SUNKEN,bg='yellow')
                self.lbltemp.grid(row=2, column=j)
            for j in range(1, 6):
                self.lblhumd = Label(self.frame, text=self.hum[j-1], width=15,bd=1,relief=SUNKEN,bg='yellow')
                self.lblhumd.grid(row=3, column=j)
            for i in range(1, 6):
                self.lblweat = Label(self.frame, text=self.weather[i-1],width=105,height=20,bd=1,relief=SUNKEN,bg='yellow')
                self.lblweat.grid(row=4, column=i)
                if self.weather[i-1] == 'Clear':
                    self.lblweat.config(image=self.sun, compound=RIGHT)
                elif self.weather[i-1] == 'Clouds':
                    self.lblweat.config(image=self.cloud, compound=RIGHT)
                elif self.weather[i-1] == 'Rain':
                    self.lblweat.config(image=self.rain, compound=RIGHT)
                elif self.weather[i-1] == 'Snow':
                    self.lblweat.config(image=self.snowing, compound=RIGHT)
                else:
                    self.lblweat.config()
            for i in range(1,6):
                self.lbldescrip = Label(self.frame, text=self.des[i-1], width=15,bd=1,relief=SUNKEN,bg='yellow')
                self.lbldescrip.grid(row=5, column=i)
            for i in range(1,6):
                self.lblwind = Label(self.frame, text=self.wind[i-1], width=15,bd=1,relief=SUNKEN,bg='yellow')
                self.lblwind.grid(row=6, column=i)
        elif self.code == "404":
            tkinter.messagebox.showinfo("Alert", "City Not Found")
root=Tk()
root.title("Weather Forecasting")
root.config(background="#33E6FF",padx=100,pady=100)
g = GUI(root)
root.resizable(width=False,height=False)
root.wm_iconbitmap("W.ico")
root.mainloop()
