# CodeForcesTester

This is a small program to help you quickly run test cases to test your program for a specific Codeforces problem

To run a specific contest problem pass the contest number and question letter as arguments or change the variables in the code. Then the scipt crawls the web, grabs the specific problem's inputs and the outputs, runs your script with the inputs, compares your scripts output with the correct output.

IMPORTANT:
	- You have to have python 3 installed on your machine
	- You script files have to be named <problem letter>.py example: A.py
	- This does not work with compiling other languages at the moment
	- This scipt will create a directory named after the contest number, your scipt should be in that directory
