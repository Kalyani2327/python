# 1. Create a string with your name and print it.
name="kalyani"
print(name)

# 2. Get the first character from the string.
name="kalyani"
print(name[0])

# 3. Get the last character from the string.
name="kalyani"
print(name[-1])

# 4. Concatenate two strings.
sen1="hello i am "
sen2="kalyani"
print(sen1+sen2)

# 5. Repeat a string 3 times.
name="python "
print(name*3)


# 6. Slice the first 5 characters.
word="programming language"
print(word[:5:])

# 7. Reverse a string using slicing.
word="programming"
print(word[::-1])

# 8. Check if a substring exists in a string.
sen1="i am from guntur"
sen2="guntur"
if sen1 in sen2:
    print("Substring exists in a string")
else:
    print("Substring does not exist in a string")


# 9. Find the length of a string.
sen="Programming"
print(len(sen))


# 10. Convert string to uppercase.
name="kalyani"
print(name.upper())

# 11. Convert string to lowercase.
name="KALYANI"
print(name.lower())

# 12. Capitalize the first letter.
city="guntur"
print(city.capitalize())

# 13. Convert a string to title case.
sen="i am learning python"
print(sen.title())

# 14. Remove leading spaces using lstrip().
user="             kalyani              "
user=user.lstrip()
print(user,len(user))

# 15. Remove trailing spaces using rstrip().
user="             Bindu                "
user=user.rstrip()
print(user,len(user))

