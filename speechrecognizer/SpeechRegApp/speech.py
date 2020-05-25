import speech_recognition as sr 
import pyttsx3  
import webbrowser  
import os, glob
import requests
  
r = sr.Recognizer()  

def SpeakText(command): 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait()

def OpenWebsites():
    while(1):     
        try: 
            print('Speak')
            with sr.Microphone() as source: 
                r.adjust_for_ambient_noise(source, duration=1) 
                audio1 = r.record(source, duration=3) 
                textAudio1 = r.recognize_google(audio1) 
                textAudio1 = textAudio1.lower()
                # for name in os.listdir("."):
                #     if name.endswith(".txt"):
                #         os.startfile(name)
                #         print(name)

                # for root, dirs, files in os.walk("."):
                #     for filename in files:
                #         print(filename)

                # for fn in glob.glob("*.exe"):
                #     print(fn)

                # for name in os.listdir("C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/Common7/IDE"):
                #     if name.endswith(".exe"):
                #         print(name)
               
                # for file in glob.glob("*.txt"):
                #     print(file)


                if "open" in textAudio1: 
                    splitText = textAudio1.split()
                    query = ''
                    if "github" in textAudio1 or "git" in textAudio1 or "repo" in textAudio1 or "repository" in textAudio1:
                        if(len(splitText) == 2):
                            webbrowser.open_new_tab("https://github.com/")
                        else:
                            if(len(splitText) > 1):
                                query += splitText[1]
                            # if(len(splitText) > 3):
                            #     query += splitText[3]
                            # if(len(splitText) > 4):
                            #     query += splitText[4]
                            print("Query is: " + query)
                            response = requests.get("https://api.github.com/search/repositories?q="+ query +"+org:jonesfreedman")
                            if(response.status_code == 200):
                                data = response.json()
                                if(data["total_count"] > 0):
                                    items = data["items"]
                                    # repos = items[0]["repository"]
                                    htmlUrl = items[0]["html_url"]
                                    webbrowser.open_new_tab(htmlUrl)
                                else:
                                    print("The requested repository could not be found.")
                    if "youtube" in textAudio1:
                        webbrowser.open_new_tab("https://youtube.com/")
                    if "facebook" in textAudio1:
                        webbrowser.open_new_tab("https://facebook.com/")
                    if "cloud" in textAudio1:
                        webbrowser.open_new_tab("https://console.run.pivotal.io/")
                    if "google" in textAudio1:
                        webbrowser.open_new_tab("https://google.co.in")
                    if "jenkins" in textAudio1 or "pipeline" in textAudio1 or "pipe" in textAudio1:
                        webbrowser.open_new_tab("https://www.jenkins.io/")
                    if "rally" in textAudio1:
                        webbrowser.open_new_tab("https://www.broadcom.com/products/software/agile-development/rally-software")
                    if "excel" in textAudio1:
                        os.system("start excel.exe")
                    if "powerpoint" in textAudio1 or "ppt" in textAudio1:
                        os.system("start powerpnt.exe")
                    if "paint" in textAudio1:
                        os.system("start mspaint.exe")
                    if "visual studio" in textAudio1 or "vs" in textAudio1:
                        if "2019" in textAudio1 or "20 Ninteen" in textAudio1 or "Ninteen" in textAudio1 or "19" in textAudio1 or "visual studio" in textAudio1:
                            os.system("start devenv.exe")
                            
                        # if "code" in textAudio1:
                        #     os.system("start code.exe")
                # if "find" in textAudio1: 
                #     splitText = textAudio1.split()
                #     query = ""
                #     if(len(splitText) > 1):
                #         query += splitText[1]
                #     if(len(splitText) > 2):
                #         query += splitText[2]
                #     if(len(splitText) > 3):
                #         query += splitText[3]
                #     if(len(splitText) > 4):
                #         query += splitText[4]
                #     print("Searching file: " + query)
                #     print("This may take some time..")

                #     for root, dirs, files in os.walk('D:\\'):
                #         print ("searching", root)
                #         if query in files:
                #             print "found: %s" % join(root, query)
                #             os.startfile(query)  
                #             break
                #     print(os.path.isfile(query))
                #     if(os.path.isfile(query)):
                #         os.startfile(query)    
                if "exit" in textAudio1 or "stop" in textAudio1:
                    exit()
            print(textAudio1) 
            SpeakText(textAudio1) 
        except sr.RequestError as e: 
            print("Could not request results; {0}".format(e)) 
        except sr.UnknownValueError: 
            print("Listening..") 

OpenWebsites()  


      
