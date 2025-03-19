import logging
from actions_repository import ActionsRepository


class ActionsManagement:

    def add_action(user_id, type, cooperation, against):
        """Adds a new action to the database."""
        
        action_id = ActionsRepository(
            user_id, type, cooperation, against
        ).set_actions_data()

    def get_actions(user_id):
        """Gets all actions from the database."""
        action_id = ActionsRepository(user_id).get_user_actions_data()
        for action in action_id.all():
            logging.info(
                f"{action.id}, {action.user_id}, {action.type}, {action.cooperation}, {action.against}"
            )

    def delete_action(action_id):
        """Deletes an action from the database."""
        ActionsRepository(action_id).delete_all_user_actions()


if __name__ == "__main__":
    ActionsManagement.get_actions("1")

