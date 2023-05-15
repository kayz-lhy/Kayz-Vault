# generate a random string and count each character, output the result dict in order of its value
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits


def main():
    test_str = ''
    for i in range(500):
        test_str += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
    print(test_str)
    dic = {}
    for char in test_str:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1
    new_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    # dict.items() is a tuple object and x[1] is the value of each item
    print(dict(new_dic))


main()
