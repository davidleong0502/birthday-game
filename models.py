from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class Choice:
    label: str
    next_id: str
    gives: Optional[Dict[str, int]] = None
    requires: Optional[Dict[str, int]] = None
    message: Optional[str] = None


@dataclass
class Scene:
    id: str
    title: str
    text: str
    a: Choice
    b: Choice