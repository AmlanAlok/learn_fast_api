from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
'''The first bath operation that matches is the one which runs'''

saved = [{'title':'t1', 'content': 'c1', 'id':1}, {'title':'t2', 'content': 'c2', 'id':2}]


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
async def root():
    return {"message": "Hello World"}   # Automatically convert this Dictionary to JSON


# @app.post('/createposts')
# def create_posts(payload: dict = Body(...)):
#     return {'new_post': f"title = {payload['title']}, content = {payload['content']}"}

@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = 3
    saved.append(post)
    return {'data': post_dict}


@app.get('/posts')
def get_posts():
    return {'data': saved}


@app.get('/posts/{id}')
def get_post(id: int, response: Response):

    for x in saved:
        if x['id'] == id:
            return {'post_detail': x}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post with ID = {id} was not found")


@app.delete('/posts/{id}')
def delete_post(id: int, response: Response):

    delete_idx = None
    print(saved)

    for i, p in enumerate(saved):
        if p['id'] == id:
            delete_idx = i

    if delete_idx is None:
        print(delete_idx)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with ID = {id} was not found")

    del saved[delete_idx]
    print(saved)
    return {'message': f"Post with ID = {id} is deleted"}

