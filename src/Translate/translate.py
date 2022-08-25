from deep_translator import GoogleTranslator
translated = GoogleTranslator(source='english', target='hindi').translate_file('src/data/csv/18-19_modifieddata.csv')
print(translated)
f = open('src/data/Hindi_CSV/hindi_random_3.csv','w')
f.write(translated)
f.close()