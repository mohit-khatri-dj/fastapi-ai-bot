from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from chatbot import chain, context

app = FastAPI()

origins = [
    "http://localhost:5173",
    "https://madhuban-khatri.onrender.com/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request body schema
class UserQuery(BaseModel):
    user_query: str


@app.post("/user_query")
def create_user(user_query: UserQuery):
    result = chain.invoke({
            "context": context,
            "question": user_query.user_query
        })
    return {
        "message": "Success",
        "reply": result.content
    }
