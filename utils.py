import math
from constants import *

### SOLAR ARRAY POWER SIZING ###

def array_size_from_power(power, flux, df_years = 0, eclipse_fraction = 0):
    size = power / (ARRAY_EFFICIENCY * flux)

    if (df_years):
        size /= (1 - DF) ** df_years

    if (eclipse_fraction):
        size /= (1 - eclipse_fraction)

    return size

def array_incidence(area, area_0_incidence):
    return math.degrees(math.acos(area / area_0_incidence))


### SOLAR ARRAY MASS SIZING ###

# Convert area in m^2 to mass in kg
def array_mass_from_area(area):
    return area / (ARRAY_AREA_PER_POWER * ARRAY_SPECIFIC_POWER / 1000)

### BATTERY POWER SIZING ###

# Returns the required battery capacity in Wh, takes t in seconds
def battery_capacity(power, t_discharge, dod=DOD, eff_bat=BATTERY_EFFICIENCY):
    return power * t_discharge / 3600 / (dod * eff_bat)

### BATTERY MASS SIZING ###

# Convert capacity in Wh to mass in kg
specific_energy = BATTERY_SPECIFIC_ENERGY*(1-CAPACITOR_POWER_RATIO) + CAPACITOR_SPECIFIC_ENERGY*CAPACITOR_POWER_RATIO
energy_density = BATTERY_ENERGY_DENSITY*(1-CAPACITOR_POWER_RATIO) + CAPACITOR_ENERGY_DENSITY*CAPACITOR_POWER_RATIO
def battery_mass_from_capacity(capacity, specific_energy=specific_energy):
    return capacity / specific_energy
# Convert capacity in Wh to volume in m^3
def battery_volume_from_capacity(capacity, energy_density=energy_density):
    return capacity / energy_density