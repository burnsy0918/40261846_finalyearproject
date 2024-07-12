import pandas as pd
import pyodbc
import logging 

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};Server=.\SQLEXPRESS;Database=master;TrustServerCertificate=yes;UID=sa;pwd=password')
#This python file will be used to fetch the data from the sources. It will check for what buttons have been selected,
#and fetch the requested data
        
def fetch_lagrange_time_values(dsbutton1, dsbutton3, precbutton1, precbutton2, precbutton3):
    if(dsbutton1== 'sunken' and precbutton1== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Time.xlsx', sheet_name=0)
    if(dsbutton1== 'sunken' and precbutton2== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Time.xlsx', sheet_name=2)
    if(dsbutton1== 'sunken' and precbutton3== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Time.xlsx', sheet_name=4)
    if(dsbutton3== 'sunken' and precbutton1== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Time.xlsx', sheet_name=1)
    if(dsbutton3== 'sunken' and precbutton2== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Time.xlsx', sheet_name=3)
    if(dsbutton3== 'sunken' and precbutton3== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Time.xlsx', sheet_name=5)
    return data_points
    
def fetch_FGG_time_values(dsbutton1, dsbutton3, precbutton1, precbutton2, precbutton3):
    if(dsbutton1== 'sunken' and precbutton1== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Time.xlsx', sheet_name=0)
    if(dsbutton1== 'sunken' and precbutton2== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Time.xlsx', sheet_name=2)
    if(dsbutton1== 'sunken' and precbutton3== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Time.xlsx', sheet_name=4)
    if(dsbutton3== 'sunken' and precbutton1== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Time.xlsx', sheet_name=1)
    if(dsbutton3== 'sunken' and precbutton2== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Time.xlsx', sheet_name=3)
    if(dsbutton3== 'sunken' and precbutton3== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Time.xlsx', sheet_name=5)
    return data_points

def fetch_lagrange_energy_values(dsbutton1, dsbutton3, precbutton1, precbutton2, precbutton3):
    if(dsbutton1== 'sunken' and precbutton1== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Energy.xlsx', sheet_name=0)
    if(dsbutton1== 'sunken' and precbutton2== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Energy.xlsx', sheet_name=2)
    if(dsbutton1== 'sunken' and precbutton3== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Energy.xlsx', sheet_name=4)
    if(dsbutton3== 'sunken' and precbutton1== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Energy.xlsx', sheet_name=1)
    if(dsbutton3== 'sunken' and precbutton2== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Energy.xlsx', sheet_name=3)
    if(dsbutton3== 'sunken' and precbutton3== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/Conventional Lagrange Energy.xlsx', sheet_name=5)
    return data_points

def fetch_FGG_energy_values(dsbutton1, dsbutton3, precbutton1, precbutton2, precbutton3):
    if(dsbutton1== 'sunken' and precbutton1== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Energy.xlsx', sheet_name=0)
    if(dsbutton1== 'sunken' and precbutton2== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Energy.xlsx', sheet_name=2)
    if(dsbutton1== 'sunken' and precbutton3== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Energy.xlsx', sheet_name=4)
    if(dsbutton3== 'sunken' and precbutton1== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Energy.xlsx', sheet_name=1)
    if(dsbutton3== 'sunken' and precbutton2== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Energy.xlsx', sheet_name=3)
    if(dsbutton3== 'sunken' and precbutton3== 'sunken'):
        data_points= pd.read_excel('40261846_finalyearproject/FGG Energy.xlsx', sheet_name=5)
    return data_points

def fetch_FGG_energy_values_SQL(dsbutton1, dsbutton3, precbutton1, precbutton2, precbutton3):
    if(dsbutton1== 'sunken' and precbutton1== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.FGGEnergySQLLowPrecisionGrid", cnxn)
    if(dsbutton1== 'sunken' and precbutton2== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.FGGEnergySQLMediumPrecisionGrid", cnxn)
    if(dsbutton1== 'sunken' and precbutton3== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.FGGEnergySQLHighPrecisionGrid", cnxn)
    if(dsbutton3== 'sunken' and precbutton1== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.FGGEnergySQLLowPrecisionFFT", cnxn)
    if(dsbutton3== 'sunken' and precbutton2== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.FGGEnergySQLMediumPrecisionFFT", cnxn)
    if(dsbutton3== 'sunken' and precbutton3== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.FGGEnergySQLHighPrecisionFFT", cnxn)
        
    if(not data_points.empty):
        logging.info('SQL fetch successful!')
    return data_points

def fetch_Lagrange_energy_values_SQL(dsbutton1, dsbutton3, precbutton1, precbutton2, precbutton3):
    if(dsbutton1== 'sunken' and precbutton1== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.LagrangeEnergySQLLowPrecisionGrid", cnxn)
    if(dsbutton1== 'sunken' and precbutton2== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.LagrangeEnergySQLMediumPrecisionGrid", cnxn)
    if(dsbutton1== 'sunken' and precbutton3== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.LagrangeEnergySQLHighPrecisionGrid", cnxn)
    if(dsbutton3== 'sunken' and precbutton1== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.LagrangeEnergySQLLowPrecisionFFT", cnxn)
    if(dsbutton3== 'sunken' and precbutton2== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.LagrangeEnergySQLMediumPrecisionFFT", cnxn)
    if(dsbutton3== 'sunken' and precbutton3== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.LagrangeEnergySQLHighPrecisionFFT", cnxn)
        
    if(not data_points.empty):
        logging.info('SQL fetch successful!')
    return data_points

def fetch_FGG_time_values_SQL(dsbutton1, dsbutton3, precbutton1, precbutton2, precbutton3):
    if(dsbutton1== 'sunken' and precbutton1== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.FGGTimeSQLLowPrecisionGrid", cnxn)
    if(dsbutton1== 'sunken' and precbutton2== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.FGGTimeSQLMediumPrecisionGrid", cnxn)
    if(dsbutton1== 'sunken' and precbutton3== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.FGGTimeSQLHighPrecisionGrid", cnxn)
    if(dsbutton3== 'sunken' and precbutton1== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.FGGTimeSQLLowPrecisionFFT", cnxn)
    if(dsbutton3== 'sunken' and precbutton2== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.FGGTimeSQLMediumPrecisionFFT", cnxn)
    if(dsbutton3== 'sunken' and precbutton3== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.FGGTimeSQLHighPrecisionFFT", cnxn)
        
    if(not data_points.empty):
        logging.info('SQL fetch successful!')
    return data_points

def fetch_lagrange_time_values_SQL(dsbutton1, dsbutton3, precbutton1, precbutton2, precbutton3):
    if(dsbutton1== 'sunken' and precbutton1== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.LagrangeTimeSQLLowPrecisionGrid", cnxn)
    if(dsbutton1== 'sunken' and precbutton2== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.LagrangeTimeSQLMediumPrecisionGrid", cnxn)
    if(dsbutton1== 'sunken' and precbutton3== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.LagrangeTimeSQLHighPrecisionGrid", cnxn)
    if(dsbutton3== 'sunken' and precbutton1== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.LagrangeTimeSQLLowPrecisionFFT", cnxn)
    if(dsbutton3== 'sunken' and precbutton2== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.LagrangeTimeSQLMediumPrecisionFFT", cnxn)
    if(dsbutton3== 'sunken' and precbutton3== 'sunken'):
        data_points= pd.read_sql("Select * FROM dbo.LagrangeTimeSQLHighPrecisionFFT", cnxn)
        
    if(not data_points.empty):
        logging.info('SQL fetch successful!')
    return data_points