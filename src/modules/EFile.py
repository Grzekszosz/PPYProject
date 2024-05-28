from enum import Enum
from pathlib import Path


class EFile(Enum):
    FILES = Path('files')
    PROJECTS = Path('files/projects')
    TASKS = Path('files/tasks')
    LOGS = Path('files/logs')
    LOGIN = Path('files/login.txt')
    USERS = Path('files/users.txt')
