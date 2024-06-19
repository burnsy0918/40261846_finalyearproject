import pandas as pd

def fetch_algo1_values(dsbutton1, dsbutton2, dsbutton3, freqbutton1, freqbutton2, freqbutton3):
    if(dsbutton1== 'sunken' and freqbutton1== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo1.xlsx', sheet_name=0)
    if(dsbutton1== 'sunken' and freqbutton2== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo1.xlsx', sheet_name=1)
    if(dsbutton1== 'sunken' and freqbutton3== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo1.xlsx', sheet_name=2)
    if(dsbutton2== 'sunken' and freqbutton1== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo1.xlsx', sheet_name=3)
    if(dsbutton2== 'sunken' and freqbutton2== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo1.xlsx', sheet_name=4)
    if(dsbutton2== 'sunken' and freqbutton3== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo1.xlsx', sheet_name=5)
    if(dsbutton3== 'sunken' and freqbutton1== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo1.xlsx', sheet_name=6)
    if(dsbutton3== 'sunken' and freqbutton2== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo1.xlsx', sheet_name=7)
    if(dsbutton3== 'sunken' and freqbutton3== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo1.xlsx', sheet_name=8)
    return data_points

def fetch_algo2_values(dsbutton1, dsbutton2, dsbutton3, freqbutton1, freqbutton2, freqbutton3):
    if(dsbutton1== 'sunken' and freqbutton1== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo2.xlsx', sheet_name=0)
    if(dsbutton1== 'sunken' and freqbutton2== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo2.xlsx', sheet_name=1)
    if(dsbutton1== 'sunken' and freqbutton3== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo2.xlsx', sheet_name=2)
    if(dsbutton2== 'sunken' and freqbutton1== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo2.xlsx', sheet_name=3)
    if(dsbutton2== 'sunken' and freqbutton2== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo2.xlsx', sheet_name=4)
    if(dsbutton2== 'sunken' and freqbutton3== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo2.xlsx', sheet_name=5)
    if(dsbutton3== 'sunken' and freqbutton1== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo2.xlsx', sheet_name=6)
    if(dsbutton3== 'sunken' and freqbutton2== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo2.xlsx', sheet_name=7)
    if(dsbutton3== 'sunken' and freqbutton3== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo2.xlsx', sheet_name=8)
    return data_points
    
def fetch_algo3_values(dsbutton1, dsbutton2, dsbutton3, freqbutton1, freqbutton2, freqbutton3):
    if(dsbutton1== 'sunken' and freqbutton1== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo3.xlsx', sheet_name=0)
    if(dsbutton1== 'sunken' and freqbutton2== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo3.xlsx', sheet_name=1)
    if(dsbutton1== 'sunken' and freqbutton3== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo3.xlsx', sheet_name=2)
    if(dsbutton2== 'sunken' and freqbutton1== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo3.xlsx', sheet_name=3)
    if(dsbutton2== 'sunken' and freqbutton2== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo3.xlsx', sheet_name=4)
    if(dsbutton2== 'sunken' and freqbutton3== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo3.xlsx', sheet_name=5)
    if(dsbutton3== 'sunken' and freqbutton1== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo3.xlsx', sheet_name=6)
    if(dsbutton3== 'sunken' and freqbutton2== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo3.xlsx', sheet_name=7)
    if(dsbutton3== 'sunken' and freqbutton3== 'sunken'):
        data_points= pd.read_excel('C:/Users/alibu/Documents/Project/Algo3.xlsx', sheet_name=8)
    return data_points