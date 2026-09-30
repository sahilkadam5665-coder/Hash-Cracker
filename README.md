# 🔑 Password Cracker Tool
# 📖 Overview
The Password Cracker is a Python-based security tool that demonstrates how weak passwords can be exploited. It attempts to crack hashed passwords using different attack strategies, highlighting the importance of strong password policies in real-world systems.

# ✨ Features
- Supports multiple hashing algorithms (MD5, SHA1, SHA256, etc.).
- Dictionary Attack: Tests passwords against a wordlist file (e.g., rockyou.txt).
- Brute Force Attack: Generates all possible combinations up to a specified length.
- Modular command-line interface with flexible options for mode, hash type, wordlist, and maximum length.
- Extensible design for adding rainbow tables, multiprocessing, and custom character sets.

# 🛠️ Tech Stack
- Language: Python 3
- Libraries: hashlib, argparse, itertools

# ⚙️ Installation
-Clone the repository and navigate into the project folder:
 bash:
 # git clone https://github.com/your-username/password-cracker.git
 cd password-cracker

# 🚀 Usage
 - Run the tool from the command line:
 - Dictionary Attack
   bash:
   # python cracker.py --mode dictionary --hash <hash_here> --wordlist rockyou.txt --algo sha256

 -  Brute Force Attack
   bash:
   #  python cracker.py --mode bruteforce --hash <hash_here> --max-length 4 --algo md5

# 📂 Project Structure
  - Code
password-cracker/

│── cracker.py        # Main script

│── README.md         # Documentation

# 🔮 Future Enhancements
- Rainbow table lookup for faster cracking.
- Multithreading/multiprocessing for speed.
- Custom character sets for brute force.
- Logging cracked results to a file.

# ⚠️ Disclaimer
- This tool is for educational and security research purposes only.
- Do not use it against systems without explicit permission. Unauthorized password cracking may be illegal.
