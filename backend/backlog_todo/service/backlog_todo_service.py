from abc import ABC, abstractmethod

class BacklogTodoService(ABC):
    @abstractmethod
    def createBacklogTodo(self, backlogId, todo):
        pass