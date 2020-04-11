# this is a program that helps you Journal while doing software development
from arbitrary_dateparser import DateParser
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory

start()


parser = None
def start():
    # showOptions()
    parser = DateParser();
    
    while 1:
        user_input = prompt('>',
                            history=FileHistory('history.txt'),
                            auto_suggest=AutoSuggestFromHistory(),
                        )
        print(user_input)




def appendToFile(filename,string):
    #make a new file 
    pass

def timeBetween(start,end):
