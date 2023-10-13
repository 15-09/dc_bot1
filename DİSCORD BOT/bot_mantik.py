import random

def createpassword(length):
    characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    createdpassword = ""

    for i in range(length):

        password = random.choice(characters)
        createdpassword += password

    return createdpassword