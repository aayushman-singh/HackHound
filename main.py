from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import fuzzer  # Import your fuzzing logic here

app = FastAPI()

# Define the model for the input payload
class FuzzingOptions(BaseModel):
    url: str
    directories: bool = True
    vhosts: bool = True
    api_endpoints: bool = False
    parameters: bool = False

# Store fuzzing results temporarily (in-memory or you could use a database)
results = []

@app.post("/start-fuzzing")
async def start_fuzzing(options: FuzzingOptions, background_tasks: BackgroundTasks):
    # Add the fuzzing task to be executed in the background
    background_tasks.add_task(fuzzer.start, options.dict())  # Adjust the call to match your fuzzer function
    return {"message": "Fuzzing started"}

@app.get("/get-results")
async def get_results():
    return {"results": results}
