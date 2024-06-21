import pandas as pd

def fetch_lagrange_time_values(dsbutton1, dsbutton3, freqbutton1, freqbutton2, freqbutton3):
    if(dsbutton1== 'sunken' and freqbutton1== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Time.xlsx', sheet_name=0)
    if(dsbutton1== 'sunken' and freqbutton2== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Time.xlsx', sheet_name=2)
    if(dsbutton1== 'sunken' and freqbutton3== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Time.xlsx', sheet_name=4)
    if(dsbutton3== 'sunken' and freqbutton1== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Time.xlsx', sheet_name=1)
    if(dsbutton3== 'sunken' and freqbutton2== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Time.xlsx', sheet_name=3)
    if(dsbutton3== 'sunken' and freqbutton3== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Time.xlsx', sheet_name=5)
    return data_points
    
def fetch_FGG_time_values(dsbutton1, dsbutton3, freqbutton1, freqbutton2, freqbutton3):
    if(dsbutton1== 'sunken' and freqbutton1== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Time.xlsx', sheet_name=0)
    if(dsbutton1== 'sunken' and freqbutton2== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Time.xlsx', sheet_name=2)
    if(dsbutton1== 'sunken' and freqbutton3== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Time.xlsx', sheet_name=4)
    if(dsbutton3== 'sunken' and freqbutton1== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Time.xlsx', sheet_name=1)
    if(dsbutton3== 'sunken' and freqbutton2== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Time.xlsx', sheet_name=3)
    if(dsbutton3== 'sunken' and freqbutton3== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Time.xlsx', sheet_name=5)
    return data_points

def fetch_lagrange_energy_values(dsbutton1, dsbutton3, freqbutton1, freqbutton2, freqbutton3):
    if(dsbutton1== 'sunken' and freqbutton1== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Energy.xlsx', sheet_name=0)
    if(dsbutton1== 'sunken' and freqbutton2== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Energy.xlsx', sheet_name=2)
    if(dsbutton1== 'sunken' and freqbutton3== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Energy.xlsx', sheet_name=4)
    if(dsbutton3== 'sunken' and freqbutton1== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Energy.xlsx', sheet_name=1)
    if(dsbutton3== 'sunken' and freqbutton2== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Energy.xlsx', sheet_name=3)
    if(dsbutton3== 'sunken' and freqbutton3== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Energy.xlsx', sheet_name=5)
    return data_points

def fetch_FGG_energy_values(dsbutton1, dsbutton3, freqbutton1, freqbutton2, freqbutton3):
    if(dsbutton1== 'sunken' and freqbutton1== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Energy.xlsx', sheet_name=0)
    if(dsbutton1== 'sunken' and freqbutton2== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Energy.xlsx', sheet_name=2)
    if(dsbutton1== 'sunken' and freqbutton3== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Energy.xlsx', sheet_name=4)
    if(dsbutton3== 'sunken' and freqbutton1== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Energy.xlsx', sheet_name=1)
    if(dsbutton3== 'sunken' and freqbutton2== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Energy.xlsx', sheet_name=3)
    if(dsbutton3== 'sunken' and freqbutton3== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Energy.xlsx', sheet_name=5)
    return data_points