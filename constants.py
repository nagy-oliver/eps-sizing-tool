MISSION_DURATION = 7.5+1    # Mission duration (transfer + orbit) in years
ORBIT_PERIOD = 7625.65      # Orbital period around Mercury in seconds

ARRAY_EFFICIENCY = 0.268    # Efficiency of the solar array
CON_DIS_EFFICIENCY = 0.8    # Efficiency of conditioning and distribution
SOLAR_FLUX_EARTH = 1361     # Solar flux at Earth's orbit in W/m^2
SOLAR_FLUX_MERCURY = 6272   # Solar flux at Mercury's orbit in W/m^2
ECLIPSE_FRACTION = 0.28     # Fraction of orbit in shadow
DF = 0.0325                 # Degradation factor in % per year

# Details of the Triple junction GaAs rigid solar cells
# Given for 1 AU, only useful for Mercury when combined
ARRAY_SPECIFIC_POWER = 70    # W/kg
ARRAY_AREA_PER_POWER = 3.12  # m^2/kW

# Battery parameters
DOD = 0.3
BATTERY_EFFICIENCY = 0.9
BATTERY_SPECIFIC_ENERGY = 133       # Wh/kg
BATTERY_ENERGY_DENSITY = 321*1000   # Wh/m^3
# Supercapacitor parameters
CAPACITOR_SPECIFIC_ENERGY = 7     # Wh/kg
CAPACITOR_ENERGY_DENSITY = 9*1000 # Wh/m^3
CAPACITOR_POWER_RATIO = 0.1       # What fraction of power will be provided by the supercapacitor
# CAPACITOR_POWER_RATIO = 0       # (option 2)
CAPACITOR_POWER_DENSITY = 20000   # W/kg


# PCDU data (Thales ARSAT PCDU)
PCDU_MASS = 16.6                  # kg
PCDU_VOLUME = 332*345*193 * 1e-9  # m^3
# PCU and PDU data combined (option 2) 
# PCDU_MASS = 6.5+16
# PCDU_VOLUME = (286*196*142 + 455*270*200) * 1e-9

# Subsystems and their power requirement in watts, with 20% margin
SUBSYSTEMS = {
    "comms": {
        "power": 279.684,
        "transfer_fraction": 0.3
    },
    "adcs": {
        "power": 111.41*1.2,
        "transfer_fraction": 1
    },
    "obdh": {
        "power": 129.6,
        "transfer_fraction": 1
    },
    "payload": {
        "power": 100.8,
        "transfer_fraction": 0
    },
    "prop": {
        "power": 5,
        "transfer_fraction": 1
    },
    "eps": {
        "power": 5,
        "transfer_fraction": 1
    }
}

POWER_IN_ORBIT = sum(subsystem["power"] for subsystem in SUBSYSTEMS.values()) / CON_DIS_EFFICIENCY
POWER_IN_TRANSFER = sum(
    subsystem["power"] * subsystem["transfer_fraction"] for subsystem in SUBSYSTEMS.values()
) / CON_DIS_EFFICIENCY