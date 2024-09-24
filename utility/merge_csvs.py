#%%
import pandas as pd
import os
#%%
dir = "./result1"
files = [file for file in os.listdir(dir) if file[-3:]=="csv"]
files
# %%
df_merged = pd.read_csv(f'{dir}/{files[0]}')
for fileIdx in range(1,len(files)):
    df = pd.read_csv(f'{dir}/{files[fileIdx]}')
    df_merged=pd.concat([df_merged,df],ignore_index=True)


# %%
df_merged
len(df_merged["author"].unique())
# %%
df_merged.drop( columns=["b_name","p_name" ])

# %%
len(df_merged["author"].unique())
#%%
df_merged.to_csv("./result/persian_authors.csv")
# %%

df = pd.read_csv(f'./result/persian_authors.csv')
df.shape
len(df["author"].unique())
# %%
import seaborn as sns
sns.catplot(data=df, x='author', kind='count')
plt.show()

# %%
for i in df["text"]:
    try :
        (len(i))
    except:
        print(i)

# %%
        
for i in range(len(df)):
    print(df["author"][i] , len(df["text"][i]))
# %%
