import pandas as pd
from data_process import graduate_admission
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

def toefl_chance():
    df = graduate_admission("data/").full_df
    df.drop(["Serial No."], axis=1,inplace=True)
    
    plt.figure(figsize=(32,18))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    pair = sns.lmplot(x="TOEFL Score", y="Chance of Admit ", data=df, hue="Research")
    #plt.show()
    plt.savefig('graph/toeflvschance.pdf',dpi=600,format='pdf',bbox_inches='tight')
    


def gre_chance():
    df = graduate_admission("data/").full_df
    df.drop(["Serial No."], axis=1,inplace=True)
    
    plt.figure(figsize=(32,18))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    pair = sns.lmplot(x="GRE Score", y="Chance of Admit ", data=df, hue="Research")
    #plt.show()
    plt.savefig('graph/grevschance.pdf',dpi=600,format='pdf',bbox_inches='tight')
    
def gpa_chance():
    df = graduate_admission("data/").full_df
    df.drop(["Serial No."], axis=1,inplace=True)
    
    plt.figure(figsize=(32,18))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    pair = sns.lmplot(x="CGPA", y="Chance of Admit ", data=df, hue="Research")
    #plt.show()
    plt.savefig('graph/gpavschance.pdf',dpi=600,format='pdf',bbox_inches='tight')

def toefl_gre():
    df = graduate_admission("data/").full_df
    df.drop(["Serial No."], axis=1,inplace=True)
    
    plt.figure(figsize=(32,18))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    pair = sns.lmplot(x="TOEFL Score", y="GRE Score", data=df, hue="Research")
    #plt.show()
    plt.savefig('graph/toeflvsgre.pdf',dpi=600,format='pdf',bbox_inches='tight')


if __name__ == "__main__":
    # toefl_chance()
    # gre_chance()
    #gpa_chance()
    toefl_gre()