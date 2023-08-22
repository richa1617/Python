
score = {
 "A X": 3,
 "A Y": 4,
 "A Z": 8,
 "B X": 1,
 "B Y": 5,
 "B Z": 9,
 "C X": 2,
 "C Y": 6,
 "C Z": 7,
}

with open("three.txt", "r") as input_file:
 total=0
 for value in input_file: 
    stripped=value.strip()
    total=total + score[stripped]
print(total)   