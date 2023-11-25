import random

class Tank:
    def __init__(self, model, country,
                 gun_caliber, firing_rate,
                 weight, engine_power, speed):
        self.model = model
        self.country = country
        self.gun_caliber = gun_caliber
        self.firing_rate = firing_rate
        self.weight = weight
        self.engine_power = engine_power
        self.speed = speed

    def shoot(self):
        print(f"Танк {self.model} ({self.country}) стреляет из орудия калибра {self.gun_caliber} мм")

    def shots_per_minute(self, minutes):
        result = self.firing_rate * minutes
        return result

kv2 = Tank("КВ-2","СССР",
           152, 2.5,
           60.8, 640, 35)
kv2.shoot()
minutes = 5
print(f"Танк {kv2.model} выстрелил {kv2.shots_per_minute(minutes)} раз(а) за {minutes} минут")

class LightTank(Tank):
    def __init__(self, model, country,
                 gun_caliber, firing_rate,
                 weight, engine_power, speed,
                 view_range):
        self.model = model
        self.country = country
        self.gun_caliber = gun_caliber
        self.firing_rate = firing_rate
        self.weight = weight
        self.engine_power = engine_power
        self.speed = speed
        self.view_range = view_range

    def scout(self):
        chance = random.randint(1, 2)
        if chance == 1:
            print(f"Танк {self.model} ({self.country}) обнаружен и едет со скоростью {self.speed} км/ч")
        else:
            print(f"Танк {self.model} ({self.country}) разведывает территорию в диапазоне {self.view_range} м")

pz1c = LightTank("Pz.Kpfw. I Ausf. C", "Германия",
                 7.92, 165,
                 8, 150, 79,
                 320)
pz1c.shoot()
pz1c.scout()