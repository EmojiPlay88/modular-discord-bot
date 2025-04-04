import discord

def getLanguages():
    availableLanguages = []
    for dir in os.listdir('./translations'):
        availableLanguages.append(dir)
    return availableLanguages

def openLanguageFile(language:str):
    filename = os.path.basename(__file__)
    with open(f'./translations/{language}/{filename}.jso>
        return file.read().json()
