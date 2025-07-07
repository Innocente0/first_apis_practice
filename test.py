from fastapi import FastAPI
import uvicorn 

app = FastAPI()

@app.get('/marvin')
def test():
    a = 3
    b = 4
    c = a + b
    return c
@app.get('/')
def show():
    return print("Hello World")

uvicorn.run(app, host = '127.0.0.1', port = 4000)



