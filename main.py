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

def typetoggle(Button):
    typebutton1.config(relief="raised")
    typebutton1.config(background=colour3)
    typebutton1.config(foreground=colour4)
    typebutton2.config(relief="raised")
    typebutton2.config(background=colour3)
    typebutton2.config(foreground=colour4)
    Button.config(relief="sunken")
    Button.config(background=colour1)
    Button.config(foreground=colour3)
        
def dstoggle(Button):
    dsbutton1.config(relief='raised')
    dsbutton1.config(background=colour3)
    dsbutton1.config(foreground=colour4)
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
    
def sourcetoggle(Button):
    sourcebutton1.config(relief='raised')
    sourcebutton1.config(background=colour3)
    sourcebutton1.config(foreground=colour4)
    sourcebutton2.config(relief='raised')
    sourcebutton2.config(background=colour3)
    sourcebutton2.config(foreground=colour4)
    Button.config(relief='sunken')
    Button.config(background=colour1)
    Button.config(foreground=colour3)
    
def updategraph():
    for art in list(figure_plot.lines):
        art.remove()
    if(figure_plot.get_legend()!= None):
        figure_plot.get_legend().remove()
    for text in list(figure_plot.texts):
        text.remove()
        
    last1=0
    last2=0
    
    if(typebutton1['relief']== 'sunken'):
        figure_plot.set_ylabel('Time (ms)')
        if(button1['relief']== 'sunken'):
            if(sourcebutton1['relief']=='sunken'):
                data_points = fetch_values.fetch_lagrange_time_values(dsbutton1['relief'], dsbutton3['relief'],
                                                freqbutton1['relief'], freqbutton2['relief'], freqbutton3['relief'])
            elif(sourcebutton2['relief']=='sunken'):
                data_points = fetch_values.fetch_lagrange_time_values_SQL(dsbutton1['relief'], dsbutton3['relief'],
                                                freqbutton1['relief'], freqbutton2['relief'], freqbutton3['relief'])
            dataframe = pd.DataFrame(data_points)
            dataframe = dataframe[['N', 'Time (ms)']].groupby('N').sum()
            dataframe.plot(kind='line', legend=TRUE, ax=figure_plot,
                color='r', marker='o', fontsize=10)
            avg_y =dataframe['Time (ms)'].mean()
            figure_plot.axhline(y=avg_y, color='r', linestyle='--')
            figure_plot.text(0.25, 0.95, f'Average y: {avg_y:2f}', verticalalignment='top', horizontalalignment='right',
                        transform=figure_plot.transAxes, color='r', fontsize=12)
            last1= dataframe['Time (ms)'].iloc[-1]
        
        
        if(button3['relief']== 'sunken'):
            if(sourcebutton1['relief']=='sunken'):
                data_points = fetch_values.fetch_FGG_time_values(dsbutton1['relief'], dsbutton3['relief'],
                                                freqbutton1['relief'], freqbutton2['relief'], freqbutton3['relief'])
            elif(sourcebutton2['relief']=='sunken'):
                data_points = fetch_values.fetch_FGG_time_values_SQL(dsbutton1['relief'], dsbutton3['relief'],
                                                freqbutton1['relief'], freqbutton2['relief'], freqbutton3['relief'])
            dataframe = pd.DataFrame(data_points)
            dataframe = dataframe[['N', 'Time (ms)']].groupby('N').sum()
            dataframe.plot(kind='line', legend=TRUE, ax=figure_plot,
                color='g', marker='o', fontsize=10)
            avg_y =dataframe['Time (ms)'].mean()
            figure_plot.axhline(y=avg_y, color='g', linestyle='--')
            figure_plot.text(0.25, 0.85, f'Average y: {avg_y:2f}', verticalalignment='top', horizontalalignment='right',
                        transform=figure_plot.transAxes, color='g', fontsize=12)
            last2= dataframe['Time (ms)'].iloc[-1]
            
    elif(typebutton2['relief']== 'sunken'):
        figure_plot.set_ylabel('Energy (V)x10^6')
        if(button1['relief']== 'sunken'):
            if(sourcebutton1['relief']=='sunken'):
                data_points = fetch_values.fetch_lagrange_energy_values(dsbutton1['relief'], dsbutton3['relief'],
                                                freqbutton1['relief'], freqbutton2['relief'], freqbutton3['relief'])
            elif(sourcebutton2['relief']=='sunken'):
                data_points = fetch_values.fetch_lagrange_energy_values_SQL(dsbutton1['relief'], dsbutton3['relief'],
                                                freqbutton1['relief'], freqbutton2['relief'], freqbutton3['relief'])
            dataframe = pd.DataFrame(data_points)
            dataframe = dataframe[['N', 'Energy (V)x10^6']].groupby('N').sum()
            dataframe.plot(kind='line', legend=TRUE, ax=figure_plot,
                color='r', marker='o', fontsize=10)
            avg_y =dataframe['Energy (V)x10^6'].mean()
            figure_plot.axhline(y=avg_y, color='r', linestyle='--')
            figure_plot.text(0.25, 0.95, f'Average y: {avg_y:2f}', verticalalignment='top', horizontalalignment='right',
                        transform=figure_plot.transAxes, color='r', fontsize=12)
            last1= dataframe['Energy (V)x10^6'].iloc[-1]
                
        if(button3['relief']== 'sunken'):
            if(sourcebutton1['relief']=='sunken'):
                data_points = fetch_values.fetch_FGG_energy_values(dsbutton1['relief'], dsbutton3['relief'],
                                                freqbutton1['relief'], freqbutton2['relief'], freqbutton3['relief'])
            elif(sourcebutton1['relief']=='sunken'):
                data_points = fetch_values.fetch_FGG_energy_values_SQL(dsbutton1['relief'], dsbutton3['relief'],
                                                freqbutton1['relief'], freqbutton2['relief'], freqbutton3['relief'])
            dataframe = pd.DataFrame(data_points)
            dataframe = dataframe[['N', 'Energy (V)x10^6']].groupby('N').sum()
            dataframe.plot(kind='line', legend=TRUE, ax=figure_plot,
                color='g', marker='o', fontsize=10)
            avg_y =dataframe['Energy (V)x10^6'].mean()
            figure_plot.axhline(y=avg_y, color='g', linestyle='--')
            figure_plot.text(0.25, 0.85, f'Average y: {avg_y:2f}', verticalalignment='top', horizontalalignment='right',
                        transform=figure_plot.transAxes, color='g', fontsize=12)
            last2= dataframe['Energy (V)x10^6'].iloc[-1]
        
    if (last1 > last2):
        figure_plot.set_ylim(0, last1 + 5)
    else:
        figure_plot.set_ylim(0, last2 + 5)
    line_graph.draw()

