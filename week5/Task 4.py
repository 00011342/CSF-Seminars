def Compare(x,y):
    if x>y:
        return 1
    elif x==y:
        return 0
    else:
        return -1
print(Compare(10,5))

#python string
fruit='banana'
i=2
a=fruit[i+2]
print(a)
#python len in string number of charcters
fruit='banana'
a=len(fruit)
print(a)

b='Hello World'
a=len(b)
print(a)

#To get the last letter of astring:

length=len(fruit)
last=fruit[length-2]
print(last)

#Traversal
index=1
while index<len(fruit):
    letter=fruit[index]
    print (letter)
    index=index+1
print(letter)

'''str='computer'
for i in range(8):
    print(str[i]) '''
'''str1=input("Say something:")
len1=len(str1)
for i in range(len1):
    print(str1[i])'''

#Travels with while loop
'''str2=input("Say Something:")
i=0
len2=len(str2)
while i<len2:
    print(str2[i])
    i+=1'''
'''str=input("Drop any word please:")
i=0
len=len(str)
while i<len:
    print(str[i])
    i+=1'''

    #string concatenation
'''pref='JKLMNOPQ'
suffix ='act'
for letter in pref:
    print(letter +suffix)'''

index=0
fruit='banana'
for letter in fruit:
    print(letter)
    index=index+1

greeting='Hello wORLD'
new_greeting='j'+greeting[1:]
print(new_greeting)

name='Anvar'
new_name='Y'+name[1:]
print(new_name)

#searching
'''def find(word, letter):
    index=0
    while index<len(word):
        if word[index]==letter:
            return index
        index=index+1
        return -1
print(find('computer','r'))'''

def find(word,letter,index):
    while index<len(word):
        if word[index]==letter:
            return index
        index+=index
        return -1
print(find('westminster','i',0))




