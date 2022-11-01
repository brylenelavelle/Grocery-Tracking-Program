import re
import string


def printsomething():
    print("Hello from python!")

def PrintMe(v):
    print("You sent me: " + v)
    return 100;

def SquareValue(v):
    return v * v

def get_freq(file_name):
    with open(file_name, 'r') as fp: # Opens the file
        lines = fp.read().split()  # Returns a list of items as a string
        set_words = set(lines) # Turns the list into a set 
        str_ret = ''
        for word in set_words:
            str_ret += f'{word} {lines.count(word)}' # Returns the item's name with it's corresponding frequency
            str_ret += chr(0xA) # Creates new line after each item
        print(str_ret)
    return str_ret

# Counts the frequency of each item on the list 
def get_freq_dict(file_name):
    with open(file_name, 'r') as fp: # Opens the file
        lines = fp.read().split()  # Returns a list of items as a string
        set_words = set(lines) # Turns the list into a set 
        dict_freq = {} # Creates an empty dictionary list
        for word in set_words:
            dict_freq[word] = lines.count(word) # Checks how many times an item is repeated in the list
    return dict_freq

# Looks up a specific item and count its the frequency from the list
def get_itemFreq(word):
    file_name = 'Project Three Input File.txt'
    with open(file_name, 'r') as fp:
        lines = fp.read()
    return lines.count(word)

# Calls the previous function to perform the calculation and returns the item's name with it's corresponding frequency
# The return statement is then modified to where the number printed is converted into a specific number of asterisks
def display_histogram(file_name):
    dict_freq = get_freq_dict(file_name) 
    word_sorted_count = sorted(dict_freq.items()) 
    HIST_CHAR = '*'
    for word, count in word_sorted_count:
        print(word,'  ', HIST_CHAR * count)



    
