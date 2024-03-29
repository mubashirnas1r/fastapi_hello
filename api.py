from fastapi import FastAPI,Query

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the root endpoint
@app.get("/racingapi")
async def read_root(new_user:str=Query(...):
    if new_user == "cotu_update_1":
        return {"allow": True}
    else:
        return {"allow": False}


@app.post("/save_emails")
async def eduskill_emails(email:str=Query(...)):
    import requests

    api_url = 'http://mubash1r.pythonanywhere.com/save_email'  # Replace with your actual URL
    
    data = {'email': email}
    
    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        print("Email saved successfully.")
        return {"message":"Email saved successfull"}
    else:
        print("Error:", response.json())
        return {"Error:": response.json()}

