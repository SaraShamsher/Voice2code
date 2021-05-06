import speech_recognition as sr
mic = sr.Microphone()
recog = sr.Recognizer()
with mic as audio_file:
    print("Speak Please")

    flag = False
    quote = False
    flag_range = False
    flag_space=False
    flag_nospace = False
    
    while True:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)

        try:
            speech = recog.recognize_google(audio)
            speech = speech.split( )
            d={'equals': '=','plus':'+','minus':'-','multiply':'*','divide':'//'}
            s=''
            space='    '
            num=['1','2','3','4','5','6','7','8','9','10']
            

            if flag_space:
                print(space, end="")
                
            for i in speech:
                if i == 'equals':
                    s += d['equals']
                elif i == 'print':
                    s += 'print( '
                    flag = True
                elif i == "string" and flag == True:
                    s += "'"
                    quote = True
                elif i == 'plus':
                    s += d['plus']
                elif i == 'minus':
                    s += d['minus']
                elif i == 'multiply':
                    s += d['multiply']
                elif i == 'divide':
                    s += d['divide']
                elif i == 'if':
                    s += 'if:'
                    flag_space=True
                elif i == 'while':
                    s += 'while:'
                    flag_space=True
                elif i == 'close':
                    flag_space = False
                    flag_range = False
                    flage_nospace = True
                elif i == 'range':
                    s += 'range('
                    flag_range = True
                    flag_space=True
                elif i in num and flag_range == True:
                    s += i + '):'
                    flag_range = False
                else:
                    s+=i + " "
            
            
            if flag and quote:
                print(s + "')")
            elif flag:
                print(s + ')')
            #elif flag_space:
                #print(space+s)
            elif flag_nospace:
                print(s)
            else:
                print(s)
            #print("You said: " + recog.recognize_google(audio))
        except Exception as e:
            exit(0)
