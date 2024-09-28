import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    df = pd.read_csv(file_path, header=None, encoding='latin-1', names=['target','id','date','meta','user','text'])
    df['sentiment'] = df['target'].apply(lambda x: 'positive' if x==4 else 'negative')
    df.drop(columns=['id','date','meta','user'], inplace=True)
    print(df.head())
    return df

file_path ='sentiment140.csv'

df = load_data(file_path)

num_pos = len(df[df['sentiment']=='positive'])
num_negative = len(df[df['sentiment']=='negative'])

print(num_pos,num_negative)


avg_length = df['text'].apply(lambda x:len(x.split())).mean()
print(avg_length)

df['text_length'] =df['text'].apply(lambda x:len(x.split()))

plt.figure(figsize=(10,6))

sns.histplot(df[df['sentiment']=='positive']['text_length'],kde=True, color='blue',label='positive' , alpha=0.6)
sns.histplot(df[df['sentiment']=='negative']['text_length'],kde=True, color='red',label='negative' , alpha=0.6)
plt.xlabel("Tweet Length")
plt.ylabel("Frequency")
plt.title('Tweet Length Distribution')
plt.legend()
plt.show()