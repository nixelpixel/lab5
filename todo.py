import json


class ToDoList:
    def __init__(self):
        """Инициализация списка задач."""
        self.tasks = []

    def load_tasks(self, file_path):
        """Загружает задачи из JSON-файла."""
        try:
            with open(file_path, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            print("Файл не найден. Создайте новый список задач.")
        except json.JSONDecodeError:
            print("Ошибка при загрузке задач. Файл может быть поврежден.")

    def save_tasks(self, file_path):
        """Сохраняет задачи в JSON-файл."""
        with open(file_path, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        """Добавляет новую задачу в список."""
        self.tasks.append({"task": task, "completed": False})
        print(f"Задача '{task}' добавлена.")

    def complete_task(self, index):
        """Помечает задачу как выполненную."""
        try:
            self.tasks[index]["completed"] = True
            print(f"Задача '{self.tasks[index]['task']}' Выполнена.")
        except IndexError:
            print("Задача не найдена.")

    def remove_task(self, index):
        """Удаляет задачу из списка."""
        try:
            removed_task = self.tasks.pop(index)
            print(f"Задача '{removed_task['task']}' удалена.")
        except IndexError:
            print("Задача не найдена.")

    def display_tasks(self):
        """Отображает все задачи в списке."""
        if not self.tasks:
            print("Список задач пуст.")
            return

        for index, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{index + 1}. [{status}] {task['task']}")


def main():
    todo_list = ToDoList()
    todo_list.load_tasks('tasks.json')

    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Завершить задачу")
        print("3. Удалить задачу")
        print("4. Показать задачи")
        print("5. Сохранить задачи")
        print("6. Выход")

        choice = input("Выберите опцию: ")

        if choice == "1":
            task = input("Введите задачу: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Введите номер задачи для завершения: ")) - 1
            todo_list.complete_task(index)
        elif choice == "3":
            index = int(input("Введите номер задачи для удаления: ")) - 1
            todo_list.remove_task(index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            todo_list.save_tasks('tasks.json')
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()


