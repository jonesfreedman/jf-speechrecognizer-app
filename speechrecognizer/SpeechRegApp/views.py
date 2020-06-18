from django.shortcuts import render
from SpeechRegApp.speech import SpeechRecognition
from django.http import HttpRequest

# Create your views here.
def index(request):
    SpeechRecognition()
    return render(request, "index.html", {})


def speech(request):
    # start(request)
    return render(request, "SpeechRecognition.html")


def speechText(data):
    text = data
    print("Displayed from View " + text)


# def start(request):
#    if(request.GET.get('btnStartSpeech')):
#       SpeechRecognition()
