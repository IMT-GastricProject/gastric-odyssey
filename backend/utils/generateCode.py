from random import randint
def generateCode():
    CODE_LENGTH = 5
    code = ''
    for i in range(CODE_LENGTH):
        code += str(randint(0,9))
    return int(code)