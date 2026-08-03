# 1. Take input as string from user and find length of string without using len() function.
# user_input = input("Enter a string: ")
# count = 0
# for char in user_input:
#     count += 1
# print("Length of the string is:", count)

#2.Count the no. of vowels,consonants,digits ,spaces and special characters in a string.
# s=input("Enter a string: ")
# vowels=0
# consonants=0
# digits=0
# spaces=0
# special_characters=0
# def is_vowel(char):
#     return char.lower() in 'aeiou'

# for char in s:
#     if char.isalpha():
#         if is_vowel(char):
#             vowels += 1
#         else:
#             consonants += 1
#     elif char.isdigit():
#         digits += 1
#     elif char.isspace():
#         spaces += 1
#     else:
#         special_characters += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)
# print("Digits:", digits)
# print("Spaces:", spaces)
# print("Special Characters:", special_characters)

#3. To reverse a string without using inbuilt function.
# s = input("Enter a string: ")
# reversed_string = ""
# for char in s:
#     reversed_string = char + reversed_string
# print("Reversed string:", reversed_string)


#4. To check whether a string is palindrome or not.
# s = input("Enter a string: ")
# def is_palindrome(string):
#     reversed_string = ""
#     for char in string:
#         reversed_string = char + reversed_string
#     return string == reversed_string
# is_palindrome_result = is_palindrome(s)
# if is_palindrome_result:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

#5. To count the number of uppercase and lowercase letters in a string.
# s=input("Enter a string: ")
# def count_case(string):
#     uppercase_count = 0
#     lowercase_count = 0
#     for char in string:
#         if char.isupper():
#             uppercase_count += 1
#         elif char.islower():
#             lowercase_count += 1
#     return uppercase_count, lowercase_count
# count_uppercase, count_lowercase = count_case(s)
# print("Uppercase letters:", count_uppercase)
# print("Lowercase letters:", count_lowercase)

#6. To replace all occurrences of a given character with another character
# s=input("Enter a string: ")
# def replace_character(string, old_char, new_char):
#     replaced_string = ""
#     for char in string:
#         if char == old_char:
#             replaced_string += new_char
#         else:
#             replaced_string += char
#     return replaced_string
# replaced_string = replace_character(s, 'a', 'o') #replacing 'a' with 'o'
# print("String after replacement:", replaced_string)

#7.To remove all spaces from a input string.
# s=input("Enter a string: ")
# def remove_spaces(string):
#     no_space_string = ""
#     for char in string:
#         if not char.isspace():
#             no_space_string += char
#     return no_space_string
# removed_space_string = remove_spaces(s)
# print("String after removing spaces:", removed_space_string)

#8. To find no. of times a specified character appears in  string.
# s=input("Enter a string: ")
# def count_character(string, char_to_count):
#     count = 0
#     for char in string:
#         if char == char_to_count:
#             count += 1
#     return count
# count_characters = count_character(s, 'a') #counting occurrences of 'a'
# print("The character 'a' appears", count_characters, "times in the string.")

#9. To print the first and last character of a string.
# s=input("Enter a string: ")
# def first_last_character(string):
#     if len(string) == 0:
#         return None, None
#     first_char = string[0]
#     last_char = string[-1]
#     return first_char, last_char
# first_char, last_char = first_last_character(s)
# print("First character:", first_char)
# print("Last character:", last_char)

#10.To display each character of a string along with its ASCII value.
# s=input("Enter a string:")
# def display_ascii_values(string):
#     for char in string:
#         print(f"Character: {char}, ASCII Value: {ord(char)}")
# display_ascii_values(s)

#11. To count total no. of words in a sentence.
# v=input("Enter a sentence: ")
# def count_words(sentence):
#     word_count = 0
#     in_word = False
#     for char in sentence:
#         if char.isspace():
#             if in_word:
#                 word_count += 1
#                 in_word = False
#         else:
#             in_word = True
#     if in_word:
#         word_count += 1
#     return word_count
# word_count=count_words(v)
# print("Total number of words in the sentence:", word_count)

#12. To find longest word in a sentence.
# v= input("Enter a sentence: ")
# def find_longest_word(sentence):
#     words = sentence.split()
#     longest_word = ""
#     for word in words:
#         if len(word) > len(longest_word):
#             longest_word = word
#     return longest_word
# count_longest_word = find_longest_word(v)
# print("The longest word in the sentence is:", count_longest_word)

