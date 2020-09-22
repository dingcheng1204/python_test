a = 7
b = a
b = 8+9

print(a)
print(type(a))
print(9/5)
print(9//5)
print(0x25)
print(int(True))
print(int(98.3))
print(int('99'))
print(True + 5)
print(True + 6.6)

# print(int('99.3')) #error
print(float('99.3'))

print("this is first day" ",nice to meet u")
print("ha"*4 + " oh")
print(str(99))
print(str(True))

name = "Hejji"
# name[2] = "d" #'str' object does not support item assignment
name.replace('j', 'd')
print(name)

name = name.replace('j', 'd')
print(name)
print(name[:])
print(name[2:])
print(name[-3:])
print(name[1:-2])
print(name[-3:-1])
print(name[::-1])

print(name[-50:])
print(name[:70])
print(name[-51:-50]+" test")

print(len(name[-51:-50]+" test"))

sentence = " this is first day to this place" ",nice to meet u   ..."
print(sentence.split(','))
print(sentence.split())
words = ['this', 'is', 'first', 'day,Nice', 'to', 'meet', 'u']
print(' '.join(words))

print(sentence.startswith("thi"))
print(sentence.endswith(" u"))
print(sentence.find("to"))
print(sentence.rfind("to"))
print(sentence.count("to"))
print(sentence.isalnum())

print(sentence.strip('.'))
print(sentence.capitalize())
print(sentence.title())
print(sentence.upper())
print(sentence.lower())
print(sentence.ljust(20))
print(sentence.rjust(20))







