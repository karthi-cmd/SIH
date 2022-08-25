
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext import *
from telegram.ext.filters import Filters
from faqengine import *

faqslist = ["src/data/Working/Greetings.csv","src/data/Working/UGC_1.csv"]
faqmodel = FaqEngine(faqslist)
updater = Updater("5437110366:AAFwUPMgIpIijW0RaJeTnMPRsE5tGy4ZhuQ",use_context=True)
def get_response(user_message): 
    return faqmodel.query(user_message)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("testing.......\n /start\n /query\n")
    
def query(update:Update,context:CallbackContext):
    user_msg=update.message.text
    result=get_response(user_msg)
    update.message.reply_text("%s"%result)  
    
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '{}'" .format( update.message.text))

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)
  
    
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text,query))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command,unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
updater.start_polling()