import pandas as pd
from data_process import graduate_admission
import seaborn as sns
from matplotlib import pyplot as plt

def basic_info():
    df = graduate_admission("data/").full_df
    df.drop(["Serial No."], axis=1,inplace=True)
    print(df.describe())

    #ax = sns.heatmap(df.corr(), annot=True,vmin=0, vmax=1 ,cmap='Blues')
    plt.show()

if __name__ == "__main__":
    basic_info()