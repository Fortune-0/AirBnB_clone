#!/usr/bin/python3
#command interpreter in python

from ast import parse
import cmd
# print(dir(cmd.Cmd))

'''class for command interpter '''

class HBNBCommand(cmd.Cmd):
 import cmd
from datetime import datetime
from model.base_model import BaseModel
from model import classes, storage
import re
from model.user import User
from model.state import State
from model.city import City
from model.amenity import Amenity
from model.place import Place
from model.review import Review
import model

class HBNBCommand(cmd.Cmd):
    # intro = 'Welcome to the command prompt! Please enter help for a list of commands.'
    prompt = '(hbnb) '
    valid_classes = ["BaseModel", "User"]
    
    def do_EOF(self, line):
        """Handles End Of File character.
        """
        print()
        return True
    
    def do_quit(self, line):
        ''' Quit command to exit the program '''
        return True
    pass

def do_create(self, arg):
        '''Creates new instance'''
        args = parse(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            obj = classes[args[0]]()
            obj.save()
            print(obj.id)    

def do_show(self, arg):
        'Shows attributes of <class> <id>'
        args = parse(arg)
        if not args or len(args) == 0 or args[0] == "":
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2 or args[1] == "":
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

def do_destroy(self, arg):
        'Deletes instance of <class> <id>'
        args = parse(arg)
        if not args or len(args) == 0 or args[0] == "":
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2 or args[1] == "":
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

def do_all(self, arg):
        'Prints all <class> instances or all instances'
        args = parse(arg)
        objects = storage.all()
        if not args:
            v_list = []
            for k, v in objects.items():
                v_list.append(str(objects[k]))
            if v_list:
                print(v_list)
        else:
            v_list = []
            for k, v in objects.items():
                if v.__class__.__name__ == args[0]:
                    v_list.append(str(objects[k]))
            if v_list:
                print(v_list)
            else:
                print("** class doesn't exist **")