import pandas as pd
import plotly.express as px
df=pd.read_csv("Copy+of+data+-+data.csv")
figure=px.bar(df,x="date",y="cases")
figure.show()
data=df["cases"].tolist()
total=0
for i in range(0,len(data)):
  total=total+data[i]
mean=total/ len(data)
print(mean)
if(len(data)%2==1):
  median=data[int (len(data)/2)]
print(median)