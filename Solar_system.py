import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Orbital_bodies import Planet, Satellite

class SolarSystem:
    def __init__(self, bodies, system_size):
        """
        Initializes the SolarSystem object with a list of planets.
        Each planet is represented as a dictionary with 'name', 'x', 'y', and optionally 'color'.
        """
        self.time         = 0
        self.system_size  = int(system_size)
        self.bodies      = bodies
        self.fig, self.ax = plt.subplots()
    
    def init_plot(self):
        """Initial setup for the plot, called before the animation starts."""
        self.ax.clear()
        self.ax.set_facecolor('black')
        self.ax.set_xlim(-self.system_size, self.system_size)
        self.ax.set_ylim(-self.system_size, self.system_size)
        # Initialize scatter plot objects for each planet.
        self.scatters = [self.ax.scatter(body.position[0], body.position[1], label=body.name, color=body.color, s=body.size) for body in self.bodies]
        self.ax.legend()
    
    def update(self, frame):
        """
        Update function for the animation.
        This function updates the positions of the planets.
        For now, we'll just move each planet randomly.
        """
        for scatter, body in zip(self.scatters, self.bodies):
            # Here you would update the planet's position based on actual calculations.
            # For demonstration, we'll just move them randomly.
            body.update_position(self.time)
            scatter.set_offsets([body.position[0], body.position[1]])
        self.time += 1
    
    def animate(self):
        """Creates the animation."""
        self.init_plot()
        anim = FuncAnimation(self.fig, self.update, init_func=self.init_plot, frames=200, interval=250, blit=False)
        plt.show()
