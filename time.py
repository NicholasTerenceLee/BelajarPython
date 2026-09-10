import time as t
import sys

def p(text, delay):
    for texts in text:
        t.sleep(delay)
        sys.stdout.write(texts)

p("Hello", 0.05)
print()
p("How are you?", 0.1)
print()
x = input()
p("I'm doing all great", 0.065)
