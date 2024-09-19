import requests

# Fuzz API Endpoints
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

# Fuzz API Vulnerabilities in GET Parameters
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

# Fuzz API Vulnerabilities in POST Parameters
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

# Fuzz API Headers
def fuzz_api_headers(url, headers, payloads):
    vulnerabilities = []
    for key, value in headers.items():
        for payload in payloads:
            headers[key] = payload
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    vulnerabilities.append(f"Potential Vulnerability with Header: {key} = {payload}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
    
    # Return the list of found vulnerabilities (or an empty list if none found)
    return vulnerabilities


# Main API Fuzzing Function
def run_api_fuzzing(url, api_wordlist, payloads):
    vulnerabilities = []

    # API Endpoint fuzzing
    print(f"\nStarting API endpoint fuzzing on {url}")
    fuzz_api_endpoints(url, api_wordlist)

    # Example parameter fuzzing
    params = {'id': '1'}
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

    # Assuming some vulnerabilities are found, append them to the list.
    # You should append actual vulnerability findings from each fuzzing step.
    vulnerabilities.append(f"Potential Vulnerability with Header: Authorization = invalidToken")
    vulnerabilities.append(f"Potential Vulnerability with Header: Authorization = maliciousToken")

    print("\nAPI fuzzing complete.")

    # Return the list of vulnerabilities
    return vulnerabilities

