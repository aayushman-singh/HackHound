import httpx

def load_wordlist(filepath):
    """Load the wordlist from a file."""
    with open(filepath, 'r') as file:
        return [line.strip() for line in file if line.strip()]


def fuzz_directories(url, wordlist):
    found_dirs = []
    for word in wordlist:
        target_url = f"{url}/{word}"
        try:
            response = httpx.get(target_url, timeout=5)  # Add a timeout
            if response.status_code == 200:
                print(f"[+] Found: {target_url}")
                found_dirs.append(target_url)
            else:
                print(f"[-] Not found: {target_url}")
        except httpx.RequestError as e:
            print(f"[!] Error with {target_url}: {e}")
    return found_dirs

def run_directory_fuzzing(url, wordlist_path):
    """Load wordlist and run directory fuzzing."""
    wordlist = load_wordlist(wordlist_path)
    return fuzz_directories(url, wordlist)

