#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    if __name__ == "__main__":
        if len(sys.argv) == 4:
            a = sys.argv[1]
            op = sys.argv[2]
            b = sys.argv[3]
            s = ['+', '-', '*', '/']
            if op not in s:
                print('Unknown operator. Available operators: +, -, * and /')
                sys.exit(1)
            if len(sys.argv) != 4:
                print('Usage: ./100-my_calculator.py <a> <operator> <b>')
                sys.exit(1)
            else:
                if op == '+':
                    print('{} + {} = {}'.format(a, b, add(a, b)))
                elif op == '-':
                    print('{} - {} = {}'.format(a, b, sub(a, b)))
                elif op == '*':
                    print('{} * {} = {}'.format(a, b, mul(a, b)))
                else:
                    print('{} / {} = {}'.format(a, b, div(a, b)))
