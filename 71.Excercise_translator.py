# Translate file from English to Japanese 

# translate PYPY  - offline translator service module :  https://pypi.org/project/translate/
# pip install translate
# https://devlibrary.withgoogle.com/

# use tranlator for bengali with bn

from translate import Translator 
translator = Translator(to_lang = "bn")
#translation = translator.translate("This is a Pen pinable apple pen")


try: 
    with open('test.txt', mode ='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('test-bn.txt', mode='w') as my_file2: 
            my_file2.write(translation)
except FileNotFoundError as e: 
    print('check your file path')



