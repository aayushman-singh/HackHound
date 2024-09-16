from fuzzer.directories import run_directory_fuzzing

if __name__ == "__main__":
    url = "http://example.com"  # Target website
    wordlist_path = "config/wordlists/dir_wordlist.txt"  # Path to wordlist
    
    print(f"Starting directory fuzzing on {url}")
    found_dirs = run_directory_fuzzing(url, wordlist_path)
    
    print("\nFuzzing complete. Found directories:")
    for directory in found_dirs:
        print(directory)