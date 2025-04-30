from typing import Optional
from sqlmodel import Column, Field, SQLModel , JSON

class Member(SQLModel , table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    phone_number: str | None = None
    is_attending: bool = Field(default=False)
    total_person : int = Field(default=0)
    guest_names: list[str] = Field(
        sa_column=Column(JSON),
        default_factory=list,
    )
    request: Optional[str] = Field(
        default=None,
    )



class Images(SQLModel , table=True):
    id: int | None = Field(default=None, primary_key=True)
    name : str
    email : str
    image_path: str | None = Field(default=None)



class Events(SQLModel , table=True):
    id: int | None = Field(default=None, primary_key=True)
    event : str
    hotel_accommodation : str
    location : str
    url : str