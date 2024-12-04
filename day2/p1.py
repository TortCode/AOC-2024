import sys

def main():
    safe = 0
    for report in sys.stdin: 
        report = report.strip()
        if not report:
            continue
        vals = [int(v) for v in report.split()]
        diffs = [vals[i] - vals[i - 1] for i in range(1, len(vals))]
        if diffs[0] < 0:
            diffs = [-d for d in diffs]
        if all(d >= 1 and d <= 3  for d in diffs):
            safe += 1
    print(safe)

if __name__ == "__main__":
    main()