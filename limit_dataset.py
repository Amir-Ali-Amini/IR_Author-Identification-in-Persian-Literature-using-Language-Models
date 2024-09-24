#%%

import pandas as pd


def limit_df(text, n_word=500):
    try :
        return " ".join(text.split()[:n_word] if text else "")
    except:
        return "-"
df = pd.read_csv("persian_authors_tokenized.csv")
#%%
texts = list(map(limit_df,list(df["text"])))
len(texts)

# %%
df["text"] = texts
# %%
df.to_csv("persian_authors_preprocessed.csv")

df.shape
# %%
len(df["text"][8].split())
# %%
import pandas as pd

#Count spaces plus one for number of words
df = pd.read_csv("persian_authors_preprocessed.csv")
df['word_count'] = df['text'].str.count(' ') + 1
df.shape
# %%

import seaborn as sns
import matplotlib.pyplot as plt
sns.catplot(data=df, x='author', kind='count')
plt.show()

sns.histplot(data=df, x='word_count', hue='author', kde=True)
plt.show()
# %%
