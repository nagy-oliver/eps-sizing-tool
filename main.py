from constants import *
from utils import *

if __name__ == "__main__":
    area_transfer = array_size_from_power(POWER_IN_TRANSFER, SOLAR_FLUX_EARTH)
    area_mercury = array_size_from_power(POWER_IN_ORBIT, SOLAR_FLUX_MERCURY, MISSION_DURATION, ECLIPSE_FRACTION)

    incidence = array_incidence(area_mercury, area_transfer)

    array_mass = array_mass_from_area(area_transfer)

    battery_capacity_wh = battery_capacity(POWER_IN_ORBIT, ORBIT_PERIOD * ECLIPSE_FRACTION)
    battery_mass_kg = battery_mass_from_capacity(battery_capacity_wh)
    battery_volume_m3 = battery_volume_from_capacity(battery_capacity_wh)

    print(f"Final specs:")
    print(f"  - Area of the array: {area_transfer:.2f} m^2")
    print(f"  - Incidence angle at Mercury: {incidence:.2f} degrees")
    print(f"  - Mass of the array: {array_mass:.2f} kg")
    print(f"  - Battery capacity: {battery_capacity_wh:.2f} Wh")
    print(f"  - Battery mass: {battery_mass_kg:.2f} kg")
    print(f"  - Battery volume: {battery_volume_m3*1000:.2f} L")
    print(f"  - PCDU mass: {PCDU_MASS:.2f} kg")
    print(f"  - PCDU volume: {PCDU_VOLUME*1000:.2f} L")
    print()
    print(f"Total mass: {array_mass + battery_mass_kg + PCDU_MASS:.2f} kg")
    print(f"Total volume (excluding array): { battery_volume_m3*1000 + PCDU_VOLUME*1000:.2f} L")
