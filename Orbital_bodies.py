import numpy as np

class Orbital_body():
    def __init__(self, name, orbit_radius, orbital_period):
        self.name           = name
        self.orbit_radius   = orbit_radius      # Kilometers
        self.orbital_period = orbital_period    # Seconds
        self.orbital_speed  = self.calculate_orbital_speed()
        # Initial position
        self.position = np.array([np.cos(0) * orbit_radius, np.sin(0) * orbit_radius])

    def calculate_orbital_speed(self):
        # Calculate orbital speed based on the orbital period
        return (2 * np.pi) / self.orbital_period
    
    def update_position(self, time_step):
        # Update position based on the current time step
        angle = self.orbital_speed * time_step
        self.position = np.array([np.cos(angle) * self.orbit_radius, np.sin(angle) * self.orbit_radius])
    
    def print_position(self):
        print(f"{self.name} Position: {self.position}")

class Planet(Orbital_body):
    def __init__(self, name, orbit_radius, orbital_period):
        super().__init__(name, orbit_radius, orbital_period)

    def calculate_orbital_speed(self):
        return super().calculate_orbital_speed()
    
    def update_position(self, time_step):
        return super().update_position(time_step)
    
    def print_position(self):
        return super().print_position()

class Satellite(Orbital_body):
    def __init__(self, name, orbit_radius, orbital_period):
        super().__init__(name, orbit_radius, orbital_period)
        # SYSTEM STATS
        self.power_level = 100              # Percentage
        self.temperature = 20               # Celsius
        self.fuel_amount = 100              # Kilograms
        self.antenna_alignment = True       # Boolean
        self.system_health = True           # Boolean
        self.data_integrity = True          # Boolean
        self.communication_status = True    # Boolean
    
    def calculate_orbital_speed(self):
        return super().calculate_orbital_speed()

    def update_position(self, time_step):
        return super().update_position(time_step)
    
    def print_position(self):
        return super().print_position()

    def consume_power(self, amount):
        """Consume power for operations. Can lead to power shortage."""
        self.power_level -= amount
        if self.power_level < 20:
            print(f"{self.name}: Warning - Power level is critically low.")

    def adjust_temperature(self, change):
        """Adjust the satellite's temperature due to environmental conditions or operations."""
        self.temperature += change
        if self.temperature > 50 or self.temperature < 0:
            print(f"{self.name}: Warning - Temperature is out of operational range.")

    def consume_fuel(self, amount):
        """Consume fuel for maneuvers. Can lead to fuel depletion."""
        self.fuel_amount -= amount
        if self.fuel_amount < 10:
            print(f"{self.name}: Warning - Fuel level is critically low.")

    def damage_system(self, system_name):
        """Simulate damage to a system. Affects overall system health."""
        setattr(self, system_name, False)
        self.system_health = False
        print(f"{self.name}: Alert - {system_name} has been damaged.")

    def repair_system(self, system_name):
        """Repair a damaged system. Restores system to operational status."""
        setattr(self, system_name, True)
        # Check if all systems are operational to update system_health
        if all([self.antenna_alignment, self.data_integrity, self.communication_status]):
            self.system_health = True
        print(f"{self.name}: Info - {system_name} has been repaired.")

    def check_status(self):
        """Check and print the current status of the satellite."""
        print(f"{self.name} Status:")
        print(f" Power Level: {self.power_level}%")
        print(f" Temperature: {self.temperature}°C")
        print(f" Fuel Amount: {self.fuel_amount}kg")
        print(f" Antenna Alignment: {'Operational' if self.antenna_alignment else 'Damaged'}")
        print(f" System Health: {'Good' if self.system_health else 'Compromised'}")
        print(f" Data Integrity: {'Intact' if self.data_integrity else 'Corrupted'}")
        print(f" Communication Status: {'Online' if self.communication_status else 'Offline'}")
        self.print_position()

    