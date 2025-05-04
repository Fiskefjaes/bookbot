from stats import *


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return(file_contents)

        
def main(input_file):
    file_contents = get_book_text(input_file)
    num_words = word_counter(file_contents)
    num_characters = character_counter(file_contents)
    sorted_list = dictionary_sorter(num_characters)

    print(f"{num_words} words found in the document")
    print(sorted_list)




if __name__ == "__main__":
    input_file = "books/frankenstein.txt"
    main(input_file)

           