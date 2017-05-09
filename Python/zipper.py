name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


def zipped(list1,list2):
    new_list = dict(zip(list1,list2))
    print new_list

zipped(name,favorite_animal)
