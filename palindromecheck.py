# Task-3: Check the given string is palindrom or not

import sys
s = str(sys.argv[1])
#String Reverse
reverse=s[-1::-1]
if (s == reverse):
    print("Provided string \"" + s + "\" is Palindrome")
else:
    print("Provided string \"" + s + "\" is not Palindrome")
