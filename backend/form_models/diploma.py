from datetime import date
from pydantic import BaseModel


class Diploma(BaseModel):
    student: str
    course: str
    grade: int
    completed_date: date

    def as_template_dict(self) -> dict:
        data = self.dict()
        data["grade"] = f"{self.grade}%"
        data["completed_date"] = self.completed_date.strftime("%B %d, %Y")
        return data
