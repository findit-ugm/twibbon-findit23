from pydantic import BaseModel


class Img(BaseModel):
    category: str
    img_url: list = []