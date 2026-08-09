text= input("Enter your text: ")
def total_characters(text):
    return len(text)
def total_words(text):
    return len(text.split())
def convert_upper(text):
    return text.upper()
def convert_lower(text):
    return text.lower()
def replace_word(text,old_word,new_word):
        return text.replace(old_word,new_word)
def search_word(word,text):
    return text.find(word)
while True:
    print("-------------MENU-------------")
    print("1. Enter 1 to Count characters")
    print("2. Enter 2 to Count words")
    print("3. Enter 3 to Convert to uppercase")
    print("4. Enter 4 to Convert to lowecase")
    print("5. Enter 5 to Replace a word")
    print("6. Enter 6 to Search a word")
    print("7. Enter 7 to Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
       characters = total_characters(text)
       print("Total characters:", characters)
    elif choice == "2":
        words = total_words(text)
        print("Total words:", words)
    elif choice == "3":
        upper_text= convert_upper(text)
        print("Total in uppercase: ", upper_text)
    elif choice == "4":
        lower_text= convert_lower(text)
        print("Total in lowercase: ", lower_text)
    elif choice == "5":
        old_word= input("Enter word to replace: ")
        new_word=input(f"Enter the new word to replace '{old_word}': ")
        text = replace_word(text,old_word,new_word)
        print(text)
    elif choice == "6":
        word_to_search = input("Enter a word to search: ")
        word_found = search_word(word_to_search, text)
        if(word_found!=-1):
            print("Word found at starting index: ",word_found)
        else:
            print("word not found")
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
   