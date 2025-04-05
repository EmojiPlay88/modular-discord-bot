import discord
import os
import json

def getLanguages():
    availableLanguages = []
    for dir in os.listdir('./translations'):
        availableLanguages.append(dir)
    return availableLanguages

def openLanguageFile(filename:str, language:str):
    with open(f'./translations/{language}/{filename}.json') as file:
        file = json.dumps(file.read())
        return file