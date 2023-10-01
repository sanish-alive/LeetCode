def revString():
    string = "sanish shrestha"
    b = len(string)-1
    rev=""
    for i in range(b, -1, -1):
        rev += string[i]
        print(rev)
    print(rev);
    print("one lline: "+string[::-1])

def palindrome(userInput):
    userInput = ''.join(letter for letter in userInput if letter.isalnum())
    a = 0
    b = len(userInput)-1


    for i in range(b):
        if a<=b:
            if userInput[a] != userInput[b]:
                return "not palindrome"
        b -= 1
        a+=1
    return "palindrome"


def stringNumAdd(userInput):
    sum = 0
    for i in userInput:
        if i.isdigit():
            sum += int(i)
    return sum

def countOccurrence(userInput):
    hash_map = dict()

    for word in userInput:
        if word in hash_map.keys():
            hash_map[word] += 1
        else:
            hash_map[word] = 1
    return hash_map

def anagram(wordOne, wordTwo):
    if len(wordOne) != len(wordTwo):
        return "not anagram"
    wordOne = sorted(wordOne.lower().replace(' ', ''))
    wordTwo = sorted(wordTwo.lower().replace(' ', ''))
    print(wordTwo)
    print(wordOne)
    if wordOne == wordTwo:
        return "anagram"
    else:
        return "not angram"

def isVowel(userInput):
    c, v = 0, 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    for word in userInput.lower():
        if word in vowel:
            v+=1
        else:
            c+=1
    return "vowel: ",v," consonent: ",c

def reverseArray(userArray):
    a=0
    b=len(userArray)-1
    for i in range(b):
        if a<=b:
            temp = userArray[a]
            userArray[a] = userArray[b]
            userArray[b] = temp
            a+=1
            b-=1
    return userArray

def maxNum(userArray):
    max_num = userArray[0]
    for i in userArray:
        if max_num < i:
            max_num = i
    return max_num

def sortArray(userArray):
    temp = None
    for i in range(len(userArray)):
        for j in range(len(userArray)):
            if userArray[i] < userArray[j]:
                temp = userArray[i]
                userArray[i] = userArray[j]
                userArray[j] = temp
    return userArray

def averageNumber(userArray):
    sum=0
    for num in userArray:
        sum+=num
        if num%2==0:
            print(num, " :even")
        else:
            print(num, " :odd")
        
    return sum/len(userArray)


def fibonacci(n, a=0, b=1):
    if n <= 0:
        return []
    else:
        return [a]+ fibonacci(n-1, b, a+b)
    

def quickSort(array):
    if len(array)<=1:
        return array
    left, right = [], []
    pivot = array.pop()
    
    for i in array:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    return quickSort(left)+[pivot]+quickSort(right)

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    print(quickSort([1,3,7,4,9,0,3,5,7,1,3]))
    print(fib(11))