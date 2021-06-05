# Julia Cuellar
# DSC 640
# Video

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Will use in Video
def read_file():
    air = pd.read_csv('air-safety.csv')
    print("Display data with null:\n", air.isnull())
    print("Display counts of null from data:\n", air.isnull().sum())
    print('Data:\n', air)


def read_file2():
    fin = pd.read_csv('Financial_Results__1947-Present_Full_Data_data.csv')
    print("Display data with null:\n", fin.isnull())
    print("Display counts of null from data:\n", fin.isnull().sum())
    print('Data:\n', fin)


# Will use in Video
def read_file3():
    fin = pd.read_csv('Financials_Full_Data_data.csv')
    print("Display data with null:\n", fin.isnull())
    print("Display counts of null from data:\n", fin.isnull().sum())
    print('Data:\n', fin)


# Will use in Video
def read_file4():
    safety = pd.read_csv('Safety Record of U.S. Air Carriers.csv')
    print("Display data with null:\n", safety.isnull())
    print("Display counts of null from data:\n", safety.isnull().sum())
    print('Data:\n', safety)


def read_file5():
    traffic = pd.read_csv('Traffic_&_Capacity_Full_Data_data.csv')
    print("Display data with null:\n", traffic.isnull())
    print("Display counts of null from data:\n", traffic.isnull().sum())
    print('Data:\n', traffic)


if __name__ == "__main__":
    read_file()
    read_file2()
    read_file3()
    read_file4()
    read_file5()