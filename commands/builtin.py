import os
import sys

def cmd_help(args):
    print("""PyOS - Available commands:
  help              - Show this message
  ls [dir]          - List directory contents
  cd <dir>          - Change directory
  pwd               - Print working directory
  exit, quit        - Exit the terminal
  openport <port>   - Open a TCP echo server
  run <cmd> [...]   - Run external system command
""")

def cmd_ls(args):
    path = args[0] if args else '.'
    try:
        print('\n'.join(os.listdir(path)))
    except Exception as e:
        print(f"ls error: {e}")

def cmd_cd(args):
    if not args:
        print("cd: missing operand")
        return
    try:
        os.chdir(args[0])
    except Exception as e:
        print(f"cd error: {e}")

def cmd_pwd(args):
    print(os.getcwd())

def cmd_exit(args):
    print("Goodbye.")
    sys.exit(0)

COMMANDS = {
    "help": cmd_help,
    "ls": cmd_ls,
    "cd": cmd_cd,
    "pwd": cmd_pwd,
    "exit": cmd_exit,
    "quit": cmd_exit,
}
