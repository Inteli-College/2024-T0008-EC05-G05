# O objetivo desse código é funcionar como a api da tela de estoque do sistema. 
# A ideia é que a tela de supplies faça requisições para essa api para obter informações sobre os produtos e para adicionar novos produtos ao estoque. 


from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from tinydb import TinyDB, Query
from typing import List


# Modelo de dados para realizar o post no DB 
class Post(BaseModel):
    nome_kit: str
    id_kit: int
    item_1: List[str] 




# Initialize FastAPI app
app = FastAPI()

# Initialize TinyDB database
db = TinyDB('kits.json')
posts_table = db.table('kits')

# Liberando o CORS para fazer requisições locais
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update this to your frontend URL during development
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/")
def hello():
    return {"Hello World"}

# Endpoint to create a new post
@app.post("/posts/")
def create_post(post: Post):
    post_dict = post.dict()
    post_id = posts_table.insert(post_dict)
    return {"post_id": post_id, **post_dict}

# Endpoint to get a specific post by ID
@app.get("/posts/{post_id}")
def read_post(post_id: int):
    post = posts_table.get(doc_id=post_id)
    if post:
        return post
    else:
        raise HTTPException(status_code=404, detail="Post not found")

# Endpoint to get all posts
@app.get("/posts/")
def read_all_posts():
    return posts_table.all()
