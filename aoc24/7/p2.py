import re

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == "+":
            result += numbers[i + 1]
        elif operators[i] == "*":
            result *= numbers[i + 1]
        elif operators[i] == "||":
            result = int(str(result) + str(numbers[i + 1]))
    return result

def generate_operator_combinations(num_operators):
    operators = []
    operator_types = ["+", "*", "||"]
    for i in range(len(operator_types) ** num_operators):
        combination = []
        for j in range(num_operators):
            combination.append(operator_types[(i // (len(operator_types) ** j)) % len(operator_types)])
        operators.append(combination)
    return operators

def main(doc):
    total_calibration = 0
    
    for line in doc:
        parts = line.split(":")
        test_value = int(parts[0].strip())
        numbers = list(map(int, parts[1].strip().split()))
        
        num_operators = len(numbers) - 1
        operator_combinations = generate_operator_combinations(num_operators)
        
        valid = False
        for operators in operator_combinations:
            if evaluate_expression(numbers, operators) == test_value:
                valid = True
                break
        
        if valid:
            total_calibration += test_value
    
    return total_calibration

if __name__ == "__main__":
    with open("input.txt") as file:
        document = [line.strip() for line in file]
    result = main(document)
    print(result)
