import sys

from diff_eq import solve


def main():
    args = sys.argv[1]
    print(solve(args[0]))