root = tkinter.Tk()

root.geometry("700x600")
root.configure(background='#7A7776')

colour1 = '#020f12'
colour2 = '#05d7ff'
colour3 = '#65e7ff'
colour4 = 'BLACK'

chart_frame = tkinter.Frame(root, bg = '#7A7776', pady=40, height=190)
chart_frame.pack(fill=tkinter.BOTH, expand=TRUE)

figure = plt.Figure(figsize=(5,4), dpi=100)
figure_plot = figure.add_subplot(1, 1, 1)
figure_plot.set_ylabel('Time (ms)') 
line_graph = FigureCanvasTkAgg(figure, chart_frame)
line_graph.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH)
figure_plot.set_title('Line Graph')

sourcebutton1 = tkinter.Button(
    chart_frame,
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
    text='Excel',
    relief="sunken",
    command= lambda: [sourcetoggle(sourcebutton1), updategraph()]
)
sourcebutton1.pack(side = "left")

sourcebutton2 = tkinter.Button(
    chart_frame,
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
    text='SQL',
    relief="raised",
    command=lambda: [sourcetoggle(sourcebutton2), updategraph()]
)
sourcebutton2.pack(side = "right")

algo_frame = tkinter.Frame(root, bg = '#7A7776', pady=40, height=100)
algo_frame.pack(fill=tkinter.BOTH, expand=TRUE)
algo_frame.columnconfigure(1, weight=1)
type_frame = tkinter.Frame(algo_frame, bg = '#7A7776')
type_frame.grid(row=0, column=1)
type_frame.columnconfigure(1, weight=1)
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
    text='Conventional Lagrance',
    relief="raised",
    command= lambda: [toggle(button1), updategraph()]
)
button1.grid(row=0, column=0)

typebutton1 = tkinter.Button(
    type_frame,
    background=colour1,
    foreground=colour3,
    activebackground=colour3,
    activeforeground=colour4,
    highlightthickness = 5,
    highlightcolor = 'white',
    highlightbackground = 'white',
    height=3,
    width=16,
    border=8,
    cursor='hand1',
    text='Time',
    relief="sunken",
    command=lambda: [typetoggle(typebutton1), updategraph()]
)
typebutton1.grid(row=0, column=0)

typebutton2 = tkinter.Button(
    type_frame,
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
    text='Energy',
    relief="raised",
    command=lambda: [typetoggle(typebutton2), updategraph()]
)
typebutton2.grid(row=0, column=1)

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
    text='Proposed FGG',
    relief="raised",
    command=lambda: [toggle(button3), updategraph()]
)
button3.grid(row=0, column=2)



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
    text='Grid',
    relief="sunken",
    command= lambda: [dstoggle(dsbutton1), updategraph()]
)
dsbutton1.grid(row=0, column=0, padx=(100,10))

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
    text='FFT',
    relief="raised",
    command=lambda: [dstoggle(dsbutton3), updategraph()]
)
dsbutton3.grid(row=0, column=2,  padx=(10,100))


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
    text='Low Precision',
    relief="sunken",
    command= lambda: [freqtoggle(freqbutton1), updategraph()]
)
freqbutton1.grid(row=0, column=0, padx=(100,10))

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
    text='Mid Precision',
    relief="raised",
    command=lambda: [freqtoggle(freqbutton2), updategraph()]
)
freqbutton2.grid(row=0, column=1)#

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
    text='High Precision',
    relief="raised",
    command=lambda: [freqtoggle(freqbutton3), updategraph()]
)
freqbutton3.grid(row=0, column=2,  padx=(10,100))

root.mainloop()