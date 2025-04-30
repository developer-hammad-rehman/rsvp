from fastapi import File, Request, UploadFile
from typing import Optional

from ..config.env_config import ADMIN_EMAIL, ADMIN_PASSWORD
from ..db.models import Events, Images, Member
from sqlmodel import Session, select
from ..utils.emails import EmailUtil
from ..utils.jwt import JWTUtils


class Service:
    def __init__(self, db: Session) -> None:
        self.db = db

    def register_member(
        self, member : Member
    ) -> Member:
        self.db.add(member)
        self.db.commit()
        self.db.refresh(member)
        return member

    def get_registered_members(self):
        result = self.db.exec(select(Member)).all()
        return result

    async def upload_images(
        self, name:str , email:str, request: Request, files: list[UploadFile] = File(...)
    ):
        for file in files:
            file_location = f"storage/{file.filename}"
            with open(file_location, "wb+") as file_object:
                file_object.write(file.file.read())
            url = f"{request.base_url}images/{file.filename}"
            image = Images(name=name , email=email, image_path=url)
            self.db.add(image)
            self.db.commit()
            self.db.refresh(image)
        return {"status": "success"}

    # def get_member_images(self, member_id: int):
    #     result = self.db.exec(select(Images).where(Images.member_id == member_id)).all()
    #     return result

    def get_all_images(self):
        result = self.db.exec(select(Images)).all()
        return result

    def login_admin(self, username: str, password: str):
        if username == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            token = JWTUtils.create_jwt_token({"sub": username}, 3600)
            return {"status": "success", "token": token}
        else:
            return {"message": "Invalid credentials"}

    async def send_email_reminder(self, email: str):
        email_util = EmailUtil()
        await email_util.send_email(email)
        return {"status": "success"}
    def add_event(self , event : Events):
        self.db.add(event)
        self.db.commit()
        self.db.refresh(event)
        return event
    def get_all_events(self):
        result  = self.db.exec(select(Events)).all()
        return result
    def update_event(self, event_id: int , data: dict):
        stmt = select(Events).where(Events.id == event_id)
        result = self.db.exec(stmt).first()
        if result:
            if data.get("event"):
                result.event = data.get("event")
            if data.get("location"):
                result.location = data.get("location")
            if data.get("url"):
                result.url = data.get("url")
            self.db.commit()
            self.db.refresh(result)
            return result
        return {"message": "Event not found"}