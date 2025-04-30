from typing import Annotated
from fastapi import Depends 
from .config.db_config import get_session , Session
from .services.service import Service


DBSESSION = Annotated[Session, Depends(get_session)]

def get_service(db: DBSESSION) -> Service:
    return Service(db=db)



SERVICE = Annotated[Service, Depends(get_service)]