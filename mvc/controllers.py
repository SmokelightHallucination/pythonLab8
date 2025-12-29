from models import TaskModel
from views import TaskView


class TaskController:
    def __init__(self):
        self.model = TaskModel()
        self.view = TaskView()

    def run(self):
        while True:
            self.view.show_tasks(self.model.get_all_tasks())

            print("\n1. Добавить задачу")
            print("2. Переключить статус задачи")
            print("3. Выход")

            choice = self.view.get_user_input("Выберите действие: ")

            if choice == "1":
                title = self.view.get_user_input("Введите название задачи: ")
                self.model.add_task(title)
                self.view.show_message("Задача добавлена!")

            elif choice == "2":
                try:
                    index = int(self.view.get_user_input("Номер задачи: ")) - 1
                    self.model.toggle_task(index)
                    self.view.show_message("Статус обновлен!")
                except (ValueError, IndexError):
                    self.view.show_message("Неверный номер задачи!")

            elif choice == "3":
                self.view.show_message("До свидания!")
                break

            else:
                self.view.show_message("Неверный выбор!")
