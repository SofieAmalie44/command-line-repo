#!/usr/bin/env python3

import sys

def greeting():
	print("Hello! What is your name?")

def main():
	greeting()
	name = input("Your name: ")
	
	print(f"Hi {name}, nice to meet you")

if __name__ == "__main__":
    main()

