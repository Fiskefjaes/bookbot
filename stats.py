def word_counter(file_contents):    
    return len(file_contents.split()) 


def character_counter(file_contents):
    text = file_contents.lower()
    count = {}
    for letter in text:
        if letter not in count:
            count[letter] = 0            
        count[letter] += 1 # The "else" is implicit.
    return count
		

def dictionary_sorter(count):