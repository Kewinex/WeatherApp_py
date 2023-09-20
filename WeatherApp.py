from tkinter import * 
from tkinter.ttk import *
import tkinter as tk
import time
 
window = Tk()
window.resizable(False, False)
window.title("Keweather app")
status = StringVar() 

def getWeather():
    newWindow = Toplevel(window)
    newWindow.resizable(False, False)
    newWindow.geometry("300x75")
    newWindow.title("Getting weather") 
       
    label = tk.Label(newWindow, textvariable=status)
    label.pack(pady = 5)
    
    progress = Progressbar(newWindow, orient = HORIZONTAL, length = 200, mode = 'determinate')
    progress.pack(pady = 5)  
     
    for x in range(1001):
        time.sleep(0.01)    
        progress['value'] = x/10
        if x == 0:
            status.set("Zjišťuji polohu")
        if x == 250:
            status.set("Připojuji se k satelitu")
        if x == 500:
            status.set("Analyzuji mraky")
        if x == 750:
            status.set("Shromažďování posledních informací")
        if x == 1000:
            newWindow.destroy()
            result = Toplevel(window)
            result.resizable(False, False)
            result.title("Result")
            label_r = tk.Label(result, text="Nevím, prostě se koukni z okna ¯\_(ツ)_/¯")
            label_r.pack(pady = 15, padx = 15)                
        newWindow.update()      
         
Button(window, text='Zjistit jaké počasí je momentálně venku.', command=getWeather).pack(pady = 10, padx=10)

mainloop() 