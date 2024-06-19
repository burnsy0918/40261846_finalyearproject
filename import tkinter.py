import tkinter
from tkinter import *
from tkinter.ttk import *
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import fetch_values

def toggle(Button):

    if Button.config('relief')[-1] == 'sunken':
        Button.config(relief="raised")
        Button.config(background=colour3)
        Button.config(foreground=colour4)
    else:
        Button.config(relief="sunken")
        Button.config(background=colour1)
        Button.config(foreground=colour3)
        
def dstoggle(Button):
    dsbutton1.config(relief='raised')
    dsbutton1.config(background=colour3)
    dsbutton1.config(foreground=colour4)
    dsbutton2.config(relief='raised')
    dsbutton2.config(background=colour3)
    dsbutton2.config(foreground=colour4)
    dsbutton3.config(relief='raised')
    dsbutton3.config(background=colour3)
    dsbutton3.config(foreground=colour4)
    Button.config(relief='sunken')
    Button.config(background=colour1)
    Button.config(foreground=colour3)

def freqtoggle(Button):
    freqbutton1.config(relief='raised')
    freqbutton1.config(background=colour3)
    freqbutton1.config(foreground=colour4)
    freqbutton2.config(relief='raised')
    freqbutton2.config(background=colour3)
    freqbutton2.config(foreground=colour4)
    freqbutton3.config(relief='raised')
    freqbutton3.config(background=colour3)
    freqbutton3.config(foreground=colour4)
    Button.config(relief='sunken')
    Button.config(background=colour1)
    Button.config(foreground=colour3)
    
def updategraph():
    for art in list(figure_plot.lines):
        art.remove()
    if(figure_plot.get_legend()!= None):
        figure_plot.get_legend().remove()
    
    if(button1['relief']== 'sunken'):
        data_points = fetch_values.fetch_algo1_values(dsbutton1['relief'], dsbutton2['relief'], dsbutton3['relief'],
                                        freqbutton1['relief'], freqbutton2['relief'], freqbutton3['relief'])
        dataframe = pd.DataFrame(data_points)
        dataframe = dataframe[['x', 'y']].groupby('x').sum()
        dataframe.plot(kind='line', legend=TRUE, ax=figure_plot,
            color='r', marker='o', fontsize=10)
        
    if(button2['relief']== 'sunken'):
        data_points = fetch_values.fetch_algo2_values(dsbutton1['relief'], dsbutton2['relief'], dsbutton3['relief'],
                                        freqbutton1['relief'], freqbutton2['relief'], freqbutton3['relief'])
        dataframe = pd.DataFrame(data_points)
        dataframe = dataframe[['x', 'y']].groupby('x').sum()
        dataframe.plot(kind='line', legend=TRUE, ax=figure_plot,
            color='b', marker='o', fontsize=10)
        
    if(button3['relief']== 'sunken'):
        data_points = fetch_values.fetch_algo3_values(dsbutton1['relief'], dsbutton2['relief'], dsbutton3['relief'],
                                        freqbutton1['relief'], freqbutton2['relief'], freqbutton3['relief'])
        dataframe = pd.DataFrame(data_points)
        dataframe = dataframe[['x', 'y']].groupby('x').sum()
        dataframe.plot(kind='line', legend=TRUE, ax=figure_plot,
            color='g', marker='o', fontsize=10)
        
    line_graph.draw()

root = tkinter.Tk()

root.geometry("700x600")
root.configure(background='#7A7776')
# Code to add widgets will go here...

colour1 = '#020f12'
colour2 = '#05d7ff'
colour3 = '#65e7ff'
colour4 = 'BLACK'

chart_frame = tkinter.Frame(root, bg = '#7A7776', pady=40, height=190)
chart_frame.pack(fill=tkinter.BOTH, expand=TRUE)

figure = plt.Figure(figsize=(5,4), dpi=100)
#rows, cols, index position
figure_plot = figure.add_subplot(1, 1, 1)
figure_plot.set_ylabel('y') 
line_graph = FigureCanvasTkAgg(figure, chart_frame)
line_graph.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH)
figure_plot.set_title('Line Graph')
#canvas = tkinter.Canvas(chart_frame, width=400, height=300, bg='white')
#canvas.pack()

algo_frame = tkinter.Frame(root, bg = '#7A7776', pady=40, height=100)
algo_frame.pack(fill=tkinter.BOTH, expand=TRUE)
algo_frame.columnconfigure(1, weight=1)
button1 = tkinter.Button(
    algo_frame,
    background=colour3,
    foreground=colour4,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness = 5,
    highlightcolor = 'white',
    highlightbackground = 'white',
    height=3,
    width=16,
    border=8,
    cursor='hand1',
    text='Algorithm 1',
    relief="raised",
    command= lambda: [toggle(button1), updategraph()]
)
button1.grid(row=0, column=0)
#button1.pack()
#button1.place(x=100)

