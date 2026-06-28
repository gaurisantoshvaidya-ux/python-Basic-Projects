def analyze_string(s):
    # Print length
    print("Length of the string:", len(s))

    # Print reverse of the string
    print("Reversed string:", s[::-1])

    # Count vowels (case insensitive)
    vowels = "aeiou"
    count = 0
    for ch in s.lower():
        if ch in vowels:
            count += 1
    print("Number of vowels:", count)

    # Print each character with positive and negative index
    print("\nCharacter with Positive and Negative Index:")
    for i in range(len(s)):
        print(f"Character: {s[i]}, Positive Index: {i}, Negative Index: {i - len(s)}")


# User input
text = input("Enter a string: ")

# Handle empty string case
if text == "":
    print("The string is empty!")
else:
    analyze_string(text)