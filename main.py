import random
import pyjokes
import speech_recognition as sr
import pyttsx3
from gtts import gTTS
from playsound import playsound
import pywhatkit
import datetime
import wikipedia
from translate import Translator


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
translateArEn = Translator(from_lang="arabic", to_lang="english")
translateEnAr = Translator(from_lang="english", to_lang="arabic")
wikipedia.set_lang("ar")
hello = "اتفضل يا قمر عايز ايه"
command = " "

def response(lol):
    obj = gTTS(text=lol, lang='ar', slow=False)
    obj.save('lol.mp3')
    playsound('lol.mp3')

def talk(text):
    t = text
    f = open('text.text', 'a', encoding='utf-8')
    f.writelines(t + '\n')
    f.close()
    obj = gTTS(text=t, lang='ar', slow=False)
    obj.save('text.mp3')
    playsound('text.mp3')

def take_command():
    command = " "
    try:
        with sr.Microphone() as src:
            print('انا استمع اليك')
            obj = gTTS(text=hello, lang='ar', slow=False)
            obj.save('hello.mp3')
            playsound('hello.mp3')
            audio = listener.listen(src)
            command = listener.recognize_google(audio, language='ar-USA')
            if 'مانيسا' in command:
                command = command.replace('تيمو','')
                print(command)
    except:
        pass
    return command




def run_temo():
    command = take_command()
    print(command)
    if 'شغل' in command:
        song = command.replace('شغل', '')
        song_r = (' هشغلك ' + song + " حالا ")
        obj = gTTS(text=song_r, lang='ar', slow=False)
        obj.save('song_r.mp3')
        playsound('song_r.mp3')
        pywhatkit.playonyt(song)
    elif 'الساعه' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        time_l = ('الساعه دلوقتي '+ time)
        obj = gTTS(text=time_l, lang='ar', slow=False)
        obj.save('time_now.mp3')
        playsound('time_now.mp3')
    elif "تعرفي ايه عن " in command:
        person = command.replace('تعرفي ايه عن ','')
        translation1 = translateArEn.translate(person)


        info_l = ('ثواني وهقولك على ' + person)
        obj = gTTS(text=info_l, lang='ar', slow=False)
        obj.save('info_l.mp3')
        playsound('info_l.mp3')

        info = wikipedia.summary(person, sentences=3)
        obj = gTTS(text=info, lang='ar', slow=False)
        obj.save('info.mp3')
        playsound('info.mp3')

    elif 'ديت' in command:
        fun = ['انا اسفة مش هينفع نخرج لوحدنا', 'لا انت فهمتني غلط يابيه' ,"اسفة بس انا مرتبطة", 'اسفة والله مش هينفع', 'بص هو انا نفسي بس مش هينفع']
        fun_res = random.choice(fun)
        obj = gTTS(text=fun_res, lang='ar', slow=False)
        obj.save('fun_res1.mp3')
        playsound('fun_res1.mp3')

    elif 'بيت' in command:
        fun = ['انا اسفة مش هينفع نخرج لوحدنا', 'لا انت فهمتني غلط يابيه', "اسفة بس انا مرتبطة", 'اسفة والله مش هينفع',
               'بص هو انا نفسي بس مش هينفع']
        fun_res = random.choice(fun)
        obj = gTTS(text=fun_res, lang='ar', slow=False)
        obj.save('fun_res1.mp3')
        playsound('fun_res1.mp3')
    elif 'ليه' in command:
        fun = ['كدا', 'هو كدا', "اسفة", 'معلش','بص هو انا نفسي بس مش هينفع']
        fun_res = random.choice(fun)
        obj = gTTS(text=fun_res, lang='ar', slow=False)
        obj.save('fun_res2.mp3')
        playsound('fun_res2.mp3')
    elif 'سنجل' in command:
        fun = ['مرتبطة', 'مرتبطة بس متقولش لحد', "اسفة مش هقدر اقولك", 'معلش هكلمك بعدين', 'بص هو انا نفسي بس مش هينفع']
        fun_res = random.choice(fun)
        obj = gTTS(text=fun_res, lang='ar', slow=False)
        obj.save('fun_res3.mp3')
        playsound('fun_res3.mp3')
    elif 'مرتبطه' in command:
        fun = ['مرتبطة', 'مرتبطة بس متقولش لحد', "اسفة مش هقدر اقولك", 'معلش هكلمك بعدين', 'بص هو انا نفسي بس مش هينفع']
        fun_res = random.choice(fun)
        obj = gTTS(text=fun_res, lang='ar', slow=False)
        obj.save('fun_res3.mp3')
        playsound('fun_res3.mp3')

    elif 'نكته' in command:
        joke = pyjokes.get_joke()
        joke_ar = translateEnAr.translate(str(joke))
        obj = gTTS(text=joke_ar, lang='ar', slow=False)
        obj.save('joke_ar.mp3')
        playsound('joke_ar.mp3')

    else:
        response = 'قولي ياقمر محتاج ايه مني'
        obj = gTTS(text=response, lang='ar', slow=False)
        playsound('response.mp3')



run_temo()


