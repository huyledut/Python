class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.salary = None  # Khởi tạo thuộc tính salary là None

    def set_salary(self, salary):
        self.salary = salary

    def get_info(self):
        return f"Tên: {self.name}, Tuổi: {self.age}, Lương: {self.salary}"


# Tạo một đối tượng person1 với thuộc tính name và age
person1 = Person("Huy", 30)

# Gọi phương thức set_salary để thiết lập thuộc tính salary cho đối tượng person1
person1.set_salary(1000)

# In thông tin đối tượng person1 bao gồm các thuộc tính name, age và salary
print(person1.get_info())  # Kết quả: Tên: Huy, Tuổi: 30, Lương: 1000
