from fastapi import FastAPI, Request
import uvicorn
import sys



port = 8000
print_or_save = input("If you want to print select 1, if you want to save select 2, if you want to print and save select 3")
if print_or_save == "1":
    print_or_save = "print"
elif print_or_save == "2":
    print_or_save = "save"
elif print_or_save == "3":
    print_or_save = "both"
else: 
    print("Please select a valid option")
    sys.exit()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def root_post(request: Request):
    data = await request.json()
    serialised_data = data["payload"]
    format = data["payload_format"]
    print(serialised_data)
    print(format)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port, loop="asyncio")