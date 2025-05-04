from stats import *


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return(file_contents)

        
def main(input_file):
    file_contents = get_book_text(input_file) # Call function to get contents of file
    num_words = word_counter(file_contents) # Call function in stats to get word count
    num_characters = character_counter(file_contents) # Call function in stats to get character count
    sorted_list = dictionary_sorter(num_characters) # Call function in stats to get a sorted list 

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {input_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for entry in sorted_list:        
        if entry["char"].isalpha():  # Check if the value of 'char' is alphabetic
            print(f"{entry['char']}: {entry['num']}") 

    print("============= END ===============")


if __name__ == "__main__":
    input_file = "books/frankenstein.txt"
    main(input_file)

           