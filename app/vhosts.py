import requests

def fuzz_virtual_hosts(url, subdomains):
    for subdomain in subdomains:
        headers = {'Host': f'{subdomain}.example.com'}
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print(f"Found VHost: {subdomain}.example.com")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")