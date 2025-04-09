# app.py
class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]
    
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        # Навмисна помилка: повертається type замість length
        return self.type

    @property
    def get_angles(self):
        if self.type in ["квадрат", "прямокутник"]:
            return 4
        if self.type == "трикутник":
            return 3

# Тест для pytest: перевіряємо, що для трикутника повертається 3 кути.
def test_app_triangle():
    """Test if we create a triangle figure with 3 angles."""
    fig = "трикутник"
    triangle = Figure(fig, 4)
    assert triangle.get_angles == 3, f"У {fig} має бути 3 кути!"

if __name__ == '__main__':
    # Демонстрація створення об'єкта
    f = Figure("квадрат", 5)
    print("Тип фігури:", f.get_figure_type)
    print("Довжина фігури (очікується довжина, але повертається тип):", f.get_figure_length)
    print("Кількість кутів:", f.get_angles)
