class Tank:
    def sound(self):
        pass

class HeavyTank(Tank):
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

    def sound(self):
        return "БрррРрррРррр"

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

    def sound(self):
        return "ТрТрТрТр"

pz1c = LightTank("Pz.Kpfw. I Ausf. C", "Германия",
                 7.92, 165,
                 8, 150, 79,
                 320)

kv2 = HeavyTank("КВ-2","СССР",
           152, 2.5,
           60.8, 640, 35)

print(f"Двигатель танка {pz1c.model} звучит как '{pz1c.sound()}'")
print(f"Двигатель танка {kv2.model} звучит как '{kv2.sound()}'")
