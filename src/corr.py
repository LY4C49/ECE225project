import pandas as pd
from data_process import graduate_admission
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

def corr_info():
    df = graduate_admission("data/").full_df
    df.drop(["Serial No."], axis=1,inplace=True)
    #print(df.describe())

    zeros = np.zeros((df.shape[1],df.shape[1]))
    mask = np.zeros_like(zeros)
    for i in range(len(mask)):
        for j in range(i+1, len(mask[0])):
            mask[i][j] = True
    
    colormap = sns.diverging_palette(230, 10, as_cmap=True)
    #palette = sns.color_palette("Spectral", as_cmap=True)
    plt.figure(figsize=(32,18))
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    ax = sns.heatmap(df.corr(), annot=True,vmin=0.3, vmax=1 ,cmap=colormap,mask=mask, fmt=".2f",annot_kws={"fontsize": 20},cbar=False)
    
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    cb = ax.figure.colorbar(ax.collections[0]) #显示colorbar
    cb.ax.tick_params(labelsize=20)  # 设置colorbar刻度字体大小。
    
    #pair = sns.pairplot(df, hue="Research", kind='reg',height=1.5)
    #plt.show()
    plt.savefig('graph/filename.pdf',dpi=600,format='pdf',bbox_inches='tight')

if __name__ == "__main__":
    corr_info()