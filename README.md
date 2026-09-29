# Hash-Cracker
This tool highlights the risks of weak password practices by attempting to crack hashed passwords using different attack strategies. It is designed for educational and security research purposes, showing why strong password policies are essential in any system.
# Setup
1 Save the code I gave you into a file called cracker.py.
2 Make sure you have Python 3 installed (check with python --version).
3 Open a terminal (Command Prompt, PowerShell, or Linux shell).
4 Navigate to the folder where cracker.py is saved.

# RUNNING OF THE TOOL
1. Dictionary Attack
   If you have a wordlist file (e.g., rockyou.txt), run:

   python cracker.py --mode dictionary --hash <hash_here> --wordlist rockyou.txt --algo sha256

   (Replace <hash_here> with the actual hash you want to crack.)

2. Brute Force Attack

   python cracker.py --mode bruteforce --hash <hash_here> --max-length 4 --algo md5

   (--max-length sets the maximum password length to try.)
