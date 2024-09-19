import httpx

def load_wordlist(filepath):
    """Load the wordlist from a file."""
    try:
        with open(filepath, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Wordlist file not found: {filepath}")
        return []

def fuzz_directories(url, wordlist):
    """Fuzz directories for a given URL using a wordlist."""
    found_dirs = []
    if url.endswith('/'):
        url = url.rstrip('/')  # Remove trailing slash

    for word in wordlist:
        target_url = f"{url}/{word}"
        try:
            response = httpx.get(target_url, timeout=5)  # Add a timeout for each request
            if response.status_code == 200:
                print(f"[+] Found: {target_url}")
                found_dirs.append(target_url)
            else:
                print(f"[-] Not found: {target_url}")
        except httpx.RequestError as e:
            print(f"[!] Error with {target_url}: {e}")
    return found_dirs


# Directory fuzzing function with a list of words
def run_directory_fuzzing(url, wordlist_file):
    """Run directory fuzzing on the provided URL."""
    # Load the wordlist from the provided file
    wordlist = load_wordlist(wordlist_file)
    if not wordlist:
        print("No wordlist loaded, exiting.")
        return []
    
    # Fuzz directories
    return fuzz_directories(url, wordlist)

