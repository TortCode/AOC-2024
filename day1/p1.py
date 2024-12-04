import sys

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
    left.sort()
    right.sort()
    dist = 0
    for l, r in zip(left, right):
        dist += abs(l - r)
    print(dist)

if __name__ == "__main__":
    main()