# assert_input.py
a = input("Введіть число: ")
assert a.isdigit(), "Потрібно ввести число!"
print(f"Введене число: {a}")
