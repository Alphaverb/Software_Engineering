class Tank:
    def __init__(self, model, country,
                 gun_caliber, firing_rate,
                 weight, engine_power, speed):
        self.__model = model
        self.country = country
        self.gun_caliber = gun_caliber
        self.firing_rate = firing_rate
        self.weight = weight
        self.engine_power = engine_power
        self.speed = speed

    def shoot(self):
        print(f"Танк {self.__model} ({self.country}) стреляет из орудия калибра {self.gun_caliber} мм")

    def shots_per_minute(self, minutes):
        result = self.firing_rate * minutes
        return result

kv2 = Tank("КВ-2","СССР",
           152, 2.5,
           60.8, 640, 35)
kv2.shoot()
minutes = 5
print(f"Танк {kv2.__model} выстрелил {kv2.shots_per_minute(minutes)} раз(а) за {minutes} минут")