#13. To find shortest word in a sentence.
# v=input("Enter a sentence: ")
# def find_shortest_word(sentence):
#     words = sentence.split()
#     if not words:
#         return None
#     shortest_word = words[0]
#     for word in words:
#         if len(word) < len(shortest_word):
#             shortest_word = word
#     return shortest_word
# count_shortest_word = find_shortest_word(v)
# print("The shortest word in the sentence is:", count_shortest_word)

#14. To convert first letter of every word to uppercase
# v=input("Enter a sentence: ")
# def capitalize_first_letter(sentence):
#     words = sentence.split()
#     capitalized_words = []
#     for word in words:
#         if word:  # Check if the word is not empty
#             capitalized_word = word[0].upper() + word[1:]
#             capitalized_words.append(capitalized_word)
#         else:
#             capitalized_words.append(word)  # Preserve empty words (if any)
#     return ' '.join(capitalized_words)
# capitalized_sentence = capitalize_first_letter(v)
# print("Sentence after capitalizing first letter of every word:", capitalized_sentence)

#15. To print all duplicate characters in a string.
# s=input("Enter a string: ")
# def find_duplicate_characters(string):
#     duplicates = {}
#     for char in string:
#         if char in duplicates:
#             duplicates[char] += 1
#         else:
#             duplicates[char] = 1
#     duplicate_chars = {char: count for char, count in duplicates.items() if count > 1}
#     return duplicate_chars
# new_string = find_duplicate_characters(s)
# if new_string:
#     print("Duplicate characters and their counts:", new_string)

#16. To display the frequency of every character in a string.
# s= input("Enter any string: ")
# def display_character_frequency(string):
#     frequency = {}
#     for char in string:
#         if char in frequency:
#             frequency[char] += 1
#         else:
#             frequency[char] = 1
#     return frequency
# char_frequency = display_character_frequency(s)
# print("Frequency of every character in the string:", char_frequency)

#17. To check whether a string is anagram or not.
# s1 = input("Enter the first string: ")
# s2 = input("Enter the second string: ")
# def is_anagram(string1, string2):
#     string1 = string1.replace(" ", "").lower()
#     string2 = string2.replace(" ", "").lower()
#     return sorted(string1) == sorted(string2)
# result = is_anagram(s1, s2)
# if result:
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")

#18. To remove all duplicate characters while maintaining the original order of string.
# s = input("Enter a string: ")
# def remove_duplicates(string):
#     seen = set()
#     result = ""
#     for char in string:
#         if char not in seen:
#             seen.add(char)
#             result += char
#     return result
# res=remove_duplicates(s)
# print("String after removing duplicates:", res)

#19. To check whether a given substring exists in the main string or not.
# s1=input("Enter the main string: ")
# s2=input("Enter the substring: ")
# def substring_exists(main_string, substring):
#     if s2 in s1:
#         return True
#     else:
#         return False
# substring_check = substring_exists(s1, s2)
# if substring_check:
#     print("The substring exists in the main string.")
# else:
#     print("The substring does not exist in the main string.")

#20. To count how many times a specific word appears in a sentence
# v = input("Enter a sentence: ")
# def count_word_occurrences(sentence, word_to_count):
#     words = sentence.split()
#     count = 0
#     for word in words:
#         if word == word_to_count:
#             count += 1
#     return count
# occurrences = count_word_occurrences(v, 'the') 
# print("The word 'the' appears", occurrences, "times in the sentence.")

#21.Validate a password based on these conditions: 
# Minimum 8 characters 
# At least one uppercase letter 
# One lowercase letter 
# One digit 
# One special character.
#-> v = input("Enter a password: ")
# def validate_password(password):
#     if len(password) < 8:
#         return False
#     has_uppercase = any(char.isupper() for char in password)
#     has_lowercase = any(char.islower() for char in password)
#     has_digit = any(char.isdigit() for char in password)
#     has_special_char = any(not char.isalnum() for char in password)
    
#     return has_uppercase and has_lowercase and has_digit and has_special_char
# validation=validate_password(v)
# if validation:
#     print("The password is valid.")
# else:
#     print("The password is invalid.")

