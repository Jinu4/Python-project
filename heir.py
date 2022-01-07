class Computer:
    def _init_(self, li, x):
        self.li = li
        self.x = x

    def getspecs(self):
        print("Available processors are:\n")
        self.li = ["AMD Ryzen 9", "Intel i9", "Intel i7", "Intel i5", "AMD Ryzen 7"]
        print(self.li)
        self.x = int(input("Enter the processor you want : "))

    def displayspecs(self):
        print(self.li[self.x])


class Desktop(Computer):
    def components(self):
        print("Components you get when you buy desktop")
        nm = ["Keyboard", "Mouse", "Monitor"]
        print(nm)


class Laptop(Computer):
    def components(self):
        print("Components you get when you buy Laptop")
        mn = ["Mouse", "Anti-Virus", "Headphone"]
        print(mn)


ob1 = Desktop()
ob1.getspecs()
ob1.displayspecs()
ob1.components()
ob2 = Laptop()
ob2.components()
