from stats import num_words, count_characters, sorted_dictionaries
import sys





def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    number = num_words(book_text)
    #print(f'{number} words found in the document')
    num_characters = count_characters(book_text)
    #print(num_characters)
    sorted_list = sorted_dictionaries(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["character"].isalpha():
            continue
        print(f"{item["character"]}: {item["count"]}")
    print("============= END ===============")

        
        
    
    

main()
