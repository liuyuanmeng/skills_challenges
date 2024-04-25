# def get_most_common_letter(text):
#     alphabet = [chr(i + 96) for i in range(1, 27)]
#     counter = {}
#     for char in text:
#         counter[char] = counter.get(char, 0) + 1
#     characters = sorted(counter.items(), key=lambda item: item[1], reverse=True)
#     letter = [char for char in characters if char[0] in alphabet][0][0]
#     return letter


# print(f"""
# Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
# Expected: o
# Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
# """)
def get_most_common_letter(text):
    # Define the alphabet
    alphabet = [chr(i + 96) for i in range(1, 27)]

    # Initialize a dictionary to count occurrences of each character
    counter = {}

    # Count occurrences of each character in the text
    for char in text:
        counter[char] = counter.get(char, 0) + 1

    # Sort characters by their counts in descending order
    characters = sorted(
        counter.items(), key=lambda item: item[1], reverse=True)

    # Find the most common letter that belongs to the alphabet
    letter = [char for char in characters if char[0] in alphabet][0][0]

    return letter


text = "the roof, the roof, the roof is on fire!"

# Print original text
print("Original text:", text)

# Print character counts
counter = {}
for char in text:
    counter[char] = counter.get(char, 0) + 1
print("Character counts:", counter)

# Print sorted characters
characters = sorted(counter.items(), key=lambda item: item[1], reverse=True)
print("Sorted characters:", characters)

# Print most common letter
alphabet = [chr(i + 96) for i in range(1, 27)]
letter = [char for char in characters if char[0] in alphabet][0][0]
print("Most common letter:", letter)
