import dns.resolver

def load_wordlist(filepath):
    """Load the wordlist from a file."""
    with open(filepath, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def run_subdomain_fuzzing(domain, wordlist_path):
    """Load wordlist and run subdomain enumeration."""
    wordlist = load_wordlist(wordlist_path)
    return subdomain_enum(domain, wordlist)

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
            print(f"[-] NXDOMAIN: {subdomain}")
        except Exception as e:
            print(f"[!] Error resolving {subdomain}: {e}")
    
    return found_subdomains
