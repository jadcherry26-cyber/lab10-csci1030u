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
    # region Outline:
    # Restate: Evaluate an expression written in Reverse Polish Notation,
    # where each operator uses the two most recent values.
    #
    # Hand example: ["2", "1", "+", "3", "*"]
    #   Read 2, 1: keep them for later.
    #   Read +: combine 2 and 1 to get 3.
    #   Read 3, *: combine 3 and 3 to get 9.
    #
    # Approach:
    #   Use a stack of numbers.
    #   For each token:
    #     - If it is a number, convert it to an integer and push it.
    #     - If it is an operator, pop the right operand, then the left
    #       operand. Apply the operator in that order and push the result.
    #   The final stack value is the answer.
    #   For division, make sure the result truncates toward zero.
    # endregion
    stack = []
    for token in tokens:
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                result = left + right
                stack.append(result)
            elif token == "-":
                result = left - right
                stack.append(result)
            elif token == "*":
                result = left * right
                stack.append(result)
            elif token == "/":
                result = int(left / right)
                stack.append(result)
    return stack[-1]


def decode_string(s):
    # region Outline:
    # Restate: Decode text where a number before brackets says how many
    # times to repeat the bracketed text. Brackets can contain more
    # bracketed patterns.
    #
    # Hand example: "3[a2[c]]"
    #   Inside the inner brackets, "c" repeats 2 times -> "cc".
    #   Then "a" + "cc" -> "acc".
    #   Repeat "acc" 3 times -> "accaccacc".
    #
    # Approach:
    #   Scan the input from left to right, building the current text and
    #   current repeat number.
    #   When a digit appears, add it to the repeat number (so multi-digit
    #   numbers work).
    #   When "[" appears, save the current text and repeat number on stacks,
    #   then start a fresh text and repeat number for the bracket contents.
    #   When "]" appears, repeat the current text by the saved number and
    #   attach it to the saved text.
    #   When the scan is done, the current text is the decoded result.
    #  endregion
    stack = []
    current_text = ""
    repeat_count = 0

    for char in s:
        # We'll handle digits, [, ], and regular letters here
        if char.isdigit():
            repeat_count = repeat_count * 10 + int(char)
        elif char == "[":
            stack.append((current_text, repeat_count))
            current_text = ""
            repeat_count = 0
        elif char.isalpha():
            current_text += char
        elif char == "]":
            previous_text, repeat_count = stack.pop()
            current_text = previous_text + current_text * repeat_count
            repeat_count = 0
    return current_text


def daily_temperatures(temps):
    # region Outline:
    # Restate: For each day, find the number of days until a later,
    # strictly warmer temperature. Use 0 if there is no such day.
    #
    # Hand example: [73, 74, 75, 71]
    #   Day 0 (73) is answered when day 1 (74) appears: wait 1 day.
    #   Day 1 (74) is answered when day 2 (75) appears: wait 1 day.
    #   Days 2 and 3 have no warmer day in this small example.
    #
    # Approach:
    #   Make an answer list filled with 0s.
    #   Keep a stack of day indices whose warmer day has not been found.
    #   For each new day, while its temperature is warmer than the
    #   temperature at the index on top of the stack:
    #     - pop that earlier index;
    #     - set its answer to the difference between the current day and
    #       that earlier day.
    #   Push the current day index onto the stack.
    #   Any indices left on the stack keep answer 0.
    # endregion
    pass


def num_islands(grid):   # Part 4 - stretch (optional)
    # region Outline:
    # Restate: Count groups of land cells ("1") connected horizontally or
    # vertically. Diagonal contact does not connect islands.
    #
    # Hand example: ["11000", "11000", "00100", "00011"]
    #   The upper-left 2-by-2 block is one island.
    #   The single land cell in the third row is another.
    #   The two touching cells at the lower right are a third.
    #   Total: 3 islands.
    #
    # Approach:
    #   Keep track of which land cells have already been visited.
    #   Scan every cell in the grid.
    #   Whenever an unvisited land cell is found:
    #     - increase the island count;
    #     - explore all land cells connected to it using a stack or queue;
    #     - mark cells visited as they are added, so they are not explored
    #       again.
    #   During exploration, check only the four neighbors: up, down, left,
    #   and right. Check that each neighbor is inside the grid.
    #   Return the island count.
    # endregion
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
