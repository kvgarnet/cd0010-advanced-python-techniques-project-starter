
import cmd

class MyShell(cmd.Cmd):
    intro = "Welcome to MyShell! Type help or ? to list commands.\n"
    prompt = "(myshell) "

    def do_greet(self, arg):
        """Greet the named person: greet <name>"""
        name = arg.strip() or "stranger"
        print(f"Hello, {name}!")

    def do_exit(self, arg):
        """Exit the shell."""
        print("Goodbye!")
        return True  # Returning True tells cmdloop() to exit

if __name__ == "__main__":
    MyShell().cmdloop()


'''
from cmd import Cmd

class MyPrompt(Cmd):

    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
        print(f"Hello,{name}") 

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit


if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')
'''
