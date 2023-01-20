import sys
import numpy as np
import numpy.linalg as la
import pandas as pd
import seaborn as sns
sns.set()
sns.set_style('whitegrid')
paper_rc = {'lines.linewidth': 1, 'lines.markersize': 7} 
sns.set_context('paper', font_scale=2.5, rc=paper_rc)
                   
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")


df = abs(pd.read_csv('correlation.csv'))
W0 = df.to_numpy().reshape(len(df.columns), len(df.columns))

names = df.columns.tolist()
names

case = "age"
phi_values = [1.0, 0.9, 0.8, 0.5]
fig, ax= plt.subplots(2, 2, figsize=(18, 12))
grid = [ax[0,0], ax[0,1], ax[1,0], ax[1,1]]

from bfcm import reasoning

for i in range(len(phi_values)):
    
    df = pd.DataFrame(columns=["feature","iteration","value"])
    
    for k in range(20):
        
        f9 = np.random.uniform(0.0,1.0)
        f14 = np.random.uniform(0.0,1.0)
        f15 = np.random.uniform(0.0,1.0)
        
        A = np.array([[0, 0, 0, 0, 0, 0, 0, 0, f9, 0, 0, 0, 0, f14, f15, 0, 0, 0, 0, 0]])
        
        state = reasoning(W0, A, T=21, phi=phi_values[i])

        data_age = state[0,:,0]
        data_foreign = state[0,:,4]
        data_gender = state[0,:,12]
        
        df1 = pd.DataFrame(columns=["feature","iteration","value"])
        df1["iteration"] = range(len(data_age))
        df1["value"] = data_age.tolist()
        df1["feature"] = "Age"
        
        df2 = pd.DataFrame(columns=["feature","iteration","value"])
        df2["iteration"] = range(len(data_foreign))
        df2["value"] = data_foreign.tolist()
        df2["feature"] = "Foreign worker"
        
        df3 = pd.DataFrame(columns=["var","iteration","value"])
        df3["iteration"] = range(len(data_gender))
        df3["value"] = data_gender.tolist()
        df3["feature"] = "Gender"
        
        df = pd.concat([df,df1,df2,df3], ignore_index=True)
    
    ax1 = sns.lineplot(data=df, x="iteration", y="value", hue="feature", ax=grid[i], marker='o')
    ax1.xaxis.get_major_locator().set_params(integer=True)
    
    grid[i].set_title('phi=' + str(phi_values[i]))
    grid[i].set_ylabel(None)
    grid[i].set_xlabel(None)
    
    grid[i].set_ylim([0, 0.35])
    grid[i].legend(loc='best')
    plt.ylim(0, 0.35)
    
    fig.tight_layout()
    plt.savefig('age.pdf')