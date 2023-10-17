#!/usr/bin/python3
"""
console.py : The main program entry point.
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    class_dict = {"BaseModel": BaseModel}

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)."""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def validate_class_id(self, args):
        """Validate the class name and instance ID."""
        if not args:
            print("** class name missing **")
            return None, None
        class_name, instance_id = args.split()[:2]
        if class_name not in self.class_dict:
            print("** class doesn't exist **")
            return None, None
        if not instance_id:
            print("** instance id missing **")
            return None, None
        return class_name, instance_id

    def do_create(self, arg):
        """Create a new instance of a class and save it to the JSON file."""
        class_name = arg.split()[0] if arg else None
        if not class_name:
            print("** class name missing **")
        elif class_name not in self.class_dict:
            print("** class doesn't exist **")
        else:
            new_instance = self.class_dict[class_name]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance
        based on the class name and id."""
        class_name, instance_id = self.validate_class_id(arg)
        if class_name and instance_id:
            key = f"{class_name}.{instance_id}"
            instance = storage.all().get(key)
            if instance:
                print(instance)
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        class_name, instance_id = self.validate_class_id(arg)
        if class_name and instance_id:
            key = f"{class_name}.{instance_id}"
            instances = storage.all()
            if key in instances:
                del instances[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print the string representation of
        all instances based on the class name (optional).
        """
        objects = storage.all()
        if arg and arg not in self.class_dict:
            print("** class doesn't exist **")
        else:
            filtered_objects = [
                str(obj)
                for obj in objects.values()
                if not arg or type(obj).__name__ == arg
            ]
            print(filtered_objects)

    def do_update(self, arg):
        """Update an instance based on the class name,
        id, attribute name, and value.
        """
        class_name, instance_id = self.validate_class_id(arg)
        if class_name and instance_id:
            args = arg.split()[2:]
            if len(args) == 0:
                print("** attribute name missing **")
            elif len(args) == 1:
                print("** value missing **")
            else:
                key = f"{class_name}.{instance_id}"
                instance = storage.all().get(key)
                if not instance:
                    print("** no instance found **")
                    return
                attribute_name, attribute_value = args[0], args[1].strip('"')
                if hasattr(instance, attribute_name):
                    setattr(
                        instance,
                        attribute_name,
                        type(getattr(instance, attribute_name))(attribute_value),
                    )
                    instance.save()
                else:
                    print("** attribute doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
