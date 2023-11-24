#!/usr/bin/env python3

def return_evens(num_list):
    new_list = [num for num in num_list if num % 2 == 0]
    return new_list


result = return_evens([1,2,3,4,5,6,7,8,9])
print(result)    

def make_exclamation(sentence_list):
    exclamation = [word + '!' for word in sentence_list]
    return exclamation

result = make_exclamation(['Hello', "I'm doing great", 'python is fun'])
print(result)

