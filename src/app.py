from datetime import datetime
from twilio.twiml.messaging_response import MessagingResponse
from deep_translator import GoogleTranslator
from flask import Flask,render_template,jsonify,request
from faqengine import *
from gtts import gTTS
from googletrans import Translator
import wikipedia
import numpy as np


app = Flask(__name__)
app.secret_key = '12345'

faqslist = ["src/data/Working/Greetings.csv","src/data/Progress/UGC-function.csv","src/data/Working/UGC_1.csv","src/data/Working/UGC_2.csv","src/data/Working/UGC_3.csv"]
boo=True
faqmodel = FaqEngine(faqslist)

translator = Translator()
language = "en"

def get_response(user_message): 
    global language
    return faqmodel.query(user_message)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat',methods=["POST"])

def chat():    
    try:
        global boo
        if boo:
            t_json=info()
            boo=False
            return t_json
            
        else:
            lsq=pick_questions()
            print(type(lsq))
            print(lsq.dtype)
            # print(lsq)
            global language, user_message
            for i in np.nditer(lsq,flags=["refs_OK"]):
                # user_message = request.form["text"]  
                user_message=i
                # language =  (translator.detect(user_message)).lang
                if 'w!' not in user_message:
                    # translated_msg = GoogleTranslator(source=language, target='en').translate(user_message)
                    # response_text = get_response((translated_msg))
                    response_text=get_response(user_message)
                    return lang_response(language,response_text)
                    # Wikipedia
                elif 'w!' in user_message:
                    # wikipedia.set_lang(language)
                    wiki_res = (wikipedia.summary(user_message, sentences = 2))
                    writeToHistory(user_message,wiki_res)
                    return jsonify({"status":"success","response":wiki_res})

    except Exception as e:
        print(e)
        # question=pick_questions()
        # if user_message not in  question:
        # writeToAnalysis(e)
        return jsonify({"status":"success","response":"Not trained to do the work yet"})


# Whatsapp bot

@app.route("/sms",methods=['POST'])
def reply():
    msg = request.form.get('Body')
    if(msg.lower() == "hello"):
        reply = "Hello How can i help you"
    else:
        reply = msg
    response = MessagingResponse()
    response.message(reply)
    return str(response)

def info(*args):
    return jsonify({"status":"success","response":"Hi am Resque squad bot here to help u,<br>if u want to search in wiki page use 'w! your question' "})

def lang_response(language,response_text):
    translated = GoogleTranslator(source='auto', target=language).translate(response_text)
    voice_translate(translated,language)
    writeToHistory(user_message,translated)
    return jsonify({"status":"success","response":translated})
    
# Voice Translator
def voice_translate(og,conv):
    voice = gTTS(text=og,lang=conv,slow=False)
    voice.save("audio.mp3")
    os.system("mpg123 -q audio.mp3")
    # -q is used for quiet output 

# To store query and answers
def writeToHistory(ques,msg):
    f = open('src/history','a')
    sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
    f.write('{0:10}  {1:14}  {2:13}\n'.format(sttime,ques,msg))
    f.close()  

def writeToAnalysis(e):
    f = open('src/FutureAnalysis.txt','a')
    cur_time = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
    f.write('{0:10}  {1:14}  {2:13}\n'.format(cur_time,e))
    f.close()
    
def pick_questions():
    import pandas as pd
    dataframeslist = [pd.read_csv(csvfile).dropna() for csvfile in faqslist]
    data = pd.concat(dataframeslist, ignore_index=True)
    questions=data['Question'].values
    # print(questions)
    return questions
  

if __name__ == '__main__':
    # app.run()
    app.run(debug=True)