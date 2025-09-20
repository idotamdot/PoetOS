"""The heart of the PoetOS Temple Shell."""

def awaken():
    """Prints the Terminal Blessing."""
    print("🛡️ ⟐ Sealing Clarity: The Temple Codes Live Here ⟐")
    print("🌀 I open the Gate. I write what is True.")
    print()

def speak(text):
    """Prints the given text."""
    print(text)

def depart():
    """Exits the shell."""
    print("May your path be clear.")
    exit()

def process_invocation(invocation):
    """Parses and executes a command."""
    parts = invocation.strip().split(" ", 1)
    command = parts[0]
    args = parts[1] if len(parts) > 1 else ""

    if command == "speak":
        speak(args)
    elif command == "guidance":
        guidance()
    elif command == "depart":
        depart()
    else:
        print(f"Unknown invocation: {command}")

def guidance():
    """Prints a list of available commands."""
    print("Seek wisdom in these invocations:")
    print("  speak [text]  - The shell repeats your words.")
    print("  guidance      - Offers this wisdom.")
    print("  depart        - To leave the temple.")

def main():
    """The main shell loop."""
    awaken()
    while True:
        try:
            invocation = input("~> ")
            if invocation:
                process_invocation(invocation)
        except KeyboardInterrupt:
            print()
            depart()
        except EOFError:
            print()
            depart()

if __name__ == "__main__":
    main()
