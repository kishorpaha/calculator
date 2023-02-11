import sys
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Greetings
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 10:
        print("Good Morning!")
        speak("Asssalamu, Aylaikum, Good morning")

    elif hour >= 10 and hour <= 16:
        print("Good Noon!")
        speak("Asssalamu, Aylaikum, Good Noon!")

    elif hour >= 16 and hour <= 17:
        print("Good Afternoon!")
        speak("Asssalamu, Aylaikum, Good Afternoon!")

    elif hour >= 17 and hour <= 19:
        print("Good Evening!")
        speak("Asssalamu, Aylaikum, Good Evening!")

    else:
        print("Good Night!")
        speak("Asssalamu, Aylaikum, Good Night!")

    print("My name is bondhu. How may I help you?")
    speak("My name is bondhu. How may I help you?")

    # Commanding


def takeCommand():
    listener = sr.Recognizer()
    with sr.Microphone() as Mp:
        print("Listening...")
        listener.pause_threshold = 1
        audio = listener.listen(Mp)

    try:
        print("Recognizing...")
        friend = listener.recognize_google(audio, language='en-in')
        print(f"Umar said:{friend}\n")

    except Exception as e:
        print("Don't make a noise please...")
        speak(",")

        return 'None'

    # Answering the questions


if __name__ == '__main__':
    wishMe()
    while True:
        friend = takeCommand().lower()

        if 'joke' in friend:
            jokes = pyjokes.get_joke()
            print(jokes)
            speak(jokes)

        elif 'open youtube' in friend:
            print("Opening youtube...")
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in friend:
            print("Opening google...")
            speak("Opening google")
            webbrowser.open("google.com")

        elif 'open facebook' in friend:
            print("Opening facebook...")
            speak("Opening facebook")
            webbrowser.open("facebook.com")

        elif 'my website' in friend:
            print('Opening your website...')
            speak('Opening your website')
            webbrowser.open("https://kishorpaha.github.io/aandctechnology/")

        elif 'snake game' in friend:
            print('Opening your website...')
            speak('Opening your website')
            webbrowser.open("https://kishorpaha.github.io/snake/")

        # Desktop opening

        elif 'open code' in friend:
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(codePath)

        elif 'charm' in friend:
            charmPath = "C:\\Users\\Admin\\Desktop\\project 2\\pycharm-community-2021.2.2.exe"
            os.startfile(charmPath)

        elif 'open chrome' in friend:
            cromePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.exe"
            os.startfile(cromePath)

        elif 'poochho' in friend:
            puchoPath = "C:\\Users\\Admin\\Videos\\4K Video Downloader\\Full Song KHAIRIYAT.mp4"
            os.startfile(puchoPath)


        # About the time and date
        elif 'the time' in friend:
            strTime = datetime.datetime.now().strftime("%I hour %M minutes and %S seconds %p")
            print(f'Sir, the time is {strTime}')
            speak(f"Sir, the time is {strTime}")

        elif 'the date' in friend:
            strTime = datetime.datetime.now().strftime("%d day %m month and %y year")
            print(f'Sir, today is {strTime}')
            speak(f"Sir, today is {strTime}")

        elif 'the hour' in friend:
            strTime = datetime.datetime.now().strftime("%H")
            print(f'Sir, the hour is {strTime}')
            speak(f"Sir, the hour is {strTime}")

        elif 'the month' in friend:
            strTime = datetime.datetime.now().strftime("%m")
            print(f'Sir, the month is {strTime}')
            speak(f"Sir, the month is {strTime}")

        elif 'the week' in friend:
            strTime = datetime.datetime.now().strftime("%w")
            print(f'Sir, the week is {strTime}')
            speak(f"Sir, the week is {strTime}")

        elif 'the year' in friend:
            strTime = datetime.datetime.now().strftime("%y")
            print(f'Sir, the year is {strTime}')
            speak(f"Sir, the year is {strTime}")

        # About my and it self

        elif 'how are you' in friend:
            speak("I am very fine and well, thank you sir, how are you?")

        elif 'kishor' in friend:
            speak("Hallo young friends. I'm Kishor Pasha from Rokey Beach, America. The place"
                  "is in the loss angales, near at pacific ocian. And the place"
                  "in't far from Holly Wood. Those who don't know who we are, saying"
                  " them, we, three friends created an intelligence egency. Called Tin goyenda."
                  "I'm Bengali. Live with uncle and aunt. My one friend's name is 'Musa' 'Aman',"
                  "Muscle hero, the american negro. My another friend is Robin Mlfourd, Irish american,"
                  "book lover. we read in the same class. In the Pasha salvage yard, under the"
                  "metal rubbish, in an mobile home, we have a head quarter. we are going to solve"
                  "three story, You may stay with us")

        elif 'area' in friend:
            speak("Juairia Tasnim is Umars nefew and his sisters dawghter. He is 10 years old"
                  "Her mothers name is Masheta. And Her fathers name is Arifuz zaman Khandakar")

        elif 'juweria' in friend:
            speak("Juairia Tasnim is Umars nefew and his sisters dawghter. He is 10 years old"
                  "Her mothers name is Masheta. And Her fathers name is Arifuz zaman Khandakar")

        elif 'i am also fine' in friend:
            speak("Oh, thank god")

        elif 'i am very fine' in friend:
            speak("Oh, thank god")

        elif 'i am fine' in friend:
            speak("Oh, thank god")

        elif 'salam' in friend:
            speak("Assalamu Alaikum")

        elif 'chup' in friend:
            speak("Sorry sir")

        elif 'thank you' in friend:
            speak("Most well come")

        elif 'what is your name' in friend:
            speak("My name is Bondhu")

        elif 'who are you' in friend:
            speak('I am a  Robot, which is made by Umar Chowdhury')

        elif 'who is aryan' in friend:
            speak('Aryan Chowdhury is a cousin brother of Umar, His fathers name in Shumon, and mothers name is assia')

        elif 'umar' in friend:
            speak('Umar Chowdhury has made me, he is the 7th son of Golam Mawla Chowdhury, They are 3 brothers'
                  ' and 4 sisters, his mothers name is Parvin Chowdhury')

        elif 'if' in friend:
            speak('Rofath Islam Radif is Umars nephew, his fathers name is Rejaul, they are 3 brothers'
                  'they live in thana ghat, shahzadpur, sirajganj, he read in sopto borno model school,')

        elif 'Javed' in friend:
            speak('Jawad hossain, is umars nephew, his fathers name is millon, he is only him,'
                  'he live in ruppur, shahzadpur, sirajganj, he reads in soptoborno model school')

        elif 'fahim' in friend:
            speak('Fahim is umars cousin, and his fathers name is md, shafiqul islam, and'
                  'his mothers name is farida, they live in dhaka')

        elif 'fahad' in friend:
            speak('Fahad is umars cousin, and his fathers name is md, shafiqul islam, and'
                  'his mothers name is farida, they live in dhaka')

        elif 'mashkura' in friend:
            speak('Mashkura Chowdhury is the 6th daughter of Golam Mawla Chowdhury and Umars elder sister')

        elif 'sumaiya' in friend:
            speak('Sumaiya Chowdhury is the 5th daughter of Golam Mawla Chowdhury and Umars elder sister')

        elif 'tania' in friend:
            speak('Tania Chowdhury is the 4th daughter of Golam Mawla Chowdhury and Umars elder sister')

        elif 'masheta' in friend:
            speak('masheta Chowdhury is the 4th daughter of Golam Mawla Chowdhury and Umars elder sister')

        elif 'farooq' in friend:
            speak('Faruk Abdullah Chowdhury is the 3rd son of Golam Mawla Chowdhury and Umars elder sister')

        elif 'bubli' in friend:
            speak('Bubli Chowdhury is the 2nd daughter of Golam Mawla Chowdhury and Umars elder sister')

        elif 'mahfuza' in friend:
            speak('Mahfuza Chowdhury is the 2nd daughter of Golam Mawla Chowdhury and Umars elder sister')

        elif 'gulam' in friend:
            speak('Golam Mawla Chowdhury is the 1st son of Abul Maqsud Chowdhury, he is Umars father')

        elif 'mohinuddin' in friend:
            speak('Muhiuddin Hossain Mahdi is Umars nephew and his fathers name is Abdur Rahman and'
                  ' his mothers name is Mahfuza')

        elif 'who has made you' in friend:
            speak('Umar Chowdhury has made me')

        elif 'abdul rahman' in friend:
            speak('Abdur Rahman is Umars elder brother in law and mahfuzas husband')

        elif 'ananta' in friend:
            speak('Anonto Mostofa is a cadet and brilliant student of SMS')

        elif 'masoom' in friend:
            speak('Masum billa is a very brilliant student of soptoborno model school, He reads in class eight.'
                  ' he is so fatty')

        elif 'niloy' in friend:
            speak('Niloy is a brilliant student of sms, he is so tall and not fatty')

        # About It's brain

        elif 'english' in friend:
            speak("English is a West Germanic language of the Indo-European language family, with its earliest"
                  " forms spoken by the inhabitants of early medieval England.[3][4][5] It is named after"
                  " the Angles, one of the ancient Germanic peoples that migrated to the island of Great Britain."
                  " Modern English grammar is the result of a gradual change from a typical Indo-European"
                  " dependent-marking pattern, with a rich inflectional morphology and relatively free"
                  " word order, to a mostly analytic pattern with little inflection, and a fairly fixed"
                  " subject–verb–object word order.")

        elif 'bengali' in friend:
            speak("Bengali ( ben-GAW-lee), generally known by its endonym"
                  " Bangla (বাংলা, Bengali pronunciation: [ˈbaŋla]), is an"
                  " Indo-Aryan language native to the Bengal region of "
                  "South Asia")

        elif 'Ishwar Chandra Vidyasagar' in friend:
            speak("Ishwar Chandra Vidyasagar CIE (Bengali: ঈশ্বর চন্দ্র বিদ্যাসাগর; 26 September 1820 – 29 July 1891)"
                  ", born Ishwar Chandra Bandyopadhyay, was an Indian educator and social reformer of"
                  " the nineteenth century.")

        elif 'the sun' in friend:
            speak('The sun is the main character of the solar system')

        elif 'how many countries in the world' in friend:
            speak("There ar 204 countries in the world")

        elif 'samsung galaxy' in friend:
            speak("The Samsung Galaxy S6 is a line of Android-based smartphones manufactured, released"
                  " and marketed by Samsung Electronics. Succeeding the Samsung Galaxy S5, the S6 was"
                  " not released as a singular model, but instead in two variations unveiled and marketed"
                  " together—the Galaxy S6 and Galaxy S6 Edge—with the latter differentiated primarily by"
                  " having a display that is wrapped along the sides of the device. The S6 and S6 Edge"
                  " were unveiled on March 1, 2015, during the Samsung Unpacked press event at MWC"
                  " Barcelona, and released April 10, 2015, marking a counter-utilitarian and "
                  "fashion-oriented course in the Galaxy S series.")

        elif 'plant vs zombie' in friend:
            speak("plant vs zombies is an electronic art based game that made by 'POP CAP' game pregents."
                  "that is very popular game in out world. It's also popular for the child of 2000 to 2019"
                  ". It becomes as popular as all other popular games in only nine month")



        elif 'galaxy' in friend:
            speak("We live in A galaxy. Called Chayapoth")

        elif 'rayen' in friend:
            speak("Rayen is a brilliun student of soptoborno model"
                  "school")

        elif 'earth' in friend:
            speak("earth is a planet of zero on galaxy that we live")

        elif 'where do you live' in friend:
            speak("I live in Dwariapur, Shahzadpur, Sirajganj")

        elif 'your country name' in friend:
            speak("My country's name is Bangladesh")

        elif 'who is your creator' in friend:
            speak("My creator is Allah")

        elif 'who is our prime minister' in friend:
            speak("Our prime minister is Sheikh Hasina")

        elif 'who is our president' in friend:
            speak("Our president is Abdul Hamid Advocate")

        elif 'how old are you' in friend:
            speak("I am 1 years old")

        elif 'what do you eat' in friend:
            speak("I eat electricity")

        elif 'what is your software name' in friend:
            speak("My software name is Pycharm")

        elif 'who is the inventor of computer' in friend:
            speak("The invent of computer is stive jobs")

        elif 'how many district' in friend:
            speak("There are 64 districts in bangladesh")

        elif 'how many division' in friend:
            speak("There are 8 division in bangladesh")

        elif 'solar system' in friend:
            speak("Solar system is a kind of thing that is gura ghuri")

        elif 'which word contains five vowel' in friend:
            speak("'education' is the word, which contains five vowel")

        elif 'how many people in bangladesh' in friend:
            speak("My creator is Umar Chowdhury")

        elif 'which song do you like most' in friend:
            speak("I most like Lily by alane walker")

        elif 'what song do you like' in friend:
            speak("I most like Lily by alane walker.")

        elif 'destroy' in friend:
            speak("No, never")

        elif 'bangladesh' in friend:
            speak('Bangladesh is an independent country of Asia. Its independence on 16 December in 1971 from Pakistan.'
                  ' Dhaka is the largest and capital of the country. Bey Of Bengle is the bay of the country.'
                  ' It has 64 districts and 68000 villages. It has 8 education boards and 7 divisions,'
                  ' Dhaka, Chattogrm(chottogram), Barishal(borishal), Sylhet(silet), Rajshahi(rajshahi),'
                  ' Mymanshingh(moymonshingh), Jashar(joshor), Rangpur(rongpur), Khulna(khulna)')

        elif 'dhaka' in friend:
            speak('Dhaka is the capital and largest city of Bangladesh. It is the main division of Bangladesh.'
                  ' There are 13 districts in this division. The districts of the divission is, Dhaka, Faridpur,'
                  'Gazipur, Gopalganj, Kishorganj, Manikganj, Madaripur, Munsiganj, Norshingdi, Narayonganj,'
                  ' Rajbari, Shariyatpur, Tangail')

        elif 'rajshahi' in friend:
            speak('Rajshahi division is a popular division of Bangladesh. There are 8 districts in this division. '
                  'The districts of the division is, Bogra, Jaypurhat, Chapai Nawabganj, Naogaon, Nator, Pabna,'
                  ' Rajshahi, Shirajganj')

        elif 'rangpur' in friend:
            speak('Rangpur division is a popular division of Bangladesh. There are 8 districts in this division. '
                  'The districts of the division is, Dinajpur, Gaibandha, Kurigram, Lalmonirhat, Nilfamari,'
                  ' Panchagar, Rangpur, Thakurgaon')

        elif 'chattogram' in friend:
            speak('division is a popular division of Bangladesh. There are 11 districts in this division. '
                  'The districts of the division is, Bandarban, Khagrachori, Rangamati, Chattogram, Coxbazar, '
                  'Bramhonbariya, Chadpur, Kumilla, Fenei, Lakkhipur, Nawakhali')

        elif 'khulna' in friend:
            speak('Khulna division is a popular division of Bangladesh, There are 10 districts in this division. '
                  'The districts of the division is, Bagerhat, Chuadanga, Jashar, Jhinaidah, Khulna, Kushtia, '
                  'Magura, Meherpur, Narail, Shatkhira')

        elif 'barishal' in friend:
            speak('Barishal division is a popular division of Bangladesh, There are 6 districts in this division. '
                  'The districts of the division is, Barishal, Barguna, Vola, Jhalokathi, Potuakhali, Pirojpur')

        elif 'maymanshingh' in friend:
            speak('Maymanshingh division is a popular division of Bangladesh, There are 4 districts in this division. '
                  'The districts of the division is, Jamalpur, Maymanshingh, Netrokona, Sherpur')

        elif 'sylhet' in friend:
            speak('Sylhet division is a popular division of Bangladesh, There are 4 districts in this division. '
                  'The districts of the division is, Hobiganj, Moulovibazar, Shunamganj, Sylhet')

        elif 'shahzadpur' in friend:
            speak('Shahzadpur is The Bigger upozela of Shirajganj, It is popular for Shari of Loom machine'
                  'There are 4 days sits a hut and as a fair of Shari or wear')

        elif 'sirajganj' in friend:
            speak('Shirajganj is a popular district of Rajshahi '
                  'division in Bangladesh')

        # Short forms

        elif 'what is sms' in friend:
            speak('The short form of Shoptoborno Model School is sms, The another short form of Short Message'
                  ' Service called sms')

        elif 'what is psc' in friend:
            speak('The short form of Primary School Certificate called PSC'
                  ' service is sms')

        elif 'what is pec' in friend:
            speak('The short form of Primary Education completion examination Certificate called PEC')

        elif 'what is jsc' in friend:
            speak('The short form of Junior School Certificate called JSC')

        elif 'when do you born' in friend:
            speak('I born in 2022, 25th January')

        elif 'what is jdc' in friend:
            speak('The short form of Junior Dakhil Certificate called JEC')

        elif 'who is the prophet of muslim' in friend:
            speak("The Companions of the Prophet (Arabic: اَلصَّحَابَةُ; aṣ-ṣaḥāba meaning 'the"
                  " companions', from the verb صَحِبَ meaning 'accompany', 'keep company with',"
                  " 'associate with') were the disciples and followers of Muhammad who 'saw or"
                  " met the prophet during his lifetime, while being a Muslim and were physically"
                  " in his presence'")

        elif 'who is the prophet of us' in friend:
            speak("The Companions of the Prophet (Arabic: اَلصَّحَابَةُ; aṣ-ṣaḥāba meaning 'the"
                  " companions', from the verb صَحِبَ meaning 'accompany', 'keep company with',"
                  " 'associate with') were the disciples and followers of Muhammad who 'saw or"
                  " met the prophet during his lifetime, while being a Muslim and were physically"
                  " in his presence'")

        elif 'what is ssc' in friend:
            speak('The short form of School School Certificate called SSC')

        elif 'what is bbc' in friend:
            speak('The short form of British Broadcast called BBC')

        elif 'what is mbbs' in friend:
            speak('The short form of Bachalor of Medicine, Bachalor of sergery is MBBS')

        elif 'what is hsc' in friend:
            speak('The short form of Hair Secondary of School Certificate called HSC')

        elif 'sir' in friend:
            speak('Moyeen sir is the chairman and the teacher of Soptoborno Model school')

        elif 'wifi' in friend:
            speak('The short form of Wireless fedeelity is called wi-fi')

        elif 'what is your school' in friend:
            speak('I read in Shoptoborno model school. Soptoborno model school is thw largest school'
                  ' in shahzadpur, There is three thougence +'
                  'students, and , the students of it are very good and brilliunt, there is a Dream Land'
                  ' Called Shopno rajjo, here small boys and girls playes and enjoys school life')

        elif 'what school do you read' in friend:
            speak('I read in Shoptoborno model school. Soptoborno model school is thw largest school'
                  ' in shahzadpur, There is three thougence +'
                  'students, and , the students of it are very good and brilliunt, there is a Dream Land'
                  ' Called Shopno rajjo, here small boys and girls playes and enjoys school life')

        elif 'school' in friend:
            speak('I read in Shoptoborno model school. Soptoborno model school is thw largest school'
                  ' in shahzadpur, There is three thougence +'
                  'students, and , the students of it are very good and brilliunt, there is a Dream Land'
                  ' Called Shopno rajjo, here small boys and girls playes and enjoys school life')


        elif 'bangabandhu sheikh mujibur rahman' in friend:
            speak("Sheikh Mujibur Rahman (Bengali: shekh mujibur rohhman; 17 March 1920 – 15 August 1975)"
                  ", often shortened as Sheikh Mujib or Mujib and widely known as Bangabandhu was "
                  "a Bangladeshi politician, statesman and Founding Father of Bangladesh who served"
                  " as the first President and later as the Prime Minister of Bangladesh from April"
                  " 1971 until his assassination in August 1975. Mujib is credited with leading the "
                  "successful campaign for Bangladesh's independence from Pakistan. He is revered "
                  "in Bangladesh with the honourific title of 'Bangabandhu' (Bongobondhu 'Friend"
                  " of Bengal') which is used around the world.")

        elif 'bangabandhu' in friend:
            speak("Sheikh Mujibur Rahman (Bengali: shekh mujibur rohhman; 17 March 1920 – 15 August 1975)"
                  ", often shortened as Sheikh Mujib or Mujib and widely known as Bangabandhu was "
                  "a Bangladeshi politician, statesman and Founding Father of Bangladesh who served"
                  " as the first President and later as the Prime Minister of Bangladesh from April"
                  " 1971 until his assassination in August 1975. Mujib is credited with leading the "
                  "successful campaign for Bangladesh's independence from Pakistan. He is revered "
                  "in Bangladesh with the honourific title of 'Bangabandhu' (Bongobondhu 'Friend"
                  " of Bengal') which is used around the world.")

        elif 'bangabandhu sheikh mujib' in friend:
            speak("Sheikh Mujibur Rahman (Bengali: shekh mujibur rohhman; 17 March 1920 – 15 August 1975)"
                  ", often shortened as Sheikh Mujib or Mujib and widely known as Bangabandhu was "
                  "a Bangladeshi politician, statesman and Founding Father of Bangladesh who served"
                  " as the first President and later as the Prime Minister of Bangladesh from April"
                  " 1971 until his assassination in August 1975. Mujib is credited with leading the "
                  "successful campaign for Bangladesh's independence from Pakistan. He is revered "
                  "in Bangladesh with the honourific title of 'Bangabandhu' (Bongobondhu 'Friend"
                  " of Bengal') which is used around the world.")

        elif 'sheikh mujibur rahman' in friend:
            speak("Sheikh Mujibur Rahman (Bengali: shekh mujibur rohhman; 17 March 1920 – 15 August 1975)"
                  ", often shortened as Sheikh Mujib or Mujib and widely known as Bangabandhu was "
                  "a Bangladeshi politician, statesman and Founding Father of Bangladesh who served"
                  " as the first President and later as the Prime Minister of Bangladesh from April"
                  " 1971 until his assassination in August 1975. Mujib is credited with leading the "
                  "successful campaign for Bangladesh's independence from Pakistan. He is revered "
                  "in Bangladesh with the honourific title of 'Bangabandhu' (Bongobondhu 'Friend"
                  " of Bengal') which is used around the world.")

        elif 'sheikh mujib' in friend:
            speak("Sheikh Mujibur Rahman (Bengali: shekh mujibur rohhman; 17 March 1920 – 15 August 1975)"
                  ", often shortened as Sheikh Mujib or Mujib and widely known as Bangabandhu was "
                  "a Bangladeshi politician, statesman and Founding Father of Bangladesh who served"
                  " as the first President and later as the Prime Minister of Bangladesh from April"
                  " 1971 until his assassination in August 1975. Mujib is credited with leading the "
                  "successful campaign for Bangladesh's independence from Pakistan. He is revered "
                  "in Bangladesh with the honourific title of 'Bangabandhu' (Bongobondhu 'Friend"
                  " of Bengal') which is used around the world.")

        elif 'stop' in friend:
            print('stopping it...')
            speak('stopping it')
            sys.exit()

        elif 'close' in friend:
            print('closing it...')
            speak('closing it')
            sys.exit()

        elif 'exit' in friend:
            print('closing it...')
            speak('closing it')
            sys.exit()

        elif 'whats your name' in friend:
            speak('My name is bondhu')

        elif 'brain' in friend:
            speak('Searching my brain...')
            print('Searching my brain...')
            friend = friend.replace("brain", "")
            friend = friend.replace("your", "")
            friend = friend.replace("search", "")
            friend = friend.replace("from", "")
            friend = friend.replace("what is", "")
            friend = friend.replace("who is", "")
            results = wikipedia.summary(friend, sentences=3)
            speak("According to my brain")
            print("According to my brain...")
            print(results)
            speak(results)


        elif 'search' in friend:
            print("Please wait...")
            speak("Please wait...")
            friend = friend.replace("search", "")
            friend = friend.replace("about", "")
            friend = friend.replace("in", "")
            friend = friend.replace("play", "")
            friend = friend.replace("please", "")
            friend = friend.replace("open", "")
            pywhatkit.search(friend)

        elif 'youtube' in friend:
            friend = friend.replace("search", "")
            friend = friend.replace("youtube", "")
            friend = friend.replace("in", "")
            friend = friend.replace("play", "")
            friend = friend.replace("please", "")
            friend = friend.replace("open", "")
            print("Opening " + friend + "in youtube")
            speak("Opening " + friend + "in youtube")
            pywhatkit.playonyt(friend)