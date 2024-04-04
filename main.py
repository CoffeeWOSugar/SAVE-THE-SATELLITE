import numpy as np
import time
from Orbital_bodies import Planet, Star
import Satellite
import Terminal_tools as tt
import Solar_system as ssys

# Constants

SYSTEM_SIZE = 1000
BASE_PLANET_TIME = 628

# Indecies
EARTH_INDEX = 0
MARS_INDEX = 1

SUN_POSITION = (0, 0)
SUN_SIZE     = 50

PLANET_ORBITS        = [int(SYSTEM_SIZE*0.03), int(SYSTEM_SIZE * 0.046)]  # Arbitrary distances from the sun
PLANET_ORBITAL_TIMES = [BASE_PLANET_TIME, int(1.88*BASE_PLANET_TIME)]  # Orbital periods in seconds for two planets and the satellite
PLANET_INITAL_ANGLES = [0, 2]
PLANET_SIZES         = [30, 25]

SATELLITE_ORBIT        = int(SYSTEM_SIZE*0.005)  # Arbitrary distance, between the two planets
SATELLITE_ORBIT_TIME   = 30
SATELLITE_INITAL_ANGLE = PLANET_INITAL_ANGLES[EARTH_INDEX]
SATELLITE_SIZE         = 10



# Initialize orbital bodies
sun       = Star("Sol", 'yellow', SUN_SIZE) # This is not right... 
mercury   = Planet("Mercury", sun, int(0.012*SYSTEM_SIZE),     int(00.24*BASE_PLANET_TIME), 0, 'gray', 10)
venus     = Planet("Venus",   sun, int(0.022*SYSTEM_SIZE),     int(00.62*BASE_PLANET_TIME), 3, 'white', 28)
earth     = Planet("Earth",   sun, PLANET_ORBITS[EARTH_INDEX], PLANET_ORBITAL_TIMES[EARTH_INDEX], PLANET_INITAL_ANGLES[EARTH_INDEX], 'blue', PLANET_SIZES[EARTH_INDEX])
mars      = Planet("Mars",    sun, PLANET_ORBITS[MARS_INDEX],  PLANET_ORBITAL_TIMES[MARS_INDEX], PLANET_INITAL_ANGLES[MARS_INDEX], 'red', PLANET_SIZES[MARS_INDEX])
jupiter   = Planet("Jupiter", sun, int(0.156*SYSTEM_SIZE),     int(11.86*BASE_PLANET_TIME), -1, 'brown', 330)
saturn    = Planet("Saturn",  sun, int(0.287*SYSTEM_SIZE),     int(29.46*BASE_PLANET_TIME), 1.2, 'gold', int(9.14*28))
uranus   = Planet("Uranus",  sun, int(0.576*SYSTEM_SIZE),     int(84.01*BASE_PLANET_TIME), 2.5, 'cyan', 120)
neptune   = Planet("Neptune", sun, int(0.900*SYSTEM_SIZE),     int(164.8*BASE_PLANET_TIME), 1-0, 'blue', int(3.86*28))

satellite = Satellite("GeoStationary Observer", earth, SATELLITE_ORBIT, SATELLITE_ORBIT_TIME, SATELLITE_INITAL_ANGLE, 'white', SATELLITE_SIZE)

ORBITAL_BODIES = [sun, mercury, venus, satellite, earth, mars, jupiter, saturn, uranus, neptune]

solar_system = ssys.SolarSystem(ORBITAL_BODIES, SYSTEM_SIZE)
solar_system.animate()

"""
seconds_passed = 0
for time_step in range(1, 601):  # Simulate for 10 minutes as an example
    
    for x in ORBITAL_BODIES:
        x.update_position(time_step)

    if seconds_passed % 10 == 0:  # Every 10 seconds
        print(f"Time: {seconds_passed}s")
        earth.print_position()
        mars.print_position()
        satellite.print_position()
        tt.print_line()
        satellite.check_status()  # Include satellite status checks as needed
        tt.print_line()

    time.sleep(1)
    seconds_passed += 1"""
