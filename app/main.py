from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.apis import run_api_fuzzing, fuzz_api_headers
from app.directories import run_directory_fuzzing
from app.subdomains import run_subdomain_fuzzing
from app.vhosts import fuzz_virtual_hosts

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class FuzzRequest(BaseModel):
    url: str
    domain: str = None
    actions: dict

@app.post("/fuzz")
async def fuzz(data: FuzzRequest):
    url = data.url
    domain = data.domain
    actions = data.actions
    results = {}
    vulnerabilities = []

    if actions.get("fuzz_directory"):
        dir_wordlist = "./config/wordlists/dir_wordlist.txt"
        found_dirs = run_directory_fuzzing(url, dir_wordlist)
        results["directories"] = found_dirs
        vulnerabilities.extend(found_dirs)  # Add directory vulnerabilities

    if actions.get("fuzz_subdomain") and domain:
        sub_wordlist = "./config/wordlists/subdomains.txt"
        found_subdomains = run_subdomain_fuzzing(domain, sub_wordlist)
        results["subdomains"] = found_subdomains
        vulnerabilities.extend(found_subdomains)  # Add subdomain vulnerabilities

    if actions.get("fuzz_vhost") and domain:
        vhost_wordlist = "./config/wordlists/vhosts.txt"
        found_vhosts = fuzz_virtual_hosts(domain, vhost_wordlist)
        results["virtual_hosts"] = found_vhosts
        vulnerabilities.extend(found_vhosts)  # Add virtual host vulnerabilities

    if actions.get("fuzz_api"):
        params = {'id': '1'}
        api_wordlist = "./config/wordlists/api_endpoints.txt"
        payloads = ["' OR '1'='1", '<script>alert(1)</script>', '../../../../../etc/passwd']
        api_vulns = run_api_fuzzing(url,api_wordlist, payloads)
        vulnerabilities.extend(api_vulns)  # Add API parameter vulnerabilities

        headers = {'Authorization': 'Bearer token123'}
        header_vulns = fuzz_api_headers(url, headers, ['invalidToken', 'maliciousToken'])
        vulnerabilities.extend(header_vulns)  # Add header vulnerabilities

    results["vulnerabilities"] = vulnerabilities  # Send all vulnerabilities

    return {"status": "Fuzzing completed", "results": results}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
