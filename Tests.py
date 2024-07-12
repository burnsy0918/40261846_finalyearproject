import unittest
import fetch_values
import pandas as pd

class TestStringMethods(unittest.TestCase):
    def test_lagrange_time_values(self):
        Test_data1 = fetch_values.fetch_lagrange_time_values('sunken', 'raised', 'sunken', 'raised', 'raised')
        Test_data2 = fetch_values.fetch_lagrange_time_values('sunken', 'raised', 'raised', 'sunken', 'raised')
        Test_data3 = fetch_values.fetch_lagrange_time_values('sunken', 'raised', 'raised', 'raised', 'sunken')
        Test_data4 = fetch_values.fetch_lagrange_time_values('raised', 'sunken', 'sunken', 'raised', 'raised')
        Test_data5 = fetch_values.fetch_lagrange_time_values('raised', 'sunken', 'raised', 'sunken', 'raised')
        Test_data6 = fetch_values.fetch_lagrange_time_values('raised', 'sunken', 'raised', 'raised', 'sunken')
        
        Actual_data1 = pd.DataFrame(data= {'N': [64, 128, 256, 512], 'Time (ms)': [3.07, 6.3, 12.65, 35.1]})
        Actual_data2 = pd.DataFrame(data= {'N': [64, 128, 256, 512], 'Time (ms)': [4.62, 9.43, 19.05, 26.67]})
        Actual_data3 = pd.DataFrame(data= {'N': [64, 128, 256, 512], 'Time (ms)': [7.8, 15.87, 27.64, 43.84]})
        Actual_data4 = pd.DataFrame(data= {'N': [64, 128, 256, 512], 'Time (ms)': [6.8, 15.61, 33.1, 73.13]})
        Actual_data5 = pd.DataFrame(data= {'N': [64, 128, 256, 512], 'Time (ms)': [15.6, 33.03, 73.13, 121.59]})
        Actual_data6 = pd.DataFrame(data= {'N': [64, 128, 256, 512], 'Time (ms)': [33.02, 73.21, 121.59, 457.7]})
        
        self.assertEqual(Test_data1.values.all(), Actual_data1.values.all())
        self.assertEqual(Test_data2.values.all(), Actual_data2.values.all())
        self.assertEqual(Test_data3.values.all(), Actual_data3.values.all())
        self.assertEqual(Test_data4.values.all(), Actual_data4.values.all())
        self.assertEqual(Test_data5.values.all(), Actual_data5.values.all())
        self.assertEqual(Test_data6.values.all(), Actual_data6.values.all())
    
    def test_FGG_time_values(self):
        Test_data1 = fetch_values.fetch_FGG_time_values('sunken', 'raised', 'sunken', 'raised', 'raised')
        Test_data2 = fetch_values.fetch_FGG_time_values('sunken', 'raised', 'raised', 'sunken', 'raised')
        Test_data3 = fetch_values.fetch_FGG_time_values('sunken', 'raised', 'raised', 'raised', 'sunken')
        Test_data4 = fetch_values.fetch_FGG_time_values('raised', 'sunken', 'sunken', 'raised', 'raised')
        Test_data5 = fetch_values.fetch_FGG_time_values('raised', 'sunken', 'raised', 'sunken', 'raised')
        Test_data6 = fetch_values.fetch_FGG_time_values('raised', 'sunken', 'raised', 'raised', 'sunken')
        
        Actual_data1 = pd.DataFrame({'N': [64, 128, 256, 512], 'Time (ms)': [1.58, 3.29, 8.18, 16.88]})
        Actual_data2 = pd.DataFrame({'N': [64, 128, 256, 512], 'Time (ms)': [2.5, 5.13, 13.33, 27.3]})
        Actual_data3 = pd.DataFrame({'N': [64, 128, 256, 512], 'Time (ms)': [4.33, 8.78, 23.32, 47.7]})
        Actual_data4 = pd.DataFrame({'N': [64, 128, 256, 512], 'Time (ms)': [3.09, 6.8, 15.63, 32.99]})
        Actual_data5 = pd.DataFrame({'N': [64, 128, 256, 512], 'Time (ms)': [3.13, 6.8, 15.6, 33]})
        Actual_data6 = pd.DataFrame({'N': [64, 128, 256, 512], 'Time (ms)': [3.09, 6.79, 15.61, 33]})
        
        self.assertEqual(Test_data1.values.all(), Actual_data1.values.all())
        self.assertEqual(Test_data2.values.all(), Actual_data2.values.all())
        self.assertEqual(Test_data3.values.all(), Actual_data3.values.all())
        self.assertEqual(Test_data4.values.all(), Actual_data4.values.all())
        self.assertEqual(Test_data5.values.all(), Actual_data5.values.all())
        self.assertEqual(Test_data6.values.all(), Actual_data6.values.all())
    
    def test_lagrange_energy_values(self):
        Test_data1 = fetch_values.fetch_lagrange_energy_values('sunken', 'raised', 'sunken', 'raised', 'raised')
        Test_data2 = fetch_values.fetch_lagrange_energy_values('sunken', 'raised', 'raised', 'sunken', 'raised')
        Test_data3 = fetch_values.fetch_lagrange_energy_values('sunken', 'raised', 'raised', 'raised', 'sunken')
        Test_data4 = fetch_values.fetch_lagrange_energy_values('raised', 'sunken', 'sunken', 'raised', 'raised')
        Test_data5 = fetch_values.fetch_lagrange_energy_values('raised', 'sunken', 'raised', 'sunken', 'raised')
        Test_data6 = fetch_values.fetch_lagrange_energy_values('raised', 'sunken', 'raised', 'raised', 'sunken')
        
        Actual_data1 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [1.6, 3.1, 6.2, 10]})
        Actual_data2 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [2.2, 4.4, 8.8, 12]})
        Actual_data3 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [3.5, 7, 12, 19]})
        Actual_data4 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [3.2, 7.3, 15, 34]})
        Actual_data5 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [7.2, 15, 34, 54]})
        Actual_data6 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [15, 34, 54, 190]})
        
        self.assertEqual(Test_data1.values.all(), Actual_data1.values.all())
        self.assertEqual(Test_data2.values.all(), Actual_data2.values.all())
        self.assertEqual(Test_data3.values.all(), Actual_data3.values.all())
        self.assertEqual(Test_data4.values.all(), Actual_data4.values.all())
        self.assertEqual(Test_data5.values.all(), Actual_data5.values.all())
        self.assertEqual(Test_data6.values.all(), Actual_data6.values.all())
    
    def test_FGG_energy_values(self):
        Test_data1 = fetch_values.fetch_FGG_energy_values('sunken', 'raised', 'sunken', 'raised', 'raised')
        Test_data2 = fetch_values.fetch_FGG_energy_values('sunken', 'raised', 'raised', 'sunken', 'raised')
        Test_data3 = fetch_values.fetch_FGG_energy_values('sunken', 'raised', 'raised', 'raised', 'sunken')
        Test_data4 = fetch_values.fetch_FGG_energy_values('raised', 'sunken', 'sunken', 'raised', 'raised')
        Test_data5 = fetch_values.fetch_FGG_energy_values('raised', 'sunken', 'raised', 'sunken', 'raised')
        Test_data6 = fetch_values.fetch_FGG_energy_values('raised', 'sunken', 'raised', 'raised', 'sunken')
        
        Actual_data1 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [0.74, 1.5, 3.5, 7.1]})
        Actual_data2 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [1.1, 2.2, 5.4, 11]})
        Actual_data3 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [1.8, 3.5, 9.1, 19]})
        Actual_data4 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [1.5, 3.2, 7.3, 15]})
        Actual_data5 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [1.5, 3.2, 7.3, 15]})
        Actual_data6 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [1.5, 3.2, 7.3, 15]})
        
        self.assertEqual(Test_data1.values.all(), Actual_data1.values.all())
        self.assertEqual(Test_data2.values.all(), Actual_data2.values.all())
        self.assertEqual(Test_data3.values.all(), Actual_data3.values.all())
        self.assertEqual(Test_data4.values.all(), Actual_data4.values.all())
        self.assertEqual(Test_data5.values.all(), Actual_data5.values.all())
        self.assertEqual(Test_data6.values.all(), Actual_data6.values.all())
        
    
    def test_FGG_energy_values_SQL(self):
        Test_data1 = fetch_values.fetch_FGG_energy_values_SQL('sunken', 'raised', 'sunken', 'raised', 'raised')
        Test_data2 = fetch_values.fetch_FGG_energy_values_SQL('sunken', 'raised', 'raised', 'sunken', 'raised')
        Test_data3 = fetch_values.fetch_FGG_energy_values_SQL('sunken', 'raised', 'raised', 'raised', 'sunken')
        Test_data4 = fetch_values.fetch_FGG_energy_values_SQL('raised', 'sunken', 'sunken', 'raised', 'raised')
        Test_data5 = fetch_values.fetch_FGG_energy_values_SQL('raised', 'sunken', 'raised', 'sunken', 'raised')
        Test_data6 = fetch_values.fetch_FGG_energy_values_SQL('raised', 'sunken', 'raised', 'raised', 'sunken')
        
        Actual_data1 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [0.74, 1.5, 3.5, 7.1]})
        Actual_data2 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [1.1, 2.2, 5.4, 11]})
        Actual_data3 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [1.8, 3.5, 9.1, 19]})
        Actual_data4 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [1.5, 3.2, 7.3, 15]})
        Actual_data5 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [1.5, 3.2, 7.3, 15]})
        Actual_data6 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [1.5, 3.2, 7.3, 15]})
        
        self.assertEqual(Test_data1.values.all(), Actual_data1.values.all())
        self.assertEqual(Test_data2.values.all(), Actual_data2.values.all())
        self.assertEqual(Test_data3.values.all(), Actual_data3.values.all())
        self.assertEqual(Test_data4.values.all(), Actual_data4.values.all())
        self.assertEqual(Test_data5.values.all(), Actual_data5.values.all())
        self.assertEqual(Test_data6.values.all(), Actual_data6.values.all())
    
    def test_Lagrange_energy_values_SQL(self):
        Test_data1 = fetch_values.fetch_Lagrange_energy_values_SQL('sunken', 'raised', 'sunken', 'raised', 'raised')
        Test_data2 = fetch_values.fetch_Lagrange_energy_values_SQL('sunken', 'raised', 'raised', 'sunken', 'raised')
        Test_data3 = fetch_values.fetch_Lagrange_energy_values_SQL('sunken', 'raised', 'raised', 'raised', 'sunken')
        Test_data4 = fetch_values.fetch_Lagrange_energy_values_SQL('raised', 'sunken', 'sunken', 'raised', 'raised')
        Test_data5 = fetch_values.fetch_Lagrange_energy_values_SQL('raised', 'sunken', 'raised', 'sunken', 'raised')
        Test_data6 = fetch_values.fetch_Lagrange_energy_values_SQL('raised', 'sunken', 'raised', 'raised', 'sunken')
        
        Actual_data1 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [1.6, 3.1, 6.2, 10]})
        Actual_data2 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [2.2, 4.4, 8.8, 12]})
        Actual_data3 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [3.5, 7, 12, 19]})
        Actual_data4 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [3.2, 7.3, 15, 34]})
        Actual_data5 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [7.2, 15, 34, 54]})
        Actual_data6 = pd.DataFrame({'N': [64, 128, 256, 512], 'Energy (V)x10^6': [15, 34, 54, 190]})
        
        self.assertEqual(Test_data1.values.all(), Actual_data1.values.all())
        self.assertEqual(Test_data2.values.all(), Actual_data2.values.all())
        self.assertEqual(Test_data3.values.all(), Actual_data3.values.all())
        self.assertEqual(Test_data4.values.all(), Actual_data4.values.all())
        self.assertEqual(Test_data5.values.all(), Actual_data5.values.all())
        self.assertEqual(Test_data6.values.all(), Actual_data6.values.all())
    
    def test_FGG_time_values_SQL(self):
        Test_data1 = fetch_values.fetch_FGG_time_values_SQL('sunken', 'raised', 'sunken', 'raised', 'raised')
        Test_data2 = fetch_values.fetch_FGG_time_values_SQL('sunken', 'raised', 'raised', 'sunken', 'raised')
        Test_data3 = fetch_values.fetch_FGG_time_values_SQL('sunken', 'raised', 'raised', 'raised', 'sunken')
        Test_data4 = fetch_values.fetch_FGG_time_values_SQL('raised', 'sunken', 'sunken', 'raised', 'raised')
        Test_data5 = fetch_values.fetch_FGG_time_values_SQL('raised', 'sunken', 'raised', 'sunken', 'raised')
        Test_data6 = fetch_values.fetch_FGG_time_values_SQL('raised', 'sunken', 'raised', 'raised', 'sunken')
        
        Actual_data1 = pd.DataFrame({'N': [64, 128, 256, 512], 'Time (ms)': [1.58, 3.29, 8.18, 16.88]})
        Actual_data2 = pd.DataFrame({'N': [64, 128, 256, 512], 'Time (ms)': [2.5, 5.13, 13.33, 27.3]})
        Actual_data3 = pd.DataFrame({'N': [64, 128, 256, 512], 'Time (ms)': [4.33, 8.78, 23.32, 47.7]})
        Actual_data4 = pd.DataFrame({'N': [64, 128, 256, 512], 'Time (ms)': [3.09, 6.8, 15.63, 32.99]})
        Actual_data5 = pd.DataFrame({'N': [64, 128, 256, 512], 'Time (ms)': [3.13, 6.8, 15.6, 33]})
        Actual_data6 = pd.DataFrame({'N': [64, 128, 256, 512], 'Time (ms)': [3.09, 6.79, 15.61, 33]})
        
        self.assertEqual(Test_data1.values.all(), Actual_data1.values.all())
        self.assertEqual(Test_data2.values.all(), Actual_data2.values.all())
        self.assertEqual(Test_data3.values.all(), Actual_data3.values.all())
        self.assertEqual(Test_data4.values.all(), Actual_data4.values.all())
        self.assertEqual(Test_data5.values.all(), Actual_data5.values.all())
        self.assertEqual(Test_data6.values.all(), Actual_data6.values.all())
    
    def test_lagrange_time_values_SQL(self):
        Test_data1 = fetch_values.fetch_lagrange_time_values_SQL('sunken', 'raised', 'sunken', 'raised', 'raised')
        Test_data2 = fetch_values.fetch_lagrange_time_values_SQL('sunken', 'raised', 'raised', 'sunken', 'raised')
        Test_data3 = fetch_values.fetch_lagrange_time_values_SQL('sunken', 'raised', 'raised', 'raised', 'sunken')
        Test_data4 = fetch_values.fetch_lagrange_time_values_SQL('raised', 'sunken', 'sunken', 'raised', 'raised')
        Test_data5 = fetch_values.fetch_lagrange_time_values_SQL('raised', 'sunken', 'raised', 'sunken', 'raised')
        Test_data6 = fetch_values.fetch_lagrange_time_values_SQL('raised', 'sunken', 'raised', 'raised', 'sunken')
        
        Actual_data1 = pd.DataFrame(data= {'N': [64, 128, 256, 512], 'Time (ms)': [3.07, 6.3, 12.65, 35.1]})
        Actual_data2 = pd.DataFrame(data= {'N': [64, 128, 256, 512], 'Time (ms)': [4.62, 9.43, 19.05, 26.67]})
        Actual_data3 = pd.DataFrame(data= {'N': [64, 128, 256, 512], 'Time (ms)': [7.8, 15.87, 27.64, 43.84]})
        Actual_data4 = pd.DataFrame(data= {'N': [64, 128, 256, 512], 'Time (ms)': [6.8, 15.61, 33.1, 73.13]})
        Actual_data5 = pd.DataFrame(data= {'N': [64, 128, 256, 512], 'Time (ms)': [15.6, 33.03, 73.13, 121.59]})
        Actual_data6 = pd.DataFrame(data= {'N': [64, 128, 256, 512], 'Time (ms)': [33.02, 73.21, 121.59, 457.7]})
        
        self.assertEqual(Test_data1.values.all(), Actual_data1.values.all())
        self.assertEqual(Test_data2.values.all(), Actual_data2.values.all())
        self.assertEqual(Test_data3.values.all(), Actual_data3.values.all())
        self.assertEqual(Test_data4.values.all(), Actual_data4.values.all())
        self.assertEqual(Test_data5.values.all(), Actual_data5.values.all())
        self.assertEqual(Test_data6.values.all(), Actual_data6.values.all())
        
if __name__ == '__main__':
    unittest.main()