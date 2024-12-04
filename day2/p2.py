import sys

def check_diff(diffs):
    if diffs[0] < 0:
        diffs = [-d for d in diffs]
    return all(d >= 1 and d <= 3 for d in diffs)

def mkdiff(vs):
    return [vs[i] - vs[i-1] for i in range(1, len(vs))]

def is_safe(vals):
    orig = vals
    if check_diff(mkdiff(vals)):
        return True
    for i in range(len(orig)):
        vals = orig[:i] + orig[i+1:]
        if check_diff(mkdiff(vals)):
            return True
    return False

def main():
    safe = 0
    for report in sys.stdin: 
        report = report.strip()
        if not report:
            continue
        vals = [int(v) for v in report.split()]
        if is_safe(vals):
            safe += 1
    print(safe)

if __name__ == "__main__":
    main()