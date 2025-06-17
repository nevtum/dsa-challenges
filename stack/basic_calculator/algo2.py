def calc(acc: int, val: int, operand) -> int:
    if operand == '+':
        return acc + val
    if operand == '-':
        return acc - val
    if operand == '^':
        return acc ** val
    if operand == '*':
        return acc * val
    raise NotImplementedError("operand not supported")


def evaluate(expression: str)-> int:
    # remove all spaces
    expression = expression.replace(' ', '')

    # ensure all expressions start and end with parenthesis
    # so that calculation always goes through ')' branch at the end
    expression = f"({expression})"

    acc, val, operand, stack = 0, 0, '+', []

    for char in expression:
        # print(f"character is '{char}' in '{expression}'")
        if char.isdigit():
            # still not finished processing number
            val = val * 10 + int(char)
        elif char == '+':
             # end of the number, add to cumulative sum and reset val ptr
            acc = calc(acc, val, operand)
            operand = '+'
            val = 0
            # print("plus detected")
        elif char == '-':
            # end of the number, add to cumulative sum and reset val ptr
            acc = calc(acc, val, operand)
            operand = '-'
            val = 0
            # print("minus detected")
        elif char == '^':
            # end of the number, add to cumulative sum and reset val ptr
            acc = calc(acc, val, operand)
            operand = '^'
            val = 0
            # print("power detected")
        elif char == '*':
            # end of the number, add to cumulative sum and reset val ptr
            acc = calc(acc, val, operand)
            operand = '*'
            val = 0
            # print("multiplication detected")
        elif char == '(':
            # within a new scope so all variables need to be reset
            # memoize acc and last operand in outer scope so that it can be
            # retrieved again upon exiting scope
            stack.append((acc, operand))
            acc, val, operand = 0, 0, '+'
            # print("entering new scope")
        elif char == ')':
            # exiting scope. cumulative sum and last operand in outer expression
            # needs to be restored before adding inner_sum to it make sure to
            # reset val ptr so next number can be properly read in the outer
            # expression
            # breakpoint()
            inner_val = calc(acc, val, operand)
            print(f"inner_val={inner_val}")
            acc, operand = stack.pop()
            acc = calc(acc, inner_val, operand)
            val = 0
            operand = '+'
            # print("exiting scope")

        print(f"acc={acc}, val={val}, operand={operand}, stack={stack}")
    return acc
