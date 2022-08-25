import pandas as pd
from transformers import pipeline

def NeuralNetwork(faqslist,user_message):
    # Checking for question in already exisiting file
    for i in range(0,len(faqslist)):
        # print(pd.read_csv(faqslist[i]))
        question = pd.read_csv(faqslist[i])['Question'].tolist()
        answer = pd.read_csv(faqslist[i])['Answer'].tolist()
        answer = str(answer)
        # print(question)
        # question = str(question)
    if user_message in question:
        print(user_message)
        print("Found") 
    else:
        f = open('src/test.csv','a')
        f.write("\n {},".format(user_message))

    question_answerer = pipeline("question-answering", model='src/models/distilbert-base-uncased-distilled-squad')
    # print(str(answer))
    result = question_answerer(question=user_message,context=answer)
    # print(result)
    print(f"{result['answer']}")

faqslist = ["src/data/Working/Greetings.csv"]
NeuralNetwork(faqslist,"Thanks")



# from pandas import *

# data = read_csv('src/data/Working/Greetings.csv')
# question = data['Question'].tolist()
# answer = data['Answer'].tolist()

# f = open('src/data/Working/Greetings.csv','a')

# take_input = str(input("enter: "))

# if take_input not in question:
#     new_word = take_input

#     f.write(str(new_word))
#     print('\n')
#     print(new_word)

# else:
#     pass
