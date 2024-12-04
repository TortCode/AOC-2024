import sys

def search(grid, pos, dir):
    N = len(grid)
    M = len(grid[0])
    x, y = pos
    dx, dy = dir
    for c in "XMAS":
        if x < 0 or x >= N or y < 0 or y >= M:
            return False
        if grid[x][y] != c:
            return False
        x += dx
        y += dy
    return True

dirs = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, 1),
    (1, -1),
    (-1, -1),
]

def main():
    grid = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        grid.append(line)

    count = 0
    N = len(grid)
    M = len(grid[0])
    for i in range(N):
        for j in range(M):
            for dir in dirs:
                if search(grid, (i, j), dir):
                    count += 1
    print(count)

if __name__ == "__main__":
    main()