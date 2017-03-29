#!/usr/bin/python

class Menu:
    def __init__(self, prompt='', openingMessage=None, closingMessage=None):
        self.menuCommands = {'help':
                             [self.PrintHelpMessage, 'Display Help Message']}
        self.prompt = prompt
        self.openingMessage = openingMessage
        self.closingMessage = closingMessage
        self.currentCommand = ''
        self.currentCommandArguments = []

    def SetPrompt(self, prompt):
        self.prompt = prompt
    def SetOpeningMessage(self, message):
        self.openingMessage = openingMessage
    def SetClosingMessage(self, message):
        self.closingMessage = closingMessage

    def RunMenu(self, script=None):
        if self.openingMessage is not None:
            self.PrintHeaderOne(self.openingMessage)

        if script is None:
            while(self.currentCommand.lower() != 'exit'):
                self.PromptUserForCommand()
                self.ParseUserCommandArguments()
                self.InvokeUserCommand()

    def PromptUserForCommand(self):
        self.currentCommand = raw_input(self.prompt + '> ')

    def ParseUserCommandArguments(self):
        if self.currentCommand != '':
            self.currentCommandArgs = self.currentCommand.split()
            self.currentCommand = self.currentCommandArgs.pop(0)

    def InvokeUserCommand(self):
        command = self.currentCommand.lower()

        if command == '':
            raise Exception('No Command')
        else:
            try:
                self.menuCommands[command][0]()
            except Exception:
                print ('Invalid Selection in Menu')
                raise

    def RunScript(self, scriptFileName):
        pass

    def PrintHelpMessage(self, arguments=None):
        self.PrintHeaderOne('Menu Commands:')
        for command in self.menuCommands:
            if len(command) <= 7:
                print(command + '\t\t' + self.menuCommands[command.lower()][1])

    def PrintHeaderOne(self, message):
        print('==================================================================================')
        print(message)
        print('==================================================================================')

    def PrintHeaderTwo(self, message):
        print('----------------------------------------------------------------------------------')
        print(message)
        print('----------------------------------------------------------------------------------')

