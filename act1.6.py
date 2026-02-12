sentence =input("Enter your snentence:")

print("\nUppercase:", sentence.upper())
print("\nLowercase:", sentence.lower())

count_a = sentence.lower().count("a")
print("\nNumber of letter 'a':",count_a)

if sentence.startswith("Hello"):
    print("\nThe sentence starts with 'Hello'")
else:
    print("\nThe sentence does not start with 'Hello'")
    
    words = sentence.split()
    print("Words in the sentence")
    for word in words:
        print(word)  