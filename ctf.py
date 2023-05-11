from string import ascii_lowercase

ltrs = {k: v for v, k in enumerate(list(ascii_lowercase), 1)}

print(ltrs)



result = 'vygh ba i ovqhtom himb TVKKVLI XOGRK'


result_num = [ltrs[i] for i in result]
while True:
    key = input("Enter key")
    for i, let in enumerate(key):
        pass