
class Operations:
    def Add(self, x, y):
        print(x + y)

op = Operations()
op.Add(3, 9)
op.Add(3.3, 9.8)
op.Add("yo", "bro")


class Parent:
    def Display(self):
        print("This is the parent class")

class Child(Parent):
    def Display(self):
        super().Display()
        print("This is the child class")

obj1 = Child()
obj1.Display()