button2 = tkinter.Button(
    algo_frame,
    background=colour3,
    foreground=colour4,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness = 5,
    highlightcolor = 'white',
    highlightbackground = 'white',
    height=3,
    width=16,
    border=8,
    cursor='hand1',
    text='Algorithm 2',
    relief="raised",
    command=lambda: [toggle(button2), updategraph()]
)
button2.grid(row=0, column=1)
#button2.pack()
#button2.place(x=100)

button3 = tkinter.Button(
    algo_frame,
    background=colour3,
    foreground=colour4,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness = 5,
    highlightcolor = 'white',
    highlightbackground = 'white',
    height=3,
    width=16,
    border=8,
    cursor='hand1',
    text='Algorithm 3',
    relief="raised",
    command=lambda: [toggle(button3), updategraph()]
)
button3.grid(row=0, column=2)
#button3.pack()



dataset_frame = tkinter.Frame(root, bg = '#7A7776', pady=40, height=5)
dataset_frame.pack()
dataset_frame.columnconfigure(1, weight=1)
dsbutton1 = tkinter.Button(
    dataset_frame,
    background=colour1,
    foreground=colour3,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness = 5,
    highlightcolor = 'white',
    highlightbackground = 'white',
    height=1,
    width=12,
    border=0,
    cursor='hand1',
    text='Algorithm 1',
    relief="sunken",
    command= lambda: [dstoggle(dsbutton1), updategraph()]
)
dsbutton1.grid(row=0, column=0, padx=(100,10))
#button1.pack()
#button1.place(x=100)

dsbutton2 = tkinter.Button(
    dataset_frame,
    background=colour3,
    foreground=colour4,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness = 5,
    highlightcolor = 'white',
    highlightbackground = 'white',
    height=1,
    width=12,
    border=0,
    cursor='hand1',
    text='Algorithm 2',
    relief="raised",
    command=lambda: [dstoggle(dsbutton2), updategraph()]
)
dsbutton2.grid(row=0, column=1)
#button2.pack()
#button2.place(x=100)

dsbutton3 = tkinter.Button(
    dataset_frame,
    background=colour3,
    foreground=colour4,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness = 5,
    highlightcolor = 'white',
    highlightbackground = 'white',
    height=1,
    width=12,
    border=0,
    cursor='hand1',
    text='Algorithm 3',
    relief="raised",
    command=lambda: [dstoggle(dsbutton3), updategraph()]
)
dsbutton3.grid(row=0, column=2,  padx=(10,100))
#button3.pack()
freq_frame = tkinter.Frame(root, bg = '#7A7776', pady=40, height=5)
freq_frame.pack()
freq_frame.columnconfigure(1, weight=1)

freqbutton1 = tkinter.Button(
    freq_frame,
    background=colour1,
    foreground=colour3,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness = 5,
    highlightcolor = 'white',
    highlightbackground = 'white',
    height=1,
    width=12,
    border=0,
    cursor='hand1',
    text='Algorithm 1',
    relief="sunken",
    command= lambda: [freqtoggle(freqbutton1), updategraph()]
)
freqbutton1.grid(row=0, column=0, padx=(100,10))
#button1.pack()
#button1.place(x=100)

freqbutton2 = tkinter.Button(
    freq_frame,
    background=colour3,
    foreground=colour4,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness = 5,
    highlightcolor = 'white',
    highlightbackground = 'white',
    height=1,
    width=12,
    border=0,
    cursor='hand1',
    text='Algorithm 2',
    relief="raised",
    command=lambda: [freqtoggle(freqbutton2), updategraph()]
)
freqbutton2.grid(row=0, column=1)
#button2.pack()
#button2.place(x=100)

freqbutton3 = tkinter.Button(
    freq_frame,
    background=colour3,
    foreground=colour4,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness = 5,
    highlightcolor = 'white',
    highlightbackground = 'white',
    height=1,
    width=12,
    border=0,
    cursor='hand1',
    text='Algorithm 3',
    relief="raised",
    command=lambda: [freqtoggle(freqbutton3), updategraph()]
)
freqbutton3.grid(row=0, column=2,  padx=(10,100))
#b = Button(root,text = "Simple", style='W.TButton') 
#b.pack()  

root.mainloop()