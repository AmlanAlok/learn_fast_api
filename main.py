from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()
'''The first bath operation that matches is the one which runs'''


@app.get("/")
async def root():
    return {"message": "Hello World"}   # Automatically convert this Dictionary to JSON


@app.post('/createposts')
def create_posts(payload: dict = Body(...)):
    return {'new_post': f"title = {payload['title']}, content = {payload['content']}"}

