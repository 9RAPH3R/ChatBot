from chatterbot.trainers import ListTrainer
from tkinter import *
from chatterbot import ChatBot
import tkinter as tk
try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.scrolledtext as ScrolledText
import time
import os

class TkinterGUIExample(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        """Create & set window variables."""
        
        tk.Tk.__init__(self, *args, **kwargs)

        self.chatbot = ChatBot(
            "GUI Bot", system_performance_warning=True,         
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            logic_adapters=[
                "chatterbot.logic.BestMatch","chatterbot.logic.TimeLogicAdapter","chatterbot.logic.MathematicalEvaluation"
            ],
            input_adapter="chatterbot.input.VariableInputTypeAdapter",
            output_adapter="chatterbot.output.OutputAdapter",
            database="./database.db"
        )
        
        self.title("ChatBot")           #Name of the bot on the window

        self.initialize()
        
        style = ttk.Style()             #For styling the window
        style.theme_use('winnative')    #winnative is a style
        
        self.chatbot.set_trainer(ListTrainer)   
        
        for files in os.listdir('C:/Users\Desktop\Product\Completed\chatterbot-corpus-master\chatterbot_corpus\data\english/'):
            data = open( 'C:/Users\Desktop\Product\Completed\chatterbot-corpus-master\chatterbot_corpus\data\english/'+ files , 'r').readlines()
            self.chatbot.train(data)

    def initialize(self):
        
        """ Setting the window layout."""
        
        self.grid()
        
        self.respond = ttk.Button(self, text='Get Response', command=self.get_response)
        self.respond.grid(column=1, row=0, sticky='nesw', padx=3, pady=3)
        
        self.usr_input = ttk.Entry(self, state='normal')
        self.usr_input.grid(column=0, row=0, sticky='nesw', padx=3, pady=3)

        self.conversation_lbl = ttk.Label(self, anchor=tk.E, text='Conversation:')
        self.conversation_lbl.grid(column=0, row=1, sticky='nesw', padx=3, pady=3)

        self.conversation = ScrolledText.ScrolledText(self, state='disabled')
        self.conversation.grid(column=0, row=2, columnspan=3, sticky='nesw', padx=3, pady=3)

        self.respond = ttk.Button(self, text='More>>>', command=self.get_response)
        self.respond.grid(column=1, row=3, sticky='nesw', padx=3, pady=3)
        
        self.respond = ttk.Button(self, text = 'Voice', compound=LEFT,command=self.get_response)
        self.respond.grid(row=0, column=2 , sticky='nesw', padx=1, pady=1)

    def get_response(self):
        
        """Getting response from the chatbot and displaying it."""
        
        message = self.usr_input.get()
        self.usr_input.delete(0, tk.END)

        response = self.chatbot.get_response(message)

        self.conversation['state'] = 'normal'
        self.conversation.insert(
        tk.END, "Human: " + message + "\n" + "Bot: " + str(response.text) + "\n")
        self.conversation['state'] = 'disabled'

        time.sleep(0.1) 


TkinterGUIExample().mainloop()  #Runs the main class 
