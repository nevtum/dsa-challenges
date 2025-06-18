def add(expression: str) -> int:
    # remove all spaces
    expression = expression.replace(" ", "")

    # ensure all expressions start and end with parenthesis
    # so that calculation always goes through ')' branch at the end
    expression = f"({expression})"

    acc, val, sign, stack = 0, 0, 1, []

    for char in expression:
        print(f"character is '{char}' in '{expression}'")
        if char.isdigit():
            # still not finished processing number
            val = val * 10 + int(char)
        elif char == "+":
            # end of the number, add to cumulative sum and reset val ptr
            acc += val * sign
            sign = 1
            val = 0
            # print("plus detected")
        elif char == "-":
            # end of the number, add to cumulative sum and reset val ptr
            acc += val * sign
            sign = -1
            val = 0
            # print("minus detected")
        elif char == "(":
            # within a new scope so all variables need to be reset
            # memoize acc and last sign in outer scope so that it can be
            # retrieved again upon exiting scope
            stack.append((acc, sign))
            acc, val, sign = 0, 0, 1
            # print("entering new scope")
        elif char == ")":
            # exiting scope. cumulative sum and last sign in outer expression
            # needs to be restored before adding inner_sum to it make sure to
            # reset val ptr so next number can be properly read in the outer
            # expression
            inner_sum = acc + val * sign
            acc, sign = stack.pop()
            acc += inner_sum * sign
            val = 0
            # print("exiting scope")

        # print(f"acc={acc}, val={val}, sign={sign}, stack={stack}")
    return acc


if __name__ == "__main__":
    assert add("18 + (2 - 10 + (1 + 2)) + 4") == 17
    print("end")
