import dns.resolver
import requests

def load_wordlist(filepath):
    """Load the wordlist from a file."""
    try:
        with open(filepath, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Wordlist file not found: {filepath}")
        return []

# Subdomain fuzzing function using HTTP requests
import requests

def run_subdomain_fuzzing(domain, wordlist_path):
    """Fuzz subdomains for a given domain using a wordlist."""
    found_subdomains = []
    
    try:
        # Open the wordlist file and read each line (assuming the wordlist file has subdomains)
        with open(wordlist_path, 'r') as file:
            subdomains = file.read().splitlines()

        for subdomain in subdomains:
            # Create the full subdomain URL (e.g., sub.example.com)
            full_url = f"http://{subdomain}.{domain}"

            try:
                # Make a request to the subdomain
                response = requests.get(full_url, timeout=5)
                if response.status_code == 200:
                    print(f"[+] Found subdomain: {full_url}")
                    found_subdomains.append(full_url)
                else:
                    print(f"[-] Not found: {full_url}")
            except requests.exceptions.RequestException as e:
                print(f"[!] Error with {full_url}: {e}")

    except FileNotFoundError:
        print(f"Wordlist file {wordlist_path} not found.")
    
    return found_subdomains


# Subdomain enumeration using DNS resolution
def subdomain_enum(domain, wordlist):
    """Enumerate subdomains for a given domain using a wordlist."""
    found_subdomains = []
    resolver = dns.resolver.Resolver()

    for word in wordlist:
        subdomain = f"{word}.{domain}"
        try:
            # Try to resolve the subdomain to check if it exists
            answers = resolver.resolve(subdomain, 'A')
            print(f"[+] Found: {subdomain}")
            found_subdomains.append(subdomain)
        except dns.resolver.NoAnswer:
            print(f"[-] No answer: {subdomain}")
        except dns.resolver.NXDOMAIN:
            print(f"[-] NXDOMAIN: {subdomain} does not exist")
        except dns.exception.Timeout:
            print(f"[-] Timeout: Could not resolve {subdomain}")
        except Exception as e:
            print(f"[!] Error resolving {subdomain}: {e}")
    
    return found_subdomains

