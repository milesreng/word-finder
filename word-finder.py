def find_word(words, lst, exclude):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for word in words:
        match = True
        for i in range(5):
            if lst[i] in alphabet and word[i] != lst[i]:
                match = False
            elif word[i].upper() in exclude:
                match = False
        if match:
            print(word)

def exclude():
    excluded = []
    letter = input("please enter a letter or type 1 to terminate: ")
    while (letter != "1"):
        excluded.append(letter)
        letter = input("please enter a letter or type 1 to terminate: ")
    return "".join(excluded).upper()

if __name__ == "__main__":
    with open("resources/fiveletterwords.txt") as file:
        valid_words = [line.rstrip().upper() for line in file]

    letters = ["_" for i in range(5)]

    for i in range(5):
        letters[i] = input("please enter letter #" + str(i + 1) + " (or \"_\" if unknown): ").upper()
    
    unused = input("would you like to input letters to exclude (y/n)? ")
    non_use = ""

    if unused == "y":
        non_use = exclude()

    find_word(valid_words, "".join(letters), non_use)