import sys

def search(grid, pos, dir):
    N = len(grid)
    M = len(grid[0])
    x, y = pos
    dx, dy = dir
    x -= dx
    y -= dy
    for c in "MAS":
        if x < 0 or x >= N or y < 0 or y >= M:
            return False
        if grid[x][y] != c:
            return False
        x += dx
        y += dy
    return True

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
            pos = i, j
            for forward_diag in [(1, 1), (-1, -1)]:
                for backward_diag in [(1, -1), (-1, 1)]:
                    if search(grid, pos, forward_diag) and search(grid, pos, backward_diag):
                        count += 1
    print(count)

if __name__ == "__main__":
    main()