from typing import Annotated
from fastapi import File, Form, Request, UploadFile

from invite_managment_system.db.models import Events, Member
from ..dependencies import SERVICE


class Controller:
    @staticmethod
    def register_member(member:Member  , service : SERVICE):
        result = service.register_member(member)
        return result
    
    @staticmethod
    def get_registered_members(service : SERVICE):
        result = service.get_registered_members()
        return result
    @staticmethod
    async def upload_images(request:Request , files : Annotated[list[UploadFile] ,  File()] , service : SERVICE):
        result = await service.upload_images(request=request , files=files)
        return result
    # @staticmethod
    # def get_member_images(member_id : int , service : SERVICE):
    #     result = service.get_member_images(member_id)
    #     return result
    @staticmethod
    def get_all_images(service : SERVICE):
        result = service.get_all_images()
        return result
    @staticmethod
    def login_admin(username : Annotated[str , Form()] , password : Annotated[str , Form()] , service : SERVICE):
        result = service.login_admin(username, password)
        return result
    @staticmethod
    async def send_email_reminder(email : Annotated[str , Form()] , service : SERVICE):
        result = await service.send_email_reminder(email)
        return result
    @staticmethod
    def add_event(event : Events , service : SERVICE):
        result = service.add_event(event)
        return result
    @staticmethod
    def get_all_events(service : SERVICE):
        result = service.get_all_events()
        return result
    @staticmethod
    async def updated_event(event_id : int , request : Request , service : SERVICE):
        data : dict = await request.json()
        result = service.update_event(event_id, data)
        return result