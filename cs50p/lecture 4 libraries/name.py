import sys
if len(sys.argv) > 2:
    sys.exit("Too many argumments")
elif len(sys.argv) < 2:
    sys.exit("Too few argumentes")

print("Hello, My name is",sys.argv[1])