#!/usr/bin/python3
"""program containing the command interpreter's entry point"""


import cmd
from posixpath import split
import string
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = ["BaseModel",
           "User",
           "Place",
           "State",
           "City",
           "Amenity",
           "Review"]


class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter"""

    prompt = "(hbnb)"
    intro = "Welcome to the HBNB Command Interpreter"

    def do_quit(self, arg):
        """To exit the program, use the Quit command."""
        print("quitting")
        raise SystemExit

    def do_EOF(self, arg):
        """The program terminates with EOF."""
        return True

    def emptyline(self):
        """Does nothing"""
        pass

    def do_create(self, arg):
        """Creates new instance of BaseModel,
        saves it to json and prints Id"""

        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = (eval(arg)())
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints string representation of an
        instance based on class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            argv = arg.split(' ')

            if argv[0] not in classes:
                print("** class doesn't exist **")
            elif len(argv) < 2:
                print("** instance id missing **")
            else:
                key = argv[0] + "." + argv[1]
                if key in storage.all():
                    new = storage.all()[key]
                    print(new)
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on classname and id"""
        if not arg:
            print("** class name missing **")
        else:
            argv = arg.split(' ')

            if argv[0] not in classes:
                print("** class doesn't exist **")
            elif len(argv) < 2:
                print("** instance id missing **")
            else:
                key = argv[0] + '.' + argv[1]
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """prints all string representation of all instances
        based or not on the class name"""
        argv = arg.split(' ')
        if not arg:
            print([str(obj) for obj in storage.all().values()])
        else:
            if argv[0] not in classes:
                print("** class doesn't exist **")
            else:
                new = ([str(obj) for obj in storage.all().values()
                        if argv[0] in str(obj)])
                print(new)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        and save the change into the JSON file"""
        if not arg:
            print("** class name missing **")
        else:
            argv = arg.split(' ')
            if argv[0] not in classes:
                print("** class doesn't exist **")
            else:
                if len(argv) < 2:
                    print("** instance id missing **")
                else:
                    key = argv[0] + '.' + argv[1]
                    if key not in storage.all():
                        print("** no instance found **")
                    else:
                        if len(argv) < 3:
                            print("** attribute name missing **")
                        else:
                            if len(argv) < 4:
                                print("** value missing **")
                            else:
                                setattr(storage.all()[key], argv[2], argv[3])
                                storage.all()[key].save()
    def do_count(self, arg):
        """Retrieve number of instances of a class"""
        argv = arg.split(' ')
        count = 0
        for obj in models.storage.all().values():
            if argv[0] == type(obj).__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
