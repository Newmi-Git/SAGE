import fastapi as FastAPI
import pydantic as BaseModel

app = FastAPI()

class Message(BaseModel):
    text :str
    
@app.post("/chat")
def chat(msg: Message):
    repy = get_ollama_response(msg.text)
    return {"reply": reply}
    
