from stack import Stack


def eval_postfix(expr):
    if not isinstance(expr, str):
        raise SyntaxError("Parameter passed to eval_postfix() is not a string. Parameter must be a string.")

    numbers_stack = Stack()
    operators = ["+", "-", "*", "/"]

    for char in expr:
        if char != " ":
            if char not in operators:
                numbers_stack.push(char)
            else:
                value1 = int(numbers_stack.pop())
                value2 = int(numbers_stack.pop())
                if char == "+":
                    result = value2 + value1
                elif char == "-":
                    result = value2 - value1
                elif char == "*":
                    result = value2 * value1
                elif char == "/":
                    result = value2 / value1
                numbers_stack.push(result)
    final_result = float(numbers_stack.pop())

    return final_result


def in2post(expr):
    if not isinstance(expr, str):
        raise ValueError("Parameter passed to in2post() is not a string. Parameter must be a string.")

    symbols_stack = Stack()
    operators = ["+", "-", "*", "/"]
    output = []
    precedence = {"*": 2, "/": 2, "+": 1, "-": 1}

    for char in expr:
        if char != " ":
            if char == "(":
                symbols_stack.push(char)
            elif char.isdigit():
                output.append(char)
            elif char in operators:
                while (not symbols_stack.size() == 0 and
                       symbols_stack.top() != "(" and
                       precedence.get(symbols_stack.top(), 0) >= precedence[char]):
                    output.append(symbols_stack.pop())
                symbols_stack.push(char)
            elif char == ")":
                while (not symbols_stack.size() == 0 and
                       symbols_stack.top() != "("):
                    output.append(symbols_stack.pop())
                if symbols_stack.size() == 0 or symbols_stack.top() != "(":
                    raise SyntaxError("Invalid expression: Mismatched parentheses.")
                symbols_stack.pop()

    while not symbols_stack.size() == 0:
        if symbols_stack.top() == "(":
            raise SyntaxError("Invalid expression: Mismatched parentheses.")
        output.append(symbols_stack.pop())

    return " ".join(output)


def main():
    def output_results(data):
        infix = data
        postfix = in2post(data)
        answer = eval_postfix(postfix)
        text = f"infix: {infix}\npostfix: {postfix}\nanswer: {answer}\n"

        return text

    with open("data.txt", "r") as file:
        expressions = [line.strip() for line in file]
        for expr in expressions:
            print(output_results(expr))
        """
        infix_expressions = []
        postfix_expressions = []
        answers = []
        correct_infix = ['4', '5  +7', '7*5', '(5-3)', '5/5', '8*5+3', '8*(5+3)', '8+3*5-7', '(8+3)*(5-6)', '((8+3)*(2-7))', '((8+3)*2)-7', '(8*5)+((3-2)-7*3)', '((8*5+3)-7)-(5*3)', '7*9+7-5*6+3-4']
        correct_postfix = ['4', '5 7 +', '7 5 *', '5 3 -', '5 5 /', '8 5 * 3 +', '8 5 3 + *', '8 3 5 * + 7 -', '8 3 + 5 6 - *', '8 3 + 2 7 - *', '8 3 + 2 * 7 -', '8 5 * 3 2 - 7 3 * - +', '8 5 * 3 + 7 - 5 3 * -', '7 9 * 7 + 5 6 * - 3 + 4 -']
        correct_answers = ['4.0', '12.0', '35.0', '2.0', '1.0', '43.0', '64.0', '16.0', '-11.0', '-55.0', '15.0', '20.0', '21.0', '39.0']

        i = 0
        for expr in expressions:
            infix_expressions.append(expr)
            postfix = in2post(expr)
            postfix_expressions.append(postfix)
            answers.append(eval_postfix(postfix))

            if infix_expressions[i] != correct_infix[i]:
                print('\n------------ INFIX IS NOT CORRECT ------------\n'
                      f'infix: {infix_expressions[i]}\n{correct_infix[i]} <- infix should be\n')
            if postfix_expressions[i] != correct_postfix[i]:
                print('\n------------ POSTFIX IS NOT CORRECT ------------\n'
                      f'postfix: {postfix_expressions[i]}\n{correct_postfix[i]} <- postfix should be \n')
            if answers[i] != correct_answers[i]:
                print('\n------------ ANSWER IS NOT CORRECT ------------\n'
                      f'answer: {answers[i]}\n{correct_answers[i]} <- answer should be \n')
            print(f"#{i + 1}")
            print(f'infix: {infix_expressions[i]}\n'
                  f'postfix: {postfix_expressions[i]}\n'
                  f'answer: {answers[i]}\n')
            i += 1
            """


if __name__ == "__main__":
    main()
