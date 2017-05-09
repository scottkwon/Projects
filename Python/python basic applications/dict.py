def packer(**kwargs):
    print(kwargs)

packer(name="Scott", num=31, korean=True)

def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi no name!")

unpacker(**{"last_name": "Kwon", "first_name": "Scott"})
