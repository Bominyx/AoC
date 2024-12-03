#https://adventofcode.com/2024/day/3
import re

with open("input.txt") as file:
    # Pattern sucht nach gültigen Operationen
    # Die erste gültige Art von Operation sind Multiplikationen
    # Weitere sind do() und don't() um Multiplikation zu toggeln
    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", file.read())

result1 = 0 # Hält Ergebnis für Part 1
result2 = 0 # Hält Ergebnis für Part 2
is_enabled = True # boolean um anzugeben ob Multiplikationen erlaubt sind. Beim Start immer erlaubt

for instruction in instructions:
    if instruction == "do()":
        is_enabled = True
    elif instruction == "don't()":
        is_enabled = False
    elif instruction[:3] == "mul":
        # Berechnung für Part 1. Hier ist es egal ob Multiplikation erlaubt ist
        # mit dem Slize-Operator "mul(" und ")" entfernen
        number1, number2 = instruction[4:-1].split(',')
        result1 += int(number1) * int(number2)
        if is_enabled:
            # Berechnung für Part 2
            number1, number2 = instruction[4:-1].split(',')
            result2 += int(number1) * int(number2)

print(f"All Multiplications {result1}")
print(f"Enabled Multiplications {result2}")