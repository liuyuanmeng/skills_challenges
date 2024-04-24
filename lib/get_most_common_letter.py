def get_most_common_letter(text):
    alphabet = [chr(i + 96) for i in range(1, 27)]
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1
    characters = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    letter = [char for char in characters if char[0] in alphabet][0][0]
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
