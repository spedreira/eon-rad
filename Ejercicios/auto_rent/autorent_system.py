from datetime import datetime, timedelta

DELTA = 1e-15
CLIO_LICENSE_PLATE = "AAA001"
FORD_KA_LICENSE_PLATE = "AAA002"
LOGAN_LICENSE_PLATE = "AAA003"
DUSTER_LICENSE_PLATE = "AAA004"
DUSTER_FULL_TANK = 70
KA_FULL_TANK = 40
CLIO_FULL_TANK = 45
KA_20_PERCENT_TANK = 8
KA_40_PERCENT_TANK = 16
KA_60_PERCENT_TANK = 24
KA_80_PERCENT_TANK = 32
LOGAN_FULL_TANK = 50
MAX_KM_ALLOWED_PER_DAY = 400
TRAVELLED_300_KMS = 300
LOGAN_COST_PER_EXCEEDED_KM = 12
LOGAN_RENT_COST = 500
FORD_KA_RENT_COST = 430
DUSTER_RENT_COST = 700
CLIO_RENT_COST = 400
CLIO_RENT_COST_PER_EXCEEDED_KM = 10
CLIO_80_PERCENT_TANK = 36
FLUENCE_LICENSE_PLATE = "AAA005" #####modifique el ultimo num de 3 a 5####
FLUENCE_RENT_COST = 600
FLUENCE_RENT_COST_PER_EXCEEDED_KM = 18
FLUENCE_80_PERCENT_TANK = 48

INSUFFICIENT_TANK_LVL_PENALTY = 400
LOW_TANK_LVL_PENALTY = 300
MEDIUM_TANK_LVL_PENALTY = 200
HIGH_TANK_LVL_PENALTY = 100
FORD_KA_RENT_COST_PER_EXCEEDED_KM = 10
DUSTER_RENT_COST_PER_EXCEEDED_KM = 15
FLUENCE_FULL_TANK = 60


class AutorentSystem:
    def __init__ (self, catalogo_auto):
        self.catalogo_auto = catalogo_auto

    def fuel_penalty(self, car, return_tank_level):
        if (return_tank_level == car.tank_capacity):
            return 0
        elif (return_tank_level < car.tank_capacity*0.25):
            return INSUFFICIENT_TANK_LVL_PENALTY 
        elif (car.tank_capacity*0.25 <= return_tank_level < car.tank_capacity*0.50): 
            return LOW_TANK_LVL_PENALTY
        elif (car.tank_capacity*0.50 <= return_tank_level < car.tank_capacity*0.75):
            return MEDIUM_TANK_LVL_PENALTY
        elif (return_tank_level >= car.tank_capacity*0.75):
            return HIGH_TANK_LVL_PENALTY

    def km_penalty(self, rent_days, travelled_km, car):
        if (rent_days*MAX_KM_ALLOWED_PER_DAY < travelled_km):
            return (travelled_km - rent_days*MAX_KM_ALLOWED_PER_DAY) * car.exceeded_km_cost
        else:
            return 0

    def day_penalty(self, pickup_date, rent_days, return_date, car):
        sat = 5
        sun = 6
        special_days = 0
        days = 0
        date = pickup_date
        while (date < return_date):
            if (date.weekday() == sat or date.weekday() == sun):
                special_days += 1
            date = date + timedelta (days=1)
            days += 1
        return days*car.daily_rent_cost + special_days*car.daily_rent_cost*0.15

    def cost_for(self, license_plate, pickup_date, rent_days, return_date, return_tank_level, travelled_km):
        car = self.catalogo_auto[license_plate]      
        return self.fuel_penalty(car, return_tank_level) + self.km_penalty(rent_days, travelled_km, car) + self.day_penalty(pickup_date, rent_days, return_date, car)
        

class DasAuto:
    def __init__ (self, model, license_plate, daily_rent_cost, exceeded_km_cost, tank_capacity):
        self.daily_rent_cost = daily_rent_cost
        self.exceeded_km_cost = exceeded_km_cost
        self.tank_capacity = tank_capacity


'''
ferrari = DasAuto('Enzo', 'Rojo', 'AAA123', 500, 30, 50)
print(ferrari.daily_rent_cost)
'''


def create_system_using_data_from_the_exercise_assignment():
    catalogo = {CLIO_LICENSE_PLATE:DasAuto('Renault Clio', CLIO_LICENSE_PLATE, CLIO_RENT_COST, CLIO_RENT_COST_PER_EXCEEDED_KM, CLIO_FULL_TANK), 
                     FORD_KA_LICENSE_PLATE:DasAuto('Ford Ka', FORD_KA_LICENSE_PLATE, FORD_KA_RENT_COST, FORD_KA_RENT_COST_PER_EXCEEDED_KM, KA_FULL_TANK),
                     LOGAN_LICENSE_PLATE:DasAuto('Renault Logan', LOGAN_LICENSE_PLATE, LOGAN_RENT_COST, LOGAN_COST_PER_EXCEEDED_KM, LOGAN_FULL_TANK),
                     DUSTER_LICENSE_PLATE:DasAuto('Renault Duster', DUSTER_LICENSE_PLATE, DUSTER_RENT_COST, DUSTER_RENT_COST_PER_EXCEEDED_KM, DUSTER_FULL_TANK),
                     FLUENCE_LICENSE_PLATE:DasAuto('Renault Fluence', FLUENCE_LICENSE_PLATE, FLUENCE_RENT_COST, FLUENCE_RENT_COST_PER_EXCEEDED_KM, FLUENCE_FULL_TANK)}
    return AutorentSystem(catalogo)


a_monday_pickup_day = datetime(2015, 4, 6, 12, 0, 0, 0)

print(AutorentSystem.cost_for(create_system_using_data_from_the_exercise_assignment(), LOGAN_LICENSE_PLATE,
                a_monday_pickup_day, 1, a_monday_pickup_day + timedelta(days=1),
                LOGAN_FULL_TANK, MAX_KM_ALLOWED_PER_DAY + 85))
