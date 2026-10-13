from random import random

from fastapi import APIRouter

from resources.wortschatz import VOCABS
from routers.responses import GetWordResponse

vocab_router = APIRouter()

def random_range(end: int) -> int:
    return int(random() * end)

@vocab_router.get("/vocab")
async def get_word():
    tuple_index = random_range(len(VOCABS))
    return GetWordResponse(german=VOCABS[tuple_index][0], english=VOCABS[tuple_index][1])