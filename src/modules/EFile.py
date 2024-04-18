from enum import Enum
from pathlib import Path


class EFile(Enum):
    USERS = Path('login.txt')
    PROJECTS = Path('src/files/projects')
    TASKS = Path('src/files/tasks')
    LOGS = Path('src/files/logs')

