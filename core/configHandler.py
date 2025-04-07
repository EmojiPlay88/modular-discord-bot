import configparser
import os

class Config():
    def __init__(self, path:str):
        self.config = configparser.ConfigParser()
        if not os.path.exists(path):
            raise FileNotFoundError(f"Config file {path} not found.")
        self.config.read(path)

    def returnConfig(self):
        return {section: dict(self.config[section]) for section in self.config.sections()}