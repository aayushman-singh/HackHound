import requests

def fuzz_virtual_hosts(domain, vhost_wordlist):
    found_vhosts = []

    try:
        # Open the vhost wordlist file and read subdomains
        with open(vhost_wordlist, 'r') as file:
            subdomains = file.read().splitlines()

        for subdomain in subdomains:
            # Create the Host header with the subdomain
            headers = {'Host': f'{subdomain}.{domain}'}
            
            # Make the request
            response = requests.get(f"http://{domain}", headers=headers)

            # Check if the response status is 200 (OK)
            if response.status_code == 200:
                found_vhosts.append(f"{subdomain}.{domain}")
                print(f"Found VHost: {subdomain}.{domain}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
    except FileNotFoundError:
        print(f"Wordlist file not found: {vhost_wordlist}")
    
    return found_vhosts
