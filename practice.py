def aaa(min, max):
    number = range(min, max)
    odd = 0
    even = 0

    for x in number:

        if x % 2 == 1:
            print("odd")
            odd += 1

        elif x % 2 == 0:
            print("even")
            even += 1

        else:
            print("unknown error")


    return 0


print(aaa(1, 11))
print('a')

print('aaaaa')