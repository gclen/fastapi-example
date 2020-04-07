from typing import List
from pydantic import BaseModel

class TeamBase(BaseModel):
    team: str

class Team(TeamBase):
    id: int
    wins: int

    class Config:
        orm_mode = True