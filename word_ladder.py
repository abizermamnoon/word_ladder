#!/bin/python3

from collections import deque
import copy

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    lc = []
    if len(word1) != len(word2):
        return False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            lc += [i]
    if len(lc) != 1:
        return False
    else:
        return True


def get_text(filename): #used to get access to dictionary of 5 letter words
    f = open(filename, encoding = 'latin1')
    text = f.read()
    f.close()
    return text

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    dictionary_file = get_text("words5.dict")
    dictionary = dictionary_file.split("\n")
    stack = []
    stack.append(start_word)
    dictionary.remove(start_word)
    ys = deque([])
    ys.append(stack)
    if start_word == end_word:
        return ys
    if len(end_word) > len(start_word):
        return None
    while len(ys) != 0: 
        ref = ys.popleft()
        lci = copy.copy(dictionary)
        for word in lci:
            if _adjacent(word, ref[-1]):
                if word == end_word:
                    ref.append(word)
                    return ref
                lc = copy.copy(ref)
                lc.append(word)
                ys.append(lc)
                dictionary.remove(word)
    return None
print("word_ladder('stone','money')=", word_ladder('stone','money'))


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if len(ladder) == 0:
        return False
    for i in range(len(ladder)):
        if i == len(ladder) - 1:
            return True
        elif _adjacent(ladder[i], ladder[i + 1]) == False:
            return False
