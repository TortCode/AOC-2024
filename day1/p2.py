import sys
from collections import Counter

def main():
    left = []
    right = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        vals = [int(v) for v in line.split()]
        left.append(vals[0])
        right.append(vals[1])
    right_count = Counter(right)
    score = 0
    for l in left:
        score += l * right_count[l]
    print(score)

if __name__ == "__main__":
    main()