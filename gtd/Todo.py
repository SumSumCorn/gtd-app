from typing import List
from pydantic import BaseModel, Field


class Todo(BaseModel):
    description: str = Field(default="")


class ClassifiedTodo(Todo):
    state: str = Field(
        description="destory, someday, reference, now, delegate, calender, project"
    )
    plan: List[str] = Field(default=[])

    def make_plan(self, state: str):
        pass
        # match state:
        #     case 'destory':
        #     case 'someday':
        #     case 'reference':
        #     case 'now':
        #     case 'delegate':
        #     case 'calender':
        #     case 'project':
        #     case '_':
        #         # cancel
        #         print('revert to unclassified')


class UnclassifiedTodo(Todo):
    def calssify(self, state: str) -> ClassifiedTodo:
        return ClassifiedTodo(description=self.description, state=state)


class ProjectTodo(ClassifiedTodo):
    pass
