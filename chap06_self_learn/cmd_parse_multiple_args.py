import cmd
import shlex

class MyShell(cmd.Cmd):
    intro = "Welcome to MyShell! Type help or ? to list commands.\n"
    prompt = "(myshell) "

    def do_add(self, arg):
        """Add numbers: add 1 2 3"""
        try:
            parts = shlex.split(arg)
            nums = [float(p) for p in parts]
        except ValueError:
            print("Error: all arguments must be numbers.")
            return
        except Exception as e:
            print(f"Parse error: {e}")
            return

        total = sum(nums)
        print(f"Sum = {total}")

    def do_exit(self, arg):
        """Exit the shell."""
        print("Goodbye!")
        return True

if __name__ == "__main__":
    MyShell().cmdloop()
