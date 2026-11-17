# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    '''
    I will make a new list and append values from token to the list. By checking if a operand is the token,
    once I find a value that isn't a num, I will pop the values in the list and call
    a function that checks the operand I just landed on and performs 
    a computation based on that value. Then, I add it back with append.
    '''

    #   ...
    # TODO: `tokens` is a list of strings in Reverse Polish Notation - either an integer
    #   or one of the operators "+", "-", "*", "/". Evaluate it and return the integer
    #   result. Division should truncate toward zero (int(a / b)).
    #   Example: ["2","1","+","3","*"]  ->  9
    numbers: list = []
    for token in tokens:
        if token in ("+", "-", "*", "/"):
            b = numbers.pop()   
            a = numbers.pop()
            numbers.append(do_operation(a, b, token))
        else:
            numbers.append(int(token))
    return numbers[-1]
    
def do_operation(a: int, b: int, op: str) -> int:
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        return int(a / b)



def decode_string(s):
    # Outline:
    '''
    I have to take a string written like k[encoded] and repeat whatever character is in the brackets k amount of times. 
    I will keep track of the number in front by checking if the char at s is a digit. If I hit a parenthesis, I will
    append a tuple with the string to copy and the num. Once I hit the closing parenthesis, I will pop the entire current string as a tuple
    and add it to the new string
    '''
    #   ...
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"
    stack = []
    currentString = ""
    numStr = ""
    
    for char in s:
        if char.isdigit():
            numStr += char
        elif char == "[":
            stack.append((currentString, int(numStr)))
            currentString = ""
            numStr = ""
        elif char == "]":
            prevString, i = stack.pop()
            currentString = prevString + currentString * i
        else:
            currentString += char
    
    return currentString


def daily_temperatures(temps):
    # Outline:
    '''
    I will count how many days I'll have to wait for a warmer temperature, otherwise, I'll return 0. I'll do this by
    just using a for loop to go through the values and append the subtraction of the index's of the warmer and colder temperature
    to keep track of wait times.
    '''
    #   ...
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]
    daysWait = []

    for day in range(len(temps)):
        wait = 0
        for nextDay in range(day + 1, len(temps)):
            if temps[nextDay] > temps[day]:
                wait = nextDay - day
                break
        daysWait.append(wait)

    return daysWait


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    print(eval_rpn(["2","1","+","3","*"]))
    print(decode_string("3[a]2[bc]"))   # returns "aaabcbc"
    print(decode_string("3[a2[c]]"))    # returns "accaccacc"
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))   # returns [1, 1, 4, 2, 1, 1, 0, 0]
    print(daily_temperatures([30, 40, 50, 60]))                 # returns [1, 1, 1, 0]


if __name__ == "__main__":
    main()
