
from datetime import datetime
from deep_translator import GoogleTranslator
from flask import Flask, flash,render_template,jsonify,request
from semantic_search import semmantic
from gtts import gTTS
from googletrans import Translator
import speech_recognition
from twilio.twiml.messaging_response import MessagingResponse
import wikipedia
import os
from telegram.ext import *
from telegram.ext.filters import Filters
from telegram.ext.updater import Updater
from telegram.update import Update
from PyPDF2 import PdfReader

# import nltk
# nltk.download(('punkt'))

#Initializations
app = Flask(__name__)
app.secret_key = '12345'
translator = Translator()
language = "en"

faqslist = ["src/data/Working/UGC_2.csv"]


def get_response(user_message): 
    global language
    return semmantic(faqslist,user_message)

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat',methods=["POST"])
def chat():
    try:
        global language, user_message
        user_message = request.form["text"]  
        # Number check in string
        # if any(map(str.isdigit, user_message)):
        #     return jsonify({"status":"success","response":"The answer is "+ str(eval(user_message))})
            
        language =  (translator.detect(user_message)).lang
        if 'w!' not in user_message:

            if language == "en":
                response_text = get_response(user_message)
                #voice_translate(translated_msg,"en")
                writeToHistory(user_message,response_text)
                return jsonify({"status":"success","response":response_text})

            elif language == "hi":
                translated_msg = GoogleTranslator(source=language, target='en').translate(user_message)
                #voice_translate(translated_msg,"hi")
                response_text = get_response(translated_msg)
                translated_response = GoogleTranslator(source="en", target='hi').translate(response_text)
                return jsonify({"status":"success","response":translated_response})
            
            elif language == "ta":
                translated_msg = GoogleTranslator(source=language, target='en').translate(user_message)
                # voice_translate(translated_msg,"ta")
                response_text = get_response(translated_msg)
                translated_response = GoogleTranslator(source="en", target='ta').translate(response_text)
                return jsonify({"status":"success","response":translated_response})
            
            elif language == "te":
                translated_msg = GoogleTranslator(source=language, target='en').translate(user_message)
                # voice_translate(translated_msg,"ta")
                response_text = get_response(translated_msg)
                translated_response = GoogleTranslator(source="en", target='te').translate(response_text)
                return jsonify({"status":"success","response":translated_response})

            elif language == "gu":
                translated_msg = GoogleTranslator(source=language, target='en').translate(user_message)
                # voice_translate(translated_msg,"ta")
                response_text = get_response(translated_msg)
                translated_response = GoogleTranslator(source="en", target='gu').translate(response_text)
                return jsonify({"status":"success","response":translated_response})

            elif language == "ml":
                translated_msg = GoogleTranslator(source=language, target='en').translate(user_message)
                # voice_translate(translated_msg,"ta")
                response_text = get_response(translated_msg)
                translated_response = GoogleTranslator(source="en", target='ml').translate(response_text)
                return jsonify({"status":"success","response":translated_response})

        
            # Wikipedia
        elif 'w!' in user_message:
            # wikipedia.set_lang(language)
            wiki_res = (wikipedia.summary(user_message, sentences = 2))
            writeToHistory(user_message,wiki_res)
            return jsonify({"status":"success","response":wiki_res})

    except Exception as e:
        print(e)
        return jsonify({"status":"success","response":"Not trained to do the work yet"})


# In order to run on whatsapp first connect localhost to ngrok
@app.route("/sms",methods=['POST'])
def whatsapp():
    user_msg = request.form.get('Body')
    language =  (translator.detect(user_msg)).lang
    response = MessagingResponse()

    if language=="en":
        reply = get_response(user_msg)

    elif language=="hi":
        translated_msg = GoogleTranslator(source=language, target='en').translate(user_msg)
        # voice_translate(translated_msg,"hi")
        translated_response = get_response(translated_msg)
        reply = GoogleTranslator(source="en", target='hi').translate(translated_response)
    
    
    response.message(reply)
    return str(response)


def telegram():
    updater = Updater("5437110366:AAFwUPMgIpIijW0RaJeTnMPRsE5tGy4ZhuQ",use_context=True)
    def start(update: Update, context: CallbackContext):
        update.message.reply_text("testing.......\n /start - To start the bot")
    
    def query(update:Update,context:CallbackContext):
        try:
            user_msg=update.message.text
            print(user_msg)
            language =  (translator.detect(user_msg)).lang
            if language == "en":
                result=get_response(user_msg)
                update.message.reply_text("%s"%result) 
            elif language == "hi":
                translated_msg = GoogleTranslator(source=language, target='en').translate(user_msg)
                translated_response = get_response(translated_msg)
                result = GoogleTranslator(source="en", target='hi').translate(translated_response)
                update.message.reply_text("%s"%result)
            elif language == "ta":
                translated_msg = GoogleTranslator(source=language, target='en').translate(user_msg)
                translated_response = get_response(translated_msg)
                result = GoogleTranslator(source="en", target='ta').translate(translated_response)
                update.message.reply_text("%s"%result)

            elif language == "gu":
                translated_msg = GoogleTranslator(source=language, target='en').translate(user_msg)
                translated_response = get_response(translated_msg)
                result = GoogleTranslator(source="en", target='gu').translate(translated_response)
                update.message.reply_text("%s"%result)

            elif language == "te":
                translated_msg = GoogleTranslator(source=language, target='en').translate(user_msg)
                translated_response = get_response(translated_msg)
                result = GoogleTranslator(source="en", target='te').translate(translated_response)
                update.message.reply_text("%s"%result)

            elif language == "ml":
                translated_msg = GoogleTranslator(source=language, target='en').translate(user_msg)
                translated_response = get_response(translated_msg)
                result = GoogleTranslator(source="en", target='ml').translate(translated_response)
                update.message.reply_text("%s"%result)
                

        except Exception as e:
            print(e)
        
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text,query))
    updater.start_polling()

telegram()

@app.route('/speech')
def speech():
    recorgnizer = speech_recognition.Recognizer()
    text=""
    while text!="stop":
        try:
            with speech_recognition.Microphone() as mic:
                recorgnizer.adjust_for_ambient_noise(mic,duration=0.5)
                audio = recorgnizer.listen(mic)
            
                text = recorgnizer.recognize_google(audio)
                response_text = get_response(text)
                print(text)
                flash(response_text)
                print(response_text)
                voice_translate(response_text,'en')
                return render_template('test.html',response_text=response_text)
        
                
        except Exception as e:
            print(e)
            return ("nothing")




@app.route('/admin',methods=['GET','POST'])
def admin():
    if request.method == 'POST':
        question = request.form.get('question')
        answer = request.form.get('answer')
        f = open('src/data/user/user.csv','a')
        f.write(question+','+answer+'\n')
       
        f = request.files['file']
        f.save(f.filename)
        name = f.filename
        print(name)
        reader = PdfReader(f"{name}")
        number_of_pages = len(reader.pages)
        page = reader.pages[0]
        text = page.extract_text()
        print(text)
        return 'file uploaded successfully'

    return render_template("admin.html")

# Voice Translator
def voice_translate(og,conv):
    voice = gTTS(text=og,lang=conv,slow=False)
    voice.save("audio.mp3")
    os.system("mpg123 -q audio.mp3")
    # -q is used for quiet output 

# To store query and answers
def writeToHistory(ques,msg):
    f = open('src/logs/whatsapp.log','a')
    sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
    f.write('{0:10} , {1:14} , {2:13}\n'.format(sttime,ques,msg))
    f.close()  


if __name__ == '__main__':
    # app.run()
    app.run(debug=True,threaded=True)