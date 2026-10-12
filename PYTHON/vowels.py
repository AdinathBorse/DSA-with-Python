vowels = ['a','e','i','o','u','A','E','I','O','U']

vowelsCnt = 0
ConsonantCnt = 0

Name = input("Enter the Sring : ")

for i in Name :
    if i in vowels :
        vowelsCnt += 1
    else: 
        ConsonantCnt += 1    
    
print("number of vowels in String :",vowelsCnt)    
print("number of Consonant in String :",ConsonantCnt)    

# 1. Definition
# This program counts characters in an input string by checking whether each
# character is one of the five English vowels, in either lowercase or uppercase.
#
# 2. Explanation
# The loop examines every character. Membership in the vowels list increments
# vowelsCnt; every other character increments ConsonantCnt. As written, spaces,
# digits, and punctuation are also counted as consonants. Character counting is
# useful for basic text analysis.
#
# 3. Real-life example
# A teacher could count vowel sounds represented by letters in a student's
# written word, while noting that this program counts characters, not sounds.
#
# 4. Example (with code)
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# vowel_count = 0
# other_count = 0
# name = input("Enter the Sring : ")
# for character in name:
#     if character in vowels:
#         vowel_count += 1
#     else:
#         other_count += 1
# print("number of vowels in String :", vowel_count)
# print("number of Consonant in String :", other_count)
#
# 5. Output Explanation
# For input Hello, the output is:
# number of vowels in String : 2
# number of Consonant in String : 3
# e and o are vowels. H, l, and l are counted by the else branch.
#
# 6. Summary
# - The loop checks each character in the input text.
# - The in operator tests whether a character is in the vowel list.
# - Uppercase and lowercase vowels are both recognized.
# - Every non-vowel character is counted in the other/consonant total.