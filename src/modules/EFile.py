from enum import Enum
from pathlib import Path


class EFile(Enum):
    FILES = Path('src/files')
    PROJECTS = Path('src/files/projects')
    TASKS = Path('src/files/tasks')
    LOGS = Path('src/files/logs')
    USERS = Path('src/files/login.txt')

