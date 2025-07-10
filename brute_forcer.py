def dummy_login(username, password):
    return password == "admin123"

def brute_force(username, wordlist):
    print(f"[+] Brute-forcing {username}...")
    for password in wordlist:
        if dummy_login(username, password):
            print(f"[✓] Password found: {password}")
            return True
    print("[-] Password not found")
    return False

if __name__ == "__main__":
    username = input("Enter username: ")
    passwords = ["123456", "admin", "admin123", "root", "letmein"]
    brute_force(username, passwords)
