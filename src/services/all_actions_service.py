from src.services.actions_service import ActionsManagement
from src.services.building_service import BuildingService
from src.services.user_service import UserManagenment


class AllActionsService:
    def __init__(self, action_service):
        self.action_service = action_service

    def build(self, building_type, user_name):
        building_id = BuildingService().get_building(building_type)
        user_id = UserManagenment().get_user(user_name)

        type = "build"
        ActionsManagement().add_action(
            user_id=user_id,
            building_type=building_id,
            type=type,
            cooperation="",
            against="",
        )
        

    