#!/usr/bin/python3
"""
console module
"""

import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models import storage

class_registry = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'Review': Review,
    'Place': Place,
    'City': City,
    'Amenity': Amenity
}

class HBNBCommand(cmd.Cmd):
    """HBNB Class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Define quit"""
        return True
    
    def do_EOF(self, arg):
        """Define end of function"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Creates new instance of BaseModel and saves it to JSON file"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in class_registry:
            print("** class doesn't exist **")
            return

        # Create an instance of the class
        new_instance = class_registry[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance based on the class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

    def do_destroy(self, arg):
        """delete an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        
        class_name = args[0]
        instance_id = args[1]
        if class_name not in class_registry:
            print("** class doesn't exist **")
            return
        
        key = "{}.{}".format(class_name, instance_id) # Create the key for the instance
        if key not in storage.all():
            print("** no instance found **")
            return
        
        del storage.all()[key] # Delete instance from storage
        storage.save() # Save updated storage

    def do_all(self, arg):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        args = shlex.split(arg)
        if len(args) > 0:
            class_name = args[0]
            if class_name not in class_registry:
                print("** class doesn't exist **")
                return
            # Print all instances of specified class
            print([str(obj) for obj in storage.all().values()
                   if type(obj).__name__ == class_name])
        else:
            # print all instances regardless of class
            print([str(obj) for obj in storage.all().values()])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
