def read_dict():
    about_me = {
        "name": "Scott Kwon",
        "age": 25,
        "country of birth": "USA",
        "favorite language": "Python"
    }
    for item in about_me:
        print "My {} is {}".format(item, about_me[item])

read_dict()
