PLACEHOLDER = "[name]"

with open("./input/names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)


with open("./input/letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)




