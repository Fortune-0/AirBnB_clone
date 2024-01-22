#!/usr/bin/python3
"""
    class for command interpter
"""
import cmd
# import shlex
# from base_model import BaseModel
# from models import storage


class HBNBCommand(cmd.Cmd):
<<<<<<< HEAD
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
=======
    """
    class for command interpter
    """
    prompt = "(hbnb)"

    valid_class = ["BaseModel", "User"]

    def emptyline(self):
>>>>>>> f503673cd94fe387867fb2698b9aa6c17e3a35e1

        """
            Do nothing when an empty line is entered.
        """
        pass

    def do_EOF(self, line):

        """
        Handles End Of File (ctrl+D) to exit the program.
        """
        # print()
        return True

    def do_quit(self, arg):

        """
        Quit command to exit the program
        """
        return True

    def do_create(self, arg):
        """
        create a new instance of the base Model and save it to the json file.
        usage: create <class_name>
        """
        pass

    def do_show(self, arg):
        """
        Show all instances of a class in JSON format.
        """
        pass

    def do_destory(self, arg):
        """
        Delete an instance based on the class name and id.
        usage: destory <class_name> <id>
        """
        pass

    def do_all(self, arg):
        """
        print the string representation of all the instance or a specific type
        usage: all [class_name]
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
