import logging
from actions_repository import ActionsRepository


class ActionsManagement:
    def __init__(self, user_id, type="", cooperation="", against=""):
        self.user_id = user_id
        self.type = type
        self.cooperation = cooperation
        self.against = against

    def add_action(self):
        action_id = ActionsRepository(
            self.user_id, self.type, self.cooperation, self.against
        ).set_actions_data()

    def get_actions(self):
        action_id = ActionsRepository(self.user_id).get_user_actions_data()
        for action in action_id.all():
            logging.info(f"{action.id}, {action.user_id}, {action.type}, {action.cooperation}, {action.against}")

    def delete_action(self, action_id):
        ActionsRepository(action_id).delete_all_user_actions()


if __name__ == "__main__":
    ActionsManagement("1").get_actions()
    #ActionsManagement("1", "attack", "3", "2").add_action()
     #ActionsManagement("1", "get_wood", "", "").add_action()
    # ActionsManagement("2", "defense", "", "4").add_action()
     #ActionsManagement("1", "build", "2", "").add_action()
