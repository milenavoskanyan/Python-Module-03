#!/usr/bin/python3
import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        args = sys.argv[1:]
        print(f"Arguments received: {len(args)}")
        idx = 1
        for arg in args:
            print(f"Argument {idx}: {arg}")
            idx += 1
    print(f"Total arguments: {len(sys.argv)}")
