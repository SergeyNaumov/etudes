from dataclasses import dataclass
from typing import Tuple
from enum import Enum

class Blog(str, Enum):
    header = 'Новый блог'
    