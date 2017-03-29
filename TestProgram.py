#!/usr/bin/python
import GenericMenu
from GenericMenu import Menu
import os, sys
from os import system
import argparse

def main():
    mainMenu = Menu(prompt='TestMenu', openingMessage='Welcome. This is a test.', closingMessage='Good bye.')

    mainMenu.RunMenu()

if __name__ == '__main__':
    main()
