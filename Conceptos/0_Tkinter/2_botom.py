from tkinter import *
  
  
# create root window
root = Tk()                           
  
# frame inside root window
frame = Frame(root)                  
  
# geometry method
frame.pack()                          
  
# button inside frame which is 
# inside root
button = Button(frame, text ='Presioname')  

button1 = Button(frame,text='Ajustes y mas ')

button1.pack()
button.pack()                         
  
# Tkinter event loop
root.mainloop()    