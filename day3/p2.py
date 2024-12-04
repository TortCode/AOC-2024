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
    
    def match(self, s):
        for c in s:
            if not self.peek() == c:
                return False
            self.next()
        return True

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
        if not self.match("mul("):
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

    def parse_cond(self):
        if not self.match("do"):
            return None
        match self.peek():
            case '(':
                if self.match("()"):
                    return True
            case 'n':
                if self.match("n't()"):
                    return False
        return None
    
    def parse_all(self):
        enable = True
        s = 0
        while not self.done():
            c = self.peek()
            if c == 'm' and enable:
                n = self.parse_mul()
                if n is not None:
                    s += n
            elif c == 'd':
                flag = self.parse_cond()
                if flag is not None:
                    enable = flag
            else:
                self.next()
        return s

def main():
    text = sys.stdin.read()
    p = Parser(text)
    print(p.parse_all())

if __name__ == "__main__":
    main()