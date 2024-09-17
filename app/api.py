
import requests

def fuzz_api_endpoints(url, wordlist):
    with open(wordlist, 'r') as words:
        for word in words:
            endpoint = word.strip()
            test_url = f"{url}/{endpoint}"
            try:
                response = requests.get(test_url)
                if response.status_code == 200:
                    print(f"API Endpoint Found: {test_url}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")

def fuzz_api_vulnerabilities(url, params, payloads):
    for param, value in params.items():
        for payload in payloads:
            params[param] = payload
            try:
                response = requests.get(url, params=params)
                if "error" in response.text or response.status_code == 500:
                    print(f"Potential Vulnerability Found at {url} with {param} = {payload}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")

def fuzz_api_post(url, data, payloads):
    for key, value in data.items():
        for payload in payloads:
            data[key] = payload
            try:
                response = requests.post(url, data=data)
                if response.status_code == 200 and "error" in response.text:
                    print(f"Potential Vulnerability Found at {url} with {key} = {payload}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")

def fuzz_api_headers(url, headers, payloads):
    for key, value in headers.items():
        for payload in payloads:
            headers[key] = payload
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    print(f"Potential Vulnerability with Header: {key} = {payload}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")

    url = "http://example.com/api/v1"
    wordlist = "api_endpoints.txt"
    fuzz_api_endpoints(url, wordlist)

    params = {'id': '1'}
    payloads = ["' OR '1'='1", '<script>alert(1)</script>', '../../../../../etc/passwd']
    fuzz_api_vulnerabilities(url, params, payloads)
    
    data = {'username': 'admin', 'password': 'password123'}
    fuzz_api_post(url + '/login', data, payloads)

    headers = {'Authorization': 'Bearer token123'}
    fuzz_api_headers(url, headers, ['invalidToken', 'maliciousToken'])

def run_api_fuzzing(url, api_wordlist):
    # API Endpoint fuzzing
    print(f"\nStarting API endpoint fuzzing on {url}")
    fuzz_api_endpoints(url, api_wordlist)

    # Example parameter fuzzing
    params = {'id': '1'}
    payloads = ["' OR '1'='1", '<script>alert(1)</script>', '../../../../../etc/passwd']
    print(f"\nFuzzing API parameters on {url}")
    fuzz_api_vulnerabilities(url, params, payloads)

    # Example POST request fuzzing
    data = {'username': 'admin', 'password': 'password123'}
    print(f"\nFuzzing API POST requests on {url}/login")
    fuzz_api_post(url + '/login', data, payloads)

    # Example header fuzzing
    headers = {'Authorization': 'Bearer token123'}
    print(f"\nFuzzing API headers on {url}")
    fuzz_api_headers(url, headers, ['invalidToken', 'maliciousToken'])

    print("\nAPI fuzzing complete.")

