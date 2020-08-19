import pandas as pd

data = pd.read_excel('exemple of extract list.xls')

#print(data.head())
data.to_csv('out.csv',index=False,header=False)
df = pd.read_csv("out.csv")
#print(df.head())


df['ADDRESS'] = df['ADRESSE'].str.split('\s+').str[:-2].apply(lambda x: " ".join(x))
#df['ADDRESS'] = df['ADDRESS'].str.replace(',',' ').astype(str)
#print(df['ADDRESS'])

df['CITY'] = df['ADRESSE'].str.split('\s+').str[-1]
#print(df['CITY'])
#df= df.append(CITY)

df['POSTAL_CODE'] = df['ADRESSE'].str.split('\s+').str[-2]
# #print(df['POSTAL_CODE'])

df['FAX'] = df['TÉL / FAX'].str.split('\n').str[1]
#print(df['FAX'])
df['TEL'] = df['TÉL / FAX'].str.split('\n').str[0]


df1 = df['MARQUE'].str.split("\n",expand=True)
d = pd.concat([df,df1],axis=1)

df2 = d.rename(columns={'NOM':'NAME',0:"BRAND1",1:"BRAND2",2:"BRAND3",3:"BRAND4"})
all_data= df2.drop(['ADRESSE',"TÉL / FAX","Unnamed: 2","Unnamed: 3",'MARQUE'],axis=1)

pd.set_option('display.max_columns',100)

print(all_data.head())

# all_data = pd.concat([df,d,df['ADDRESS'],df['CITY'],df['POSTAL_CODE'],df['FAX']])
# all_data = all_data.rename(columns={'NOM':'NAME',0:"BRAND1",1:"BRAND2",2:"BRAND3",3:"BRAND4"})
# df2= all_data.drop(['ADRESSE',"TÉL / FAX","Unnamed: 2","Unnamed: 3"],axis=1)
pd.set_option('display.max_columns',100)
#print(df2.head())
all_data.to_excel('2.xlsx',index=False)
