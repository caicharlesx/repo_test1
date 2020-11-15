# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 11:51:23 2019

@author: Charles
"""

def count_words(filename):
    """count approximate words in a file"""

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:  
        #msg="Sorry, the file " + filename + " does not exist."
        #print(msg)
        pass
    else:
         # Count the approximate number of words in the file
         words = contents.split()
         num_words = len(words)
         print("The file " + filename + " has about " + str(num_words) + " words.")    

filenames=['alice.txt', 'sidr.txt', 'moby_dick.txt', 'little_woman.txt']
for filename in filenames:
    count_words(filename)