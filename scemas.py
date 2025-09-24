from pydantic import BaseModel

    
class BookResponse(BaseModel):
    id: int
    title: str
    url: str
    category: str
    price: str

    class Config:
        from_attributes = True
    
