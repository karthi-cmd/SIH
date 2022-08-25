from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
flag = 0

# Language Dictionary
dic = ('afrikaans', 'af', 'albanian', 'sq',
	'amharic', 'am', 'arabic', 'ar',
	'armenian', 'hy', 'azerbaijani', 'az',
	'basque', 'eu', 'belarusian', 'be',
	'bengali', 'bn', 'bosnian', 'bs', 'bulgarian',
	'bg', 'catalan', 'ca', 'cebuano',
	'ceb', 'chichewa', 'ny', 'chinese (simplified)',
	'zh-cn', 'chinese (traditional)',
	'zh-tw', 'corsican', 'co', 'croatian', 'hr',
	'czech', 'cs', 'danish', 'da', 'dutch',
	'nl', 'english', 'en', 'esperanto', 'eo',
	'estonian', 'et', 'filipino', 'tl', 'finnish',
	'fi', 'french', 'fr', 'frisian', 'fy', 'galician',
	'gl', 'georgian', 'ka', 'german',
	'de', 'greek', 'el', 'gujarati', 'gu',
	'haitian creole', 'ht', 'hausa', 'ha',
	'hawaiian', 'haw', 'hebrew', 'he', 'hindi',
	'hi', 'hmong', 'hmn', 'hungarian',
	'hu', 'icelandic', 'is', 'igbo', 'ig', 'indonesian',
	'id', 'irish', 'ga', 'italian',
	'it', 'japanese', 'ja', 'javanese', 'jw',
	'kannada', 'kn', 'kazakh', 'kk', 'khmer',
	'km', 'korean', 'ko', 'kurdish (kurmanji)',
	'ku', 'kyrgyz', 'ky', 'lao', 'lo',
	'latin', 'la', 'latvian', 'lv', 'lithuanian',
	'lt', 'luxembourgish', 'lb',
	'macedonian', 'mk', 'malagasy', 'mg', 'malay',
	'ms', 'malayalam', 'ml', 'maltese',
	'mt', 'maori', 'mi', 'marathi', 'mr', 'mongolian',
	'mn', 'myanmar (burmese)', 'my',
	'nepali', 'ne', 'norwegian', 'no', 'odia', 'or',
	'pashto', 'ps', 'persian', 'fa',
	'polish', 'pl', 'portuguese', 'pt', 'punjabi',
	'pa', 'romanian', 'ro', 'russian',
	'ru', 'samoan', 'sm', 'scots gaelic', 'gd',
	'serbian', 'sr', 'sesotho', 'st',
	'shona', 'sn', 'sindhi', 'sd', 'sinhala', 'si',
	'slovak', 'sk', 'slovenian', 'sl',
	'somali', 'so', 'spanish', 'es', 'sundanese',
	'su', 'swahili', 'sw', 'swedish',
	'sv', 'tajik', 'tg', 'tamil', 'ta', 'telugu',
	'te', 'thai', 'th', 'turkish',
	'tr', 'ukrainian', 'uk', 'urdu', 'ur', 'uyghur',
	'ug', 'uzbek', 'uz',
	'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
	'yiddish', 'yi', 'yoruba',
	'yo', 'zulu', 'zu')



def takecommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("listening..... 🎤")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing.....")
		query = r.recognize_google(audio, language='en-in')
		print(f"The User said {query}")
	except Exception as e:
		print("say that again please.....")
		return "None"
	return query



query = takecommand()
while (query == "None"):
	query = takecommand()


def destination_language():
	print("Enter the language in which you\
	want to convert : Ex. Hindi , English , etc.")
	print()
	

	to_lang = takecommand()
	while (to_lang == "None"):
		to_lang = takecommand()
	to_lang = to_lang.lower()
	return to_lang

to_lang = destination_language()


while (to_lang not in dic):
	print("Language in which you are trying\
	to convert is currently not available ,\
	please input some other language")
	print()
	to_lang = destination_language()

to_lang = dic[dic.index(to_lang)+1]


translator = Translator()



text_to_translate = translator.translate(query, dest=to_lang)

text = text_to_translate.text


# Also, we have given 3rd argument as False because
# by default it speaks very slowly
speak = gTTS(text=text, lang=to_lang, slow=False)


speak.save("captured_voice.mp3")

# Using OS module to run the translated voice.
playsound('captured_voice.mp3')
# os.system("captured_voice.mp3")
os.remove('captured_voice.mp3')


print(text)


# import speech_recognition as spr
# from googletrans import Translator
# from gtts import gTTS
# import os
 

# recog1 = spr.Recognizer()
 
# mc = spr.Microphone()
 
 

# with mc as source:
#     print("Speak 'hello' to initiate the Translation !")
 
#     recog1.adjust_for_ambient_noise(source, duration=0.2)
#     audio = recog1.listen(source)
#     MyText = recog1.recognize_google(audio)
#     MyText = MyText.lower()
 

# if 'hello' in MyText:

#     translator = Translator()

#     from_lang = 'en'
 
#     to_lang = 'hi'
     
#     with mc as source:
         
#         print("Speak a stentence...")
#         recog1.adjust_for_ambient_noise(source, duration=0.2)
         
        
#         audio = recog1.listen(source)
         
    
#         get_sentence = recog1.recognize_google(audio)
 
       
#         try:
             
            
#             print("Phase to be Translated :"+ get_sentence)
 
#             text_to_translate = translator.translate(get_sentence, src= from_lang, dest= to_lang)
             
           
#             text = text_to_translate.text
 
           
#             speak = gTTS(text=text, lang=to_lang, slow= False)
 
            
#             speak.save("captured_voice.mp3")    
             
           
#             os.system("start captured_voice.mp3")
 
       
#         except spr.UnknownValueError:
#             print("Unable to Understand the Input")
             
#         except spr.RequestError as e:
#             print("Unable to provide Required Output".format(e))
# from gtts import gTTS
# from translate import Translator
# translator= Translator(from_lang="english",to_lang="hindi")
# translation = translator.translate("kuldeepx")
# print (translation)

