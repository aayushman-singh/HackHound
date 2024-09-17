from fastapi import FastAPI
from pydantic import BaseModel
from app.api import run_directory_fuzzing, run_subdomain_fuzzing, run_api_fuzzing, fuzz_virtual_hosts

app = FastAPI()

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

    # Directory fuzzing
    if actions.get("fuzz_directory"):
        dir_wordlist = "config/wordlists/dir_wordlist.txt"
        found_dirs = run_directory_fuzzing(url, dir_wordlist)
        results["directories"] = found_dirs

    # Subdomain fuzzing
    if actions.get("fuzz_subdomain") and domain:
        sub_wordlist = "config/wordlists/subdomains.txt"
        found_subdomains = run_subdomain_fuzzing(domain, sub_wordlist)
        results["subdomains"] = found_subdomains

    # API fuzzing
    if actions.get("fuzz_api"):
        api_wordlist = "config/wordlists/api_endpoints.txt"
        found_api_endpoints = run_api_fuzzing(url, api_wordlist)
        results["api_endpoints"] = found_api_endpoints

    # Virtual Host fuzzing
    if actions.get("fuzz_vhost"):
        vhost_wordlist = "config/wordlists/vhosts.txt"
        found_vhosts = fuzz_virtual_hosts(url, vhost_wordlist)
        results["vhosts"] = found_vhosts

    return {"status": "Fuzzing completed", "results": results}
