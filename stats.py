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
		

def dictionary_sorter(num_characters):
    transformed_list = []
    for k, v in num_characters.items():
        transformed_list.append({"char": k, "num": v})

    return sorted(transformed_list, key=lambda x: x['num'], reverse=True) 
    # Lambda used so as to not having to create a proper function for getting the nums
    # "sorted" preferred over "sort" because it returns a new list rather that doing it "in-place and returning None"
    

'''
# This function is the "dictionary comprehension version" of the above function (sorting part not included).
def dictionary_sorter2(num_characters):
    transformed_list = [{"letter": k, "count": v} for k, v in num_characters.items()]

    return transformed_list

'''