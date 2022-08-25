import pandas as pd

df = pd.read_csv('src/data/csv/Greetings.csv')
print(df.head())
while True:
    b=input('enter your question? : ')
    if(b == 'quit'):
        print("Byee")
        break
    
    else:
        print("Question : ",b)
        a=(df[df['Question']==b].Answer)
        print("Answers : ",a)
        print("Type quit to exit ")
    



