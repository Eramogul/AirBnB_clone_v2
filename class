#!/usr/bin/python3
"""
Module for the HBNBCommand class
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command processor for the AirBnB console.
    """

    prompt = '(hbnb) '  # This is the prompt that will appear

    def do_quit(self, arg):
        """Exit the console"""
        return True

    def do_EOF(self, arg):
        """Exit the console on EOF"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class"""
        if not arg:
            print("** class name missing **")
            return
        # Add functionality to create an instance of the given class

    def do_show(self, arg):
        """Show an instance based on class name and id"""
        if not arg:
            print("** class name missing **")
            return
        # Add functionality to show the instance

    def do_destroy(self, arg):
        """Destroy an instance based on class name and id"""
        if not arg:
            print("** class name missing **")
            return
        # Add functionality to destroy the instance

    def do_all(self, arg):
        """Show all instances of all classes"""
        # Add functionality to display all instances

    def do_update(self, arg):
        """Update an instance based on class name and id"""
        if not arg:
            print("** class name missing **")
            return
        # Add functionality to update an instance

if __name__ == '__main__':
    HBNBCommand().cmdloop()

