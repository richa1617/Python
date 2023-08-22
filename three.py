


win = {
 "A X": 4,
 "A Y": 8,
 "A Z": 3,
 "B X": 1,
 "B Y": 5,
 "B Z": 9,
 "C X": 7,
 "C Y": 2,
 "C Z": 6
}

with open("three.txt", "r") as input_file:
 total=0
 for value in input_file: 
    stripped=value.strip()
    total=total + win[stripped]
print(total)    