#22.Compress a string by counting consecutive repeated characters. 
#Example:
#Input: aaabbccccd
#Output: a3b2c4d1
# s = input("Enter a string: ")
# def compress_string(string):
#     if not string:
#         return ""
#     compressed = ""
#     count = 1
#     for i in range(1, len(string)):
#         if string[i] == string[i - 1]:
#             count += 1
#         else:
#             compressed += string[i - 1] + str(count)
#             count = 1
#     compressed += string[-1] + str(count)  # Add the last character and its count
#     return compressed
# result = compress_string(s)
# print("Compressed string:", result)

#23.Compress repeated characters and return the original string if compression does not reduce the length. 
# s = input("Enter a string: ")
# def compress_string(string):
#     if not string:
#         return ""
#     compressed = ""
#     count = 1
#     for i in range(1, len(string)):
#         if string[i] == string[i - 1]:
#             count += 1
#         else:
#             compressed += string[i - 1] + str(count)
#             count = 1
#     compressed += string[-1] + str(count)  
#     return compressed if len(compressed) < len(string) else string
# result = compress_string(s)
# if result == s:
#     print("Compression did not reduce the length. Original string:", result)
# else:
#     print("Compressed string:", result)

#24. Find the character with the highest frequency. 
# s = input("Enter a string: ")
# def highest_frequency_character(string):
#     frequency = {}
#     for char in string:
#         if char in frequency:
#             frequency[char] += 1
#         else:
#             frequency[char] = 1
#     max_freq = 0
#     max_char = ''
#     for char, count in frequency.items():
#         if count > max_freq:
#             max_freq = count
#             max_char = char
            
#     return max_char, max_freq
# result = highest_frequency_character(s)
# print(f"The character with the highest frequency is '{result[0]}' with a count of {result[1]}.")

#25.Find the second most frequently occurring character.
# s = input("Enter a string: ")
# def second_highest_frequency_character(string):
#     frequency = {}
#     for char in string:
#         if char in frequency:
#             frequency[char] += 1
#         else:
#             frequency[char] = 1
#     sorted_chars = sorted(frequency.items(), key=lambda item: item[1], reverse=True)  
#     if len(sorted_chars) < 2:
#         return None, None  # Not enough unique characters for a second highest
#     second_highest_char, second_highest_count = sorted_chars[1]
#     return second_highest_char, second_highest_count
# result = second_highest_frequency_character(s)
# if result[0] is not None:
#     print(f"The second most frequently occurring character is '{result[0]}' with a count of {result[1]}.")
# else:
#     print("There is no second most frequently occurring character.") 

#26.Encrypt and decrypt a message using the Caesar Cipher algorithm.
# s = input("Enter a message: ")
# def caesar_cipher_encrypt(message, shift):
#     encrypted_message = ""
#     for char in message:
#         if char.isalpha():
#             shift_base = ord('A') if char.isupper() else ord('a')
#             encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
#             encrypted_message += encrypted_char
#         else:
#             encrypted_message += char  
#     return encrypted_message
# result = caesar_cipher_encrypt(s, 3) 

#27.Validate whether a given email address follows a valid format. 
# s = input("Enter an email address: ")
# def validate_email(email):
#     import re
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     return re.match(pattern, email) is not None
# result = validate_email(s)
# if result:
#     print("The email address is valid.")
# else:
#     print("The email address is invalid.")

#28.Count the frequency of every word in a paragraph. 
# s= input("Enter a paragraph: ")
# def count_word_frequency(paragraph):
#     words = paragraph.split()
#     frequency = {}
#     for word in words:
#         word = word.lower()  
#         if word in frequency:
#             frequency[word] += 1
#         else:
#             frequency[word] = 1
#     return frequency
# result = count_word_frequency(s)
# print("Frequency of every word in the paragraph:", result)

#29.Reverse the order of words in a sentence without changing the words themselves. 

# s = input("Enter a sentence: ")
# def reverse_word_order(sentence):
#     words = sentence.split()
#     reversed_words = words[::-1]  
#     return ' '.join(reversed_words)
# result = reverse_word_order(s)
# print("Sentence after reversing the order of words:", result)

#30.Check whether one string is a rotation of another. 
#->
# s1 = input("Enter the first string: ")
# s2 = input("Enter the second string: ")
# def is_rotation(string1, string2):
#     if len(string1) != len(string2):
#         return False
#     return string2 in (string1 + string1)
# result = is_rotation(s1, s2)
# if result:
#     print("The second string is a rotation of the first string.")
# else:
#     print("The second string is not a rotation of the first string.")


