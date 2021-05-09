import sys


def rectangles_15232():
    r = int(sys.stdin.readline())
    c = int(sys.stdin.readline())
    for idx in range(r):
        sys.stdout.write(f"{'*' * c}\n")


if __name__ == '__main__':
    rectangles_15232()
