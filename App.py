# this is a program that helps you Journal while doing software development
from arbitrary_dateparser import DateParser
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory


class myclasss():
    
    def getInput():
        user_input = prompt('==>',history=FileHistory('history.txt'),auto_suggest=AutoSuggestFromHistory())
        return user_input        


    def start():
        print("Hi welcome! how are you?")
        # showOptions()
        parser = DateParser()
        

    def appendToFile(filename,string):
        #make a new file 
        pass

    def timeBetween(start,end):
        pass





