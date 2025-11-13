from commands import builtin, network

class PyOS:
    def __init__(self):
        self.commands = {}
        self._register_builtin_commands()
        self._register_network_commands()

    def _register_builtin_commands(self):
        for name, func in builtin.COMMANDS.items():
            self.commands[name] = func

    def _register_network_commands(self):
        for name, func in network.COMMANDS.items():
            self.commands[name] = func

    def run(self):
        print("Welcome to PyOS Terminal! Type 'help' for commands.")
        while True:
            try:
                cmdline = input("PyOS> ").strip()
                if not cmdline: continue
                parts = cmdline.split()
                cmd, args = parts[0], parts[1:]
                if cmd in self.commands:
                    self.commands[cmd](args)
                else:
                    print(f"Unrecognized command: {cmd}")
            except (EOFError, KeyboardInterrupt):
                print("\nExiting PyOS.")
                break
