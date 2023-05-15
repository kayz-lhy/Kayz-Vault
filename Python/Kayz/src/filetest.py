import os
import time
import random
import string


def main():
    os.chdir(r'E:\Project\Python\Kayz\src\txt')
    mode = input('mode:')
    if mode == 'del':
        for file in os.listdir(r'E:\Project\Python\Kayz\src\txt'):
            os.remove(file)
    for i in range(0):
        with open(str(str(random.choice(range(5000, 10000))) + '.txt'), mode='w') as fp:
            x = ''
            for j in range(10):
                x += random.choice(string.ascii_lowercase)
            fp.write(x)
    os.chdir(r'D:\Software\fastgit')
    os.startfile('FastGithub.UI.exe')


main()
