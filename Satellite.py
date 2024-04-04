import Orbital_bodies as Ob
from Satellite_subsystems import CPU_simulator, Power_management, Communication_systems

class Satellite(Ob.Orbital_body):
    def __init__(self, name, center, orbit_radius, orbital_period, initial_angle, color, size):
        super().__init__(name, center, orbit_radius, orbital_period, initial_angle, color, size)
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


"""
program = [
    "LOAD A 10",
    "LOAD B 5",
    "ADD A B",      # A = A + B -> A = 10 + 5
    "ADDI A 3",     # A = A + 3 -> A = 15 + 3
    "SUB A B",      # A = A - B -> A = 18 - 5
    "LOAD C 2",
    "LSHIFT A 1",   # A = A << 1 -> A = 13 << 1
    "RSHIFT C 1",   # C = C >> 1 -> C = 2 >> 1
    "LOG A",        # Should log 26
    "LOG C",        # Should log 1
    "ADD A A A"     # Should log an error
]

cpu = CPU_simulator()
cpu.load_program(program)
cpu.run()
"""