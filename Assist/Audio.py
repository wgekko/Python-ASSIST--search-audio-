#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 20:38:24 2022

@author: walter
"""
# este programa se desarrolla de acuerdo a un tutorial de Udemy - de Nick Germaine


import pyaudio
import wave
import speech_recongnition as sr
import subprocess
from Command import Commander

running = True

def say(text):
    subprocess.call('say' + text, shell=True)
    


def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.Pyaudio()
    
    stream = pa.open(
            format = pa.get_format_from_with(wf.getsampwith()),
            channels= wf.getnchannels(),
            rate = wf.getframerate(),
            output=True
            )
    
    data_stream = wf.readframes(chunk)
    
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframe(chunk)
    
    stream.close()
    pa.terminate()
    
#play_audio("./audio/audio_end.wav")

r = sr.Recognizar()
cmd = Commander()

def initSpeech():
    print("Listening.....")
    play_audio("./audio/audio_initiate.wav")
    
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
    
    play_audio("./audio/audio_end.wav")
    
    command = ""
    try:
        command = r.recognize_google(audio)
        
    except: 
        print("Couldn't understand you, Bro...")
        
    print("Your command :")
    print(command)
    if command == ["quit", "bye", "exit", "good-bye"]:
        global running
        running = False
    
    cmd.discover(command)
    
    # say("You said : " + command)

while running:    
    initSpeech()




        

