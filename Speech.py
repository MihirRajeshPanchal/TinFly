# #import library
# import speech_recognition as sr
# #Initiаlize  reсоgnizer  сlаss  (fоr  reсоgnizing  the  sрeeсh)
# r = sr.Recognizer()
# # Reading Audio file as source
# #  listening  the  аudiо  file  аnd  stоre  in  аudiо_text  vаriаble
# with sr.Microphone() as source:
#     audio_text = r.listen(source,phrase_time_limit=5)
# # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
#     try:
#         # using google speech recognition
#         text = r.recognize_google(audio_text)
#         print('Converting audio transcripts into text ...')
#         print(text)
#     except:
#          print('Sorry.. run again...')

# import speech_recognition as sr

# r = sr.Recognizer()

# with sr.Microphone() as source:
#         r.adjust_for_ambient_noise(source=source)
#         audio = r.listen(source)
        
#         data = ''
#         try :
#             data = r.recognize_google(audio)
#             print(data)

#         except sr.UnknownValueError:
#             print(" Error")
            
#         except sr.RequestError as e:
#             print("Request Error")

# r=sr.Recognizer()
# print(sr.Microphone.list_microphone_names())
# with sr.Microphone() as source:
#     r.adjust_for_ambient_noise(source,duration=1)
#     # r.energy_threshold()
#     print("say anything : ")
#     audio= r.listen(source)
#     try:
#         text = r.recognize_google(audio)
#         print(text)
#     except:
#         print("sorry, could not recognise")

# import speech_recognition as sr
# r = sr.Recognizer()
# with sr.Microphone() as source:                # use the default microphone as the audio source
#     audio = r.adjust_for_ambient_noise(source,5) # listen for 1 second to calibrate the energy threshold for ambient noise levels
#     audio = r.listen(source)                   # now when we listen, the energy threshold is already set to a good value, and we can reliably catch speech right away

# try:
#     print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
# except LookupError:                            # speech is unintelligible
#     print("Could not understand audio")

# import speech_recognition as sr
# def callback(recognizer, audio):                          # this is called from the background thread
#     try:
#         print("You said " + recognizer.recognize(audio))  # received audio data, now need to recognize it
#     except LookupError:
#         print("Oops! Didn't catch that")
# r = sr.Recognizer()
# r.listen_in_background(sr.Microphone(), callback,phrase_time_limit=5)

# import time
# while True: time.sleep(0.1) 
import speech_recognition as sr
import pyaudio 
import sounddevice as sd
a = sd.query_devices()
print (a)
r = sr.Recognizer()

while True:
    with sr.Microphone(device_index=2) as source:
        print('say....')
        audio = r.listen(source)
        voice_data = r.recognize_google(audio, language = 'en-IN', show_all = True)
        print(voice_data)