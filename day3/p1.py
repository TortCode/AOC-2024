import sys

class Parser:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def done(self):
        return self.pos >= len(self.text)

    def next(self):
        self.pos += 1

    def peek(self):
        return self.text[self.pos] if not self.done() else None
    
    def match(self, c):
        if self.peek() == c:
            self.next()
            return True
        return False

    def parse_number(self):
        n = 0
        c = self.peek()
        if c is None or not c.isdigit() or c == '0':
            return None
        l = 0
        while l < 3 and c is not None and c.isdigit():
            n = n * 10 + ord(c) - ord('0')
            self.next()
            c = self.peek()
            l += 1
        n = int(n)
        return n

    def parse_mul(self):
        for c in "mul(":
            if not self.match(c):
                return None
        a = self.parse_number()
        if a is None:
            return None
        if not self.match(','):
            return None
        b = self.parse_number()
        if b is None:
            return None
        if not self.match(')'):
            return None
        return a * b
    
    def parse_all(self):
        s = 0
        while True:
            while not self.done() and self.peek() != 'm':
                self.next()
            if self.done():
                break
            n = self.parse_mul()
            if n is not None:
                s += n
        return s

def main():
    text = sys.stdin.read()
    p = Parser(text)
    print(p.parse_all())

if __name__ == "__main__":
    main()