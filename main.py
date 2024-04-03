import numpy as np
import time
from Orbital_bodies import Satellite, Planet
import Terminal_tools as tt

# Constants
SUN_POSITION = (0, 0)
PLANET_ORBITS = [100, 150]  # Arbitrary distances from the sun
SATELLITE_ORBIT = 120  # Arbitrary distance, between the two planets
SATELLITE_ORBIT_TIME = 83776
ORBITAL_TIMES = [62832, 134640]  # Orbital periods in seconds for two planets and the satellite

# Initialize orbital bodies
satellite = Satellite("GeoStationary Observer", SATELLITE_ORBIT, SATELLITE_ORBIT_TIME)
earth = Planet("Earth", PLANET_ORBITS[0], ORBITAL_TIMES[0])
mars = Planet("Mars", PLANET_ORBITS[1], ORBITAL_TIMES[1])

ORBITAL_BODIES = [satellite, earth, mars]

seconds_passed = 0
for time_step in range(1, 601):  # Simulate for 10 minutes as an example
    
    for x in ORBITAL_BODIES:
        x.update_position(time_step)
    #satellite.update_position(time_step)
    #earth.update_position(time_step)
    #mars.update_position(time_step)

    if seconds_passed % 10 == 0:  # Every 10 seconds
        print(f"Time: {seconds_passed}s")
        earth.print_position()
        mars.print_position()
        satellite.print_position()
        tt.print_line()
        satellite.check_status()  # Include satellite status checks as needed
        tt.print_line()

    time.sleep(1)
    seconds_passed += 1