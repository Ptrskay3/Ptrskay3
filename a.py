from dataclasses import dataclass
from enum import Enum, auto
from typing import Tuple, List

class ExperienceLevel(Enum):
    BASIC = auto()
    INTERMEDIATE = auto()
    EXPERIENCED = auto()
    ADVANCED = auto()
    EXPERT = auto()

@dataclass
class Library:
    name: str
    experience_level: ExperienceLevel
    contributed: bool = False

    def __str__(self):
        return f"{self.name}: {self.experience_level.name} {'(contributed)' if self.contributed else ''}"


@dataclass
class Info:
    libs: List[Library]
    lang: Tuple[str, ExperienceLevel] = "Python", ExperienceLevel.ADVANCED

    def build_skill_str(self) -> str:
        return f"{self.lang[0]}: {self.lang[1].name}\n" + "\n".join(map(str, [lib for lib in self.libs]))

if __name__ == "__main__":
    info = Info([
        Library("Numpy", ExperienceLevel.ADVANCED),
        Library("Scipy", ExperienceLevel.EXPERIENCED),
        Library("Matplotlib", ExperienceLevel.EXPERIENCED, contributed=True),
        Library("Pandas", ExperienceLevel.INTERMEDIATE),
        Library("Django", ExperienceLevel.BASIC),
        Library("Scikit-learn", ExperienceLevel.EXPERIENCED),
        Library("Tensorflow", ExperienceLevel.BASIC),
        Library("PyQt5", ExperienceLevel.INTERMEDIATE),
        Library("OpenCV", ExperienceLevel.BASIC)
    ])
    print(info.build_skill_str())
