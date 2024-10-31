from fastapi import FastAPI

app = FastAPI()

@app.get('/weclome')
def welcome():
    return{
        'message' : 'Hello World'
    }