#!/usr/bin/python3
"""the HBnB"""        
import cmd            
import re
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State



def my_parse_argument(arg):                    
    cur_brace = re.search(r"\{(.*?)\}", arg)     
    square_bracket = re.search(r"\[(.*?)\]", arg)
    if cur_brace is None:
        if square_bracket is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lex = split(arg[:square_bracket.span()[0]])
            result_list = [i.strip(",") for i in lex]
            result_list.append(square_bracket.group())
            return result_list
    else:
        lex = split(arg[:cur_brace.span()[0]])
        result_list = [i.strip(",") for i in lex]
        result_list.append(cur_brace.group())
        return result_list


class HBNBCommand(cmd.Cmd):
    """Defines the HBnb cmd interpreter.         
    Attributes:
        prompt (str): cmd prompt
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """An empty line to be recieved."""               
        pass

    def default(self, arg):
        """Handle invalid input for commands."""       
        arg_dict = {                      
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        exact = re.search(r"\.", arg)  
        if exact is not None:
            arg_list = [arg[:exact.span()[0]], arg[exact.span()[1]:]]
            exact = re.search(r"\((.*?)\)", arg_list[1])
            if exact is not None:
                command = [arg_list[1][:exact.span()[0]], exact.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    calling = "{} {}".format(arg_list[0], command[1])
                    return arg_dict[command[0]](calling)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Use: create <class>
        Instantiate a fresh object from a class and output its id.    
        """
        arg_list = my_parse_argument(arg)              
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_list[0])().id)
            storage.save()

    def do_show(self, arg):
        """Use: show <class> <id> or <class>.show(<id>)
        Displays the representation of a class instance along with its id. 
        """
        arg_list = my_parse_argument(arg)                      
        objectD = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in objectD:
            print("** no instance found **")
        else:
            print(objectD["{}.{}".format(arg_list[0], arg_list[1])])

    def do_destroy(self, arg):
        """Use: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance in Python using its id with the del statement.                    
        """
        arg_list = my_parse_argument(arg)                 
        objectD = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in objectD.keys():
            print("** no instance found **")
        else:
            del objectD["{}.{}".format(arg_list[0], arg_list[1])]
            storage.save()

    def do_all(self, arg):
        """Use: all <class> or all <class> or <class>.all()
        Displays the representation of a class instance identified by its id        
        Or all classes if no class is given"""
        arg_list = my_parse_argument(arg)                            
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objectL = []
            for o in storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == o.__class__.__name__:
                    objectL.append(o.__str__())
                elif len(arg_list) == 0:
                    objectL.append(o.__str__())
            print(objectL)

    def do_count(self, arg):
        """Use: count <class> or <class>.count()
        Pritns the instances number of the given class.              
        """
        arg_list = my_parse_argument(arg)             
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            c = 0
            for o in storage.all().values():
                if arg_list[0] == o.__class__.__name__:
                    c += 1
            print(c)

    def do_update(self, arg):
        """Use: update <class> <id> <attribute_name> <attribute_value>
        or <class>.update(<id>, <attribute_name>, <attribute_value>)
        or <class>.update(<id>, <dictionary>)
        Updates class instance of a given id.                
        """
        arg_list = my_parse_argument(arg)                  
        objectD = storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in objectD.keys():
            print("** no instance found **")
            return False
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            try:
                type(eval(arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg_list) == 4:
            o = objectD["{}.{}".format(arg_list[0], arg_list[1])]
            if arg_list[2] in o.__class__.__dict__.keys():
                valueT = type(o.__class__.__dict__[arg_list[2]])
                o.__dict__[arg_list[2]] = valueT(arg_list[3])
            else:
                o.__dict__[arg_list[2]] = arg_list[3]
        elif type(eval(arg_list[2])) == dict:
            o = objectD["{}.{}".format(arg_list[0], arg_list[1])]
            for k, v in eval(arg_list[2]).items():
                if (k in o.__class__.__dict__.keys() and
                        type(o.__class__.__dict__[k]) in {str, int, float}):
                    valueT = type(o.__class__.__dict__[k])
                    o.__dict__[k] = valueT(v)
                else:
                    o.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

