import argparse
import hashlib
import itertools

def hash_password(password, algo="sha256"):
    h = hashlib.new(algo)
    h.update(password.encode())
    return h.hexdigest()

def dictionary_cracker(target_hash, wordlist, algo="sha256"):
    with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
        for word in f:
            word = word.strip()
            if hash_password(word, algo) == target_hash:
                return word
    return None

def brute_force_cracker(target_hash, max_length=4, algo="sha256"):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            candidate = ''.join(attempt)
            if hash_password(candidate, algo) == target_hash:
                return candidate
    return None

def main():
    parser = argparse.ArgumentParser(description="Password Cracker Tool")
    parser.add_argument("--mode", choices=["dictionary", "bruteforce"], required=True,
                        help="Attack mode: dictionary or bruteforce")
    parser.add_argument("--hash", required=True, help="Target hash to crack")
    parser.add_argument("--algo", default="sha256", help="Hash algorithm (sha256, md5, sha1, etc.)")
    parser.add_argument("--wordlist", help="Path to dictionary file (for dictionary mode)")
    parser.add_argument("--max-length", type=int, default=4, help="Max length for brute force")

    args = parser.parse_args()

    if args.mode == "dictionary":
        if not args.wordlist:
            print("Error: --wordlist required for dictionary mode")
            return
        result = dictionary_cracker(args.hash, args.wordlist, args.algo)
    else:
        result = brute_force_cracker(args.hash, args.max_length, args.algo)

    if result:
        print(f"[+] Password cracked: {result}")
    else:
        print("[-] Failed to crack password.")

if __name__ == "__main__":
    main()
