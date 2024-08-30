import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


USERS_FILE_PATH = get_path(filename="users.csv")
UPDATE_USER_FILE_PATH = get_path(filename="user_for_update.csv")
ORDER_FILE_PATH = get_path(filename="orders.csv")
