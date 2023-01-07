#Data Frames1
#python is case sensitive
import pandas as pd
pd._version_
 #=====================================================
 # #New versions don't display all columns in the console
 # pd.set_option('display.max_rows',500)
 # pd.set_option('display.max_columns',500)
 # pd.set_option('display.width',1000)
 #
 #=======================================================
 
 #To check the version
 print(pd._version_)
 #use single / or double \\
train=pd.read_csv(r"C:\Users\user\Downloads\train.csv")
print(type(train))

#explore the dataframe
train.shape #No of rows and columns
train.info() #Data type and nullable/non-nullable
train.describe() #Gives statistical information

#access columns of a dataframe
train['Sex']
train['Fare']
train.Sex
train.Fare
#Get a subset of columns
temp=train[['Survived','Fare','Embarked']]
print(type(temp))

#access rows of a dataframe
train[10:20]
train.iloc[10:20]

train[883.891]
train.iloc[885:891]

#Get me top n records
train.head(10)

#Get me bottom n records
train.tail(10)

#access both rows and coumns of a dataframe
train.iloc[10:11]

#If you wanted to access by columnname then use .loc
train.loc[train.Sex=='male','Sex']
train.loc[train.Sex=='female','Age']

#grouping data in data frames
train.groupby(['Embarked']).size()
train.groupby(['Pclass','Sex']).size()
train.groupby(['Pclass','Embarked']).mean()

train.groupby(['Embarked','Pclass']).mean()['Fare']

