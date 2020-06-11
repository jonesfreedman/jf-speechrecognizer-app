import speech_recognition as sr 
import pyttsx3  
import webbrowser  
import os, glob
import requests
import SpeechRegApp.constants

r = sr.Recognizer()  
textAudio = ""
print("Hello " + os.getlogin())

def SpeakText(command): 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait()

def Open(textAudio):
    splitText = textAudio.split()
    query = ''

    # print(os.path.join(os.environ["ALLUSERSPROFILE"]))

    if "github" in textAudio or "git" in textAudio or "repo" in textAudio or "repository" in textAudio:
        if(len(splitText) == 2):
            webbrowser.open_new_tab("https://github.com/")
        else:
            if(len(splitText) > 1):
                query += splitText[1]
            print("Query is: " + query)
            response = requests.get("https://api.github.com/search/repositories?q="+ query +"+org:jonesfreedman")
            if(response.status_code == 200):
                data = response.json()
                if(data["total_count"] > 0):
                    items = data["items"]
                    htmlUrl = items[0]["html_url"]
                    webbrowser.open_new_tab(htmlUrl)
                else:
                    print("The requested repository could not be found.")
            else:
                    print("Server Error.")
    elif "youtube" in textAudio:
        webbrowser.open_new_tab("https://youtube.com/")
    elif "facebook" in textAudio:
        webbrowser.open_new_tab("https://facebook.com/")
    elif "cloud" in textAudio or "pcf" in textAudio:
        webbrowser.open_new_tab("https://console.run.pivotal.io/")
    elif "google" in textAudio:
        webbrowser.open_new_tab("https://google.co.in")
    elif "jenkins" in textAudio or "pipeline" in textAudio or "pipe" in textAudio:
        webbrowser.open_new_tab("https://www.jenkins.io/")
    elif "rally" in textAudio:
        webbrowser.open_new_tab("https://www.broadcom.com/products/software/agile-development/rally-software")
    elif "excel" in textAudio:
        os.startfile("excel")
    elif "powerpoint" in textAudio or "ppt" in textAudio:
        os.startfile("powerpnt")
    elif "paint" in textAudio:
        os.startfile("mspaint")
    elif "outlook" in textAudio:
        os.startfile("outlook")
    elif "visual studio" in textAudio or "vs" in textAudio:
        if "2019" in textAudio or "20 Ninteen" in textAudio or "Ninteen" in textAudio or "19" in textAudio or "visual studio" in textAudio:
            os.startfile("devenv")
    elif "calculator" in textAudio:
        os.startfile("calc")
    else:
        print("Could not find any item that matches the search criteria.")

def Find(textAudio):
    splitText = textAudio.split()
    query = ""
    if(len(splitText) > 1):
        query += splitText[1]
    if(len(splitText) > 2):
        query += splitText[2]
    if(len(splitText) > 3):
        query += splitText[3]
    if(len(splitText) > 4):
        query += splitText[4]
    print("Searching file: " + query)
    print("This may take some time..")
    found = False
    numberOfFilesFound = 0
    for root, dirs, files in os.walk(r'C:\Users\user\Desktop'): 
        for file in files:  
            if file.endswith('.txt') or file.endswith('.docx'): 
                if query in file.lower():
                    os.startfile(root+'/'+str(file))
                    found = True
                    numberOfFilesFound = numberOfFilesFound + 1
    print("{} files found".format(numberOfFilesFound))
    if(found == False):
        print("File not found.")
    # for root, dirs, files in os.walk(''):
    #     print ("searching", root)
    #     if query in files:
    #         print ("found: %s" % join(root, query))
    #         os.startfile(query)  
    #         break
    # print(os.path.isfile(query))
    # if(os.path.isfile(query)):
    #     os.startfile(query)    

def SpeechRecognition():
    while(1):     
        try: 
            print('Please speak')
            with sr.Microphone() as source: 
                r.adjust_for_ambient_noise(source, duration=1) 
                audio1 = r.record(source, duration=3) 
                textAudio = r.recognize_google(audio1) 
                textAudio = textAudio.lower()
                print("Request received: " + textAudio) 
                if "open" in textAudio: 
                    Open(textAudio)

                if "find" in textAudio: 
                    Find(textAudio)

                if "send a mail" in textAudio or "send mail" in textAudio or "send email" in textAudio or "send an email" in textAudio:
                    Open(textAudio)

                if "exit" in textAudio or "stop" in textAudio:
                    exit()
            
            SpeakText(textAudio) 
            SpeechRegApp.views.speechText(textAudio)

        except sr.RequestError as e: 
            print("Could not request results; {0}".format(e)) 

        except sr.UnknownValueError: 
            print("Listening..") 


      
