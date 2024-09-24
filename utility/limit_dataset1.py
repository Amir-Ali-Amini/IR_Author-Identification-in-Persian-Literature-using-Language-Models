#%%

import pandas as pd


def limit_df(text, n_word=500):
    print(text)
    return " ".join(text.replace("\n\n","").split()[:n_word])

df = pd.read_csv("merged_df.csv")
#%%
texts = list(map(limit_df,list(df["text"])))
len(texts)

# %%
df["text"] = texts
# %%
df.to_csv("limited_persian.csv")

# %%
import torch
torch.cuda.is_available()
# %%
