class TaskView:
    @staticmethod
    def show_tasks(tasks):
        if not tasks:
            print("Нет задач!")
            return

        print("\n--- Список задач ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("--------------------")

    @staticmethod
    def get_user_input(prompt: str) -> str:
        return input(prompt)

    @staticmethod
    def show_message(message: str):
        print(message)
