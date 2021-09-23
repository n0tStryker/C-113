import seaborn as sms
import pandas as pd 
import plotly.figure_factory as ff 

sms.boxplot(data=df,x=df["quant_saved"])
q1 = df["quant_saved"].quantile(0.25)
q3 = df["quant_saved"].quantile(0.75)
iqr = q3 - q1 
print("q1=",q1)
print()
print("q3=",q3)
print()
print(iqr)

lower_whisker = q1 - 1.5*iqr
upper_whisker = q3 + 1.5*iqr

print(lower_whisker)
print(upper_whisker)

new_df = df[df["quant_saved"]<upper_whisker]

fig = ff.create_distplot([new_df["quant_saved "].tolist()], ["Savings"], show_hist=False) 
fig.show()