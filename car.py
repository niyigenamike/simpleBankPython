class car:
    def __init__(self,model,year,color,for_sale):
        self.model = model,
        self.year = year,
        self.color = color,
        self.for_sale = for_sale,
    def drive(self):
        print(f"you can drive the {self.color} car{self.model}")
    def stop(self):
        print("stop the car")
    def descibe(self):
        print(f"{self.year} {self.color} {self.model}")