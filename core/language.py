import os
import json

def getLanguages():
    availableLanguages = []
    for dir in os.listdir('/translations'):
        availableLanguages.append(dir)
    return availableLanguages

class TranslationFile:
    def __init__(self, path: str):
        self.path = path
        with open(path, "r") as file:
            self.prompts = json.load(file)