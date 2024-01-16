#!/usr/bin/python3
"""the HBnB"""        
import cmd            
import re



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

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()

