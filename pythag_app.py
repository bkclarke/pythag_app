# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 19:55:37 2022

@author: bonny
"""

# Python GUI Program to calculate 
# Area of a Triangle
# When base and height given
# www.EasyCodebook.com

from tkinter import *


def calculate_area():
	base = float(entry1.get())
	height = float(entry2.get())
	area = 1 / 2 * base * height 
	output_label.configure(text = ' Area of Triangle= {:.2f} ' .format(area))
	
main_window = Tk()
main_window.title('Python GUI TUTORIALS, www.EasyCodeBook.com ')

message_label1 = Label(text= 'Enter base: ' ,font=( ' Verdana ' , 18))
message_label2 = Label(text= ' Enter height: ' ,font=( ' Verdana ' , 18))
output_label = Label(font=( ' Verdana ' , 18), text='Area of Triangle is:')
entry1 = Entry(font=( ' Verdana ' , 18), width=6)
entry2 = Entry(font=( ' Verdana ' , 18), width=6)
calc_button = Button(text= ' Calculate Area ' , font=( ' Verdana ' , 16),command=calculate_area)

message_label1.grid(row=1, column=0)
entry1.grid(row=1, column=1)

message_label2.grid(row=2, column=0)
entry2.grid(row=2, column=1)

calc_button.grid(row=1, column=2, rowspan=2)
output_label.grid(row=3, column=0, columnspan=3)
mainloop()