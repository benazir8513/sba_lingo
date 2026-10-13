from pydantic import BaseModel


class GetWordResponse(BaseModel):
    german: str
    english: str
