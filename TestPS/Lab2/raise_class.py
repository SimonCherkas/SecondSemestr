# raise_class.py
class Name:
    def __init__(self, name, hobby) -> None:
        # Дозволені імена – додаємо також власне ім'я, наприклад "ВашеІм'я"
        allowed_names = ["Богдан", "Анонім", "ВашеІм'я"]
        if name not in allowed_names:
            raise ValueError("Дозволені імена: Богдан, Анонім, ВашеІм'я")
        if not hobby:
            raise ValueError("Хоббі не може бути пустим!")
        self.name = name
        self.hobby = hobby

if __name__ == '__main__':
    try:
        # Спроба створити об'єкт з невірним ім'ям та порожнім хоббі:
        a = Name("Бодько", "")
    except ValueError as e:
        print("Помилка:", e)
    
    try:
        # Спроба створити об'єкт з дозволеним ім'ям та коректним хоббі:
        b = Name("ВашеІм'я", "Малювання")
        print(f"Ім'я: {b.name}, Хоббі: {b.hobby}")
    except ValueError as e:
        print("Помилка:", e)
