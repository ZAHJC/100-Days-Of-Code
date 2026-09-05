
names = []
startingLetterPath = "./Input/Letters/starting_letter.txt"
namesPath = "./Input/Names/invited_names.txt"

with open(namesPath, "r") as file:
    for line in file:
        names.append(line.strip())

for name in names:
    letterInProg = []
    with open(startingLetterPath, "r") as file:
        for line in file:
            letterInProg.append(line)
    letterInProg[0] = letterInProg[0].replace("[name]", name)

    with open(f"./Output/ReadyToSend/{name}.txt", "w") as file:
            file.writelines(letterInProg)

