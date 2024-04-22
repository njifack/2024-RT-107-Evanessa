""" create a word play game using python strings"""

word = input("hey there what's your fav word today : ") # ask the user to enter a word.
print(f"the lenght of your word is: {len(word)} ") # print the length of the word.

word_upper = word.upper() # convert the word in lowercase
word_lower = word.lower() # convert the word in uppercase
print(f"this is your fav word in upper case: {word_upper}") 
print(f"this is your fav word in lower case: {word_lower}") 

letter = input("Enter a letter :") # ask the user for a letter
letter_count = word.count(letter) # count how many times that letter appears in word
print(f"'{letter}'appears {letter_count} time(s) in '{word}'")


substring = (input("Enter a substring : ")) # ask user to enter a substring
substring_count = word.count(substring) # count how many time the substring appears in word
print(f"'{substring}' appears {substring_count} time(s) in '{word}'")


word_reverse = word[::-1] # reverse the word and print the result
print(f"Reverse word : {word_reverse}")


start_index = int(input("Enter a starting index: ")) # ask the user to enter a starting index
end_index = int(input("Enter an ending index: "))  # ask the user to enter an ending index
slice_word = word[start_index:end_index] # slicing
print(f"Sliced word : {slice_word}")

    
character = input("Enter a character : ") # ask the user to enter a character 
replace_char = word.replace(word[0] , character ,1) # replace the first occurrence of that character with another character.
print(f"New word: {replace_char}")


word_second = input("Enter a second word: ") # ask the user to enter a 2nd word
concat_words =  word +  word_second #  concatenate the original word with a second word
print(f"Concatenated words: {concat_words}")

is_palindrome = word == word[::-1] # check if the original word is a palindrome
print(f"Is palindrome ? {is_palindrome} ")

word_identifier = word.isidentifier() # check if the original word is a valid Python identifier
print(f"Is a valid Python identifier?{word_identifier} ")
