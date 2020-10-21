class Mobil:
    def __init__(self, max_speed = 0, miLeage = 0):
        self.ms = max_speed
        self.ml = miLeage

    def get_data(self):
        print(f"{self.ms}, {self.ml}")
        #print(self.ms, self.ml)

carX = Mobil(240,18)

carX.get_data()
