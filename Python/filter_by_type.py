#Write a program that tests for the type of input given, and make it respond differently to varying lengths.
def filter():
    raw_input = input("""
    Enter your integer, string, or list below!
    >
    """)
    if isinstance(raw_input, int):
        print "This item is an integer"
        if raw_input >= 100:
            print "That's a big number!"
        else:
            print "That's a small number"
    if isinstance(raw_input, str):
        print "This item is a string"
        if len(raw_input) >= 50:
            print "Long sentence."
        else:
            print "Short sentence."
    if isinstance(raw_input, list):
        print "This item is a list"
        if len(raw_input) >= 10:
            print "Big list!"
        else:
            print "Short list"

filter()
