import configparser
import os

class Config():
    def __init__(self, path:str):
        self.config = configparser.ConfigParser()
        self.path = path
        if not os.path.exists(path):
            raise FileNotFoundError(f"Config file {path} not found.")

    def returnConfig(self):
        self.config.read(self.path)
        return {section: dict(self.config[section]) for section in self.config.sections()}

    def writeConfig(self):
        with open(self.path, "w") as file:
            self.config.write(file)
