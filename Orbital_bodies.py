import numpy as np

class Star():
    def __init__(self, name, color, size):
        self.name  = name
        self.color = color
        self.size  = size
        # Inital position
        self.position = np.array([0, 0])
    
    def update_position(self, _):
        pass

class Orbital_body():
    def __init__(self, name, center, orbit_radius, orbital_period, initial_angle, color, size):
        self.name           = name
        self.center         = center
        self.orbit_radius   = orbit_radius      # Kilometers
        self.orbital_period = orbital_period    # Seconds
        self.orbital_speed  = self.calculate_orbital_speed()
        self.color          = color 
        self.size           = size
        # Initial position
        self.initial_angle  = initial_angle
        self.position = np.array([np.cos(initial_angle) * orbit_radius, np.sin(initial_angle) * orbit_radius])

    def calculate_orbital_speed(self):
        # Calculate orbital speed based on the orbital period
        return (2 * np.pi) / self.orbital_period
    
    def update_position(self, time_step):
        # Update position based on the current time step
        angle = self.initial_angle + self.orbital_speed * time_step
        self.position = self.center.position + np.array([np.cos(angle) * self.orbit_radius, np.sin(angle) * self.orbit_radius])
    
    def print_position(self):
        print(f"{self.name} Position: {self.position}")

class Planet(Orbital_body):
    def __init__(self, name, center, orbit_radius, orbital_period, initial_angle, color, size):
        super().__init__(name, center, orbit_radius, orbital_period, initial_angle, color, size)

    def calculate_orbital_speed(self):
        return super().calculate_orbital_speed()
    
    def update_position(self, time_step):
        return super().update_position(time_step)
    
    def print_position(self):
        return super().print_position()



    