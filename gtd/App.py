from __future__ import annotations
from typing import List

from pydantic import BaseModel, Field
from Todo import UnclassifiedTodo, ClassifiedTodo, ProjectTodo


class App(BaseModel):
    todos: List[UnclassifiedTodo | ClassifiedTodo] = Field(default=[])
    # projectTodos: List[ProjectTodo] = Field(default=[])

    def classify(self, state: str) -> None:
        """여기서 todo를 분류합니다."""

        for i, todo in enumerate(self.todos):
            if isinstance(todo, UnclassifiedTodo) and state is not "canceled":
                classified_todo = todo.calssify(state)
                self.todos[i] = classified_todo

    def make_todo(self, description: str) -> None:
        """여기서 todo 만듭니다."""

        new_todo = UnclassifiedTodo(description=description)
        self.todos.append(new_todo)
        print("generate todo!")


def main():
    my_app = App()
    my_app.make_todo(input("어떤것을 하고싶나요? : "))
    # my_app.classify()


if __name__ == "__main__":
    main()
