from tkinter import *
from tkinter import ttk

import  requests
def data_get():
   city=city_name.get()


#city_name="jodhpur"
   data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"").json()
#print(data)
   w_lable1.config(text=data["weather"][0]["main"])
   wb_lable1.config(text=data["weather"][0]["description"])
   temp_lable1.config(text=str(int((data["main"]["temp"])-273.15)))
   per_lable1.config(text=data["main"]["pressure"])
   vis_lable1.config(text=str(int((((data["visibility"])/10000)*100))))
   hum_lable1.config(text=data["main"]["humidity"])

win=Tk()    #window

win.title("Weather App")

win.config(bg="skyblue")
win.geometry("600x870") 

city_name=StringVar()

name_lable=Label(win,text="Weather App",
font=("Time New Roman",30,"bold"))
name_lable.place(x=25,y=50,height=50,width=450)

list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh",
           "Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand"
           ,"Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya",
           "Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu",
           "Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal",
           "Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli",
           "Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]


com=ttk.Combobox(win,text="Weather App",values=list_name,
font=("Time New Roman",20,"bold"),textvariable=city_name)

com.place(x=25,y=120,height=50,width=450)

w_lable=Label(win,text="Weather Climate",
font=("Time New Roman",15))
w_lable.place(x=25,y=260,height=50,width=210)

w_lable1=Label(win,text="",
font=("Time New Roman",20))
w_lable1.place(x=250,y=260,height=50,width=210)

wb_lable=Label(win,text="Weather Description",
font=("Time New Roman",16))
wb_lable.place(x=25,y=330,height=50,width=210)

wb_lable1=Label(win,text="",
font=("Time New Roman",16))
wb_lable1.place(x=250,y=330,height=50,width=210)

temp_lable=Label(win,text="Temperature",
font=("Time New Roman",14))
temp_lable.place(x=25,y=400,height=50,width=210)

temp_lable1=Label(win,text="",
font=("Time New Roman",14))
temp_lable1.place(x=250,y=400,height=50,width=210)


per_lable=Label(win,text="Pressure",
font=("Time New Roman",16))
per_lable.place(x=25,y=470,height=50,width=210)

per_lable1=Label(win,text="",
font=("Time New Roman",16))
per_lable1.place(x=250,y=470,height=50,width=210)

vis_lable=Label(win,text="visibility",
font=("Time New Roman",16))
vis_lable.place(x=25,y=540,height=50,width=210)

vis_lable1=Label(win,text="",
font=("Time New Roman",16))
vis_lable1.place(x=250,y=540,height=50,width=210)

hum_lable=Label(win,text="humidity",
font=("Time New Roman",16))
hum_lable.place(x=25,y=610,height=50,width=210)

hum_lable1=Label(win,text="",
font=("Time New Roman",16))
hum_lable1.place(x=250,y=610,height=50,width=210)

done_button=Button(win,text="Done",
     font=("Time New Roman",20,"bold"),command=data_get)

done_button.place(y=190,height=50,width=100,x=200)


win.mainloop()
