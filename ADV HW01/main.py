import application.salary as salary
import application.db.people as people
from datetime import datetime
import matplotlib.pyplot as graph


def main_fun():
    print(datetime.now())
    # Данные для графика
    x = [1, 2, 3]
    y = [2, 4, 6]

    # Построение графика
    graph.plot(x, y, marker='o')
    graph.title('Простой линейный график')
    graph.xlabel('Ось X')
    graph.ylabel('Ось Y')
    graph.grid(True)
    graph.show()


if __name__ == '__main__':
    salary.salary_fun()
    people.people_fun()
    main_fun()


