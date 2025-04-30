from ..controllers.controller import Controller


from fastapi import APIRouter

router = APIRouter(prefix="/api")

router.add_api_route("/register_member", Controller.register_member, methods=["POST"])
router.add_api_route("/get/registered_members", Controller.get_registered_members, methods=["GET"])
router.add_api_route("/upload/images", Controller.upload_images, methods=["POST"])
# router.add_api_route("/get/member/images/{member_id}", Controller.get_member_images, methods=["GET"])
router.add_api_route("/get/all/images", Controller.get_all_images, methods=["GET"])
router.add_api_route("/login/admin", Controller.login_admin, methods=["POST"])
router.add_api_route("/send/email/reminder", Controller.send_email_reminder, methods=["POST"])
router.add_api_route("/add/event", Controller.add_event, methods=["POST"])
router.add_api_route("/get/all/events", Controller.get_all_events, methods=["GET"])
router.add_api_route("/update/event/{event_id}", Controller.updated_event, methods=["PUT"])