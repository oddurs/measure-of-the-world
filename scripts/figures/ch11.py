#!/usr/bin/env python3
"""Generate figures for Chapter 11: Edmond Halley's Broader Canvas."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Arc
import numpy as np


def transit_parallax():
    """Diagram showing how transit parallax reveals the solar distance.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 5))

    # Sun (large circle)
    sun = Circle((0, 0), 1.5, facecolor='#FFD700', edgecolor='black', linewidth=1.5)
    ax.add_patch(sun)
    ax.text(0, 0, 'Sun', fontsize=10, ha='center', va='center')

    # Earth (small circle on right)
    earth_x = 4
    earth = Circle((earth_x, 0), 0.2, facecolor='#1f77b4', edgecolor='black', linewidth=1)
    ax.add_patch(earth)
    ax.text(earth_x, -0.4, 'Earth', fontsize=8, ha='center')

    # Two observers on Earth
    obs_a_angle = 30
    obs_b_angle = -30
    obs_r = 0.2

    obs_a_x = earth_x + obs_r * np.cos(np.radians(obs_a_angle))
    obs_a_y = obs_r * np.sin(np.radians(obs_a_angle))
    obs_b_x = earth_x + obs_r * np.cos(np.radians(180 + obs_b_angle))
    obs_b_y = obs_r * np.sin(np.radians(180 + obs_b_angle))

    ax.plot(obs_a_x, obs_a_y, 'ko', markersize=4)
    ax.plot(obs_b_x, obs_b_y, 'ko', markersize=4)
    ax.text(obs_a_x + 0.15, obs_a_y + 0.15, 'A', fontsize=8)
    ax.text(obs_b_x - 0.15, obs_b_y - 0.15, 'B', fontsize=8)

    # Venus (transiting planet)
    venus_x = 2.0
    venus = Circle((venus_x, 0.1), 0.08, facecolor='black', edgecolor='none')
    ax.add_patch(venus)
    ax.text(venus_x, 0.35, 'Venus', fontsize=8, ha='center')

    # Lines of sight from observers to Venus
    ax.plot([obs_a_x, venus_x], [obs_a_y, 0.1], 'r--', linewidth=0.8, alpha=0.7)
    ax.plot([obs_b_x, venus_x], [obs_b_y, 0.1], 'b--', linewidth=0.8, alpha=0.7)

    # Extended lines to Sun (showing apparent positions)
    # From A
    dx_a = venus_x - obs_a_x
    dy_a = 0.1 - obs_a_y
    extend = 1.5
    ax.plot([venus_x, venus_x - extend * dx_a], [0.1, 0.1 - extend * dy_a],
            'r:', linewidth=0.8, alpha=0.5)

    # From B
    dx_b = venus_x - obs_b_x
    dy_b = 0.1 - obs_b_y
    ax.plot([venus_x, venus_x - extend * dx_b], [0.1, 0.1 - extend * dy_b],
            'b:', linewidth=0.8, alpha=0.5)

    # Show parallax angle
    ax.annotate('', xy=(-0.5, 0.4), xytext=(-0.5, -0.3),
                arrowprops=dict(arrowstyle='<->', color='green', lw=1.5))
    ax.text(-0.7, 0.05, 'Parallax', fontsize=8, color='green', rotation=90, va='center')

    # Key equation
    ax.text(2, -1.5, r'$\pi_{transit} = \pi_\odot \cdot \frac{d_{Venus}}{d_{Sun}}$' + '\n' +
            r'Measure parallax $\rightarrow$ compute solar distance',
            fontsize=9, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-2.5, 5)
    ax.set_ylim(-2, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'transit-parallax', chapter=11)


def halley_comet_orbit():
    """Visualization of Halley's comet elliptical orbit.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 5))

    # Comet orbit (highly elliptical)
    a = 17.8  # semi-major axis in AU
    e = 0.967  # eccentricity
    b = a * np.sqrt(1 - e**2)

    # Plot orbit
    theta = np.linspace(0, 2 * np.pi, 1000)
    r = a * (1 - e**2) / (1 + e * np.cos(theta))
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Scale for display
    scale = 0.15
    ax.plot(x * scale, y * scale, 'gray', linewidth=1.5, alpha=0.7)

    # Sun at focus
    sun = Circle((0, 0), 0.1, facecolor='#FFD700', edgecolor='black', linewidth=1)
    ax.add_patch(sun)
    ax.text(0.15, 0.1, 'Sun', fontsize=8)

    # Planet orbits for scale
    for radius in [0.39, 0.72, 1.0, 1.52, 5.2, 9.5]:
        circle = Circle((0, 0), radius * scale, fill=False,
                        edgecolor='blue', linewidth=0.5, alpha=0.3)
        ax.add_patch(circle)

    # Label Neptune orbit for comparison
    ax.text(2.5, -0.5, 'Neptune orbit\n(30 AU)', fontsize=7, color='blue', alpha=0.5)

    # Comet at perihelion and aphelion
    perihelion = a * (1 - e) * scale
    aphelion = a * (1 + e) * scale

    ax.plot(perihelion, 0, 'ko', markersize=6)
    ax.text(perihelion + 0.1, 0.15, 'Perihelion\n(0.6 AU)', fontsize=7)

    ax.plot(-aphelion, 0, 'ko', markersize=4)
    ax.text(-aphelion, 0.2, 'Aphelion\n(35 AU)', fontsize=7, ha='center')

    # Arrow showing direction
    ax.annotate('', xy=(0.5, 0.8), xytext=(0.8, 0.5),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1))

    # Period annotation
    ax.text(0, -2.5, 'Orbital period: 76 years\n' +
            "Halley's prediction (1705): return in 1758\n" +
            'Observed return: December 1758',
            fontsize=9, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-6, 3)
    ax.set_ylim(-3, 2)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'halley-comet-orbit', chapter=11)


def magnetic_variation():
    """Conceptual diagram of magnetic variation (isogonic lines).
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 5))

    # Simplified Earth outline (circle)
    earth = Circle((0, 0), 2, fill=False, edgecolor='black', linewidth=1.5)
    ax.add_patch(earth)

    # Geographic pole (top)
    ax.plot(0, 2, 'k^', markersize=8)
    ax.text(0, 2.2, 'Geographic\nNorth', fontsize=8, ha='center', va='bottom')

    # Magnetic pole (offset)
    mag_pole_x = 0.5
    mag_pole_y = 1.7
    ax.plot(mag_pole_x, mag_pole_y, 'r^', markersize=8)
    ax.text(mag_pole_x + 0.2, mag_pole_y, 'Magnetic\nNorth', fontsize=8, ha='left', color='red')

    # Compass at different locations showing variation
    locations = [
        (-1.2, 0.5, 15, 'E'),   # Location with easterly variation
        (0.8, -0.3, -10, 'W'),  # Location with westerly variation
        (-0.3, -1.2, 5, 'E'),   # Small variation
    ]

    for lx, ly, variation, direction in locations:
        # Compass circle
        comp = Circle((lx, ly), 0.25, fill=False, edgecolor='gray', linewidth=1)
        ax.add_patch(comp)

        # True north arrow (vertical)
        ax.annotate('', xy=(lx, ly + 0.25), xytext=(lx, ly),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1))

        # Magnetic north arrow (rotated)
        var_rad = np.radians(variation)
        ax.annotate('', xy=(lx + 0.25 * np.sin(var_rad), ly + 0.25 * np.cos(var_rad)),
                    xytext=(lx, ly),
                    arrowprops=dict(arrowstyle='->', color='red', lw=1))

        # Label
        ax.text(lx, ly - 0.4, f'{abs(variation)}{direction}', fontsize=7, ha='center')

    # Isogonic lines (simplified curves)
    for offset in [-0.8, 0, 0.8]:
        theta = np.linspace(-np.pi/2, np.pi/2, 50)
        x = (1.5 + offset) * np.sin(theta)
        y = 1.5 * np.cos(theta) + offset * 0.3
        mask = x**2 + y**2 < 4
        ax.plot(x[mask], y[mask], 'g--', linewidth=0.8, alpha=0.5)

    ax.text(1.5, -0.8, 'Isogonic\nlines', fontsize=7, color='green', ha='center')

    # Legend
    ax.text(0, -2.7, 'Magnetic variation: angle between\ntrue north and compass north\n' +
            "(Halley's 1701 chart was first to map this)",
            fontsize=8, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 2.8)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'magnetic-variation', chapter=11)


def halley_life_table():
    """Visualization of Halley's life table concept.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 4))

    # Simplified survival curve based on Halley's Breslau data
    ages = np.arange(0, 85, 1)

    # Approximate survival curve (not actual Halley data, illustrative)
    # High infant mortality, then slower decline
    survival = np.zeros_like(ages, dtype=float)
    survival[0] = 1000
    for i in range(1, len(ages)):
        if i < 5:
            mortality_rate = 0.15  # High infant mortality
        elif i < 20:
            mortality_rate = 0.02
        elif i < 50:
            mortality_rate = 0.015
        elif i < 70:
            mortality_rate = 0.04
        else:
            mortality_rate = 0.08
        survival[i] = survival[i-1] * (1 - mortality_rate)

    # Normalize to start at 1000
    survival = survival / survival[0] * 1000

    ax.plot(ages, survival, 'b-', linewidth=1.5)
    ax.fill_between(ages, 0, survival, alpha=0.2)

    # Mark key ages
    key_ages = [1, 20, 50, 70]
    for age in key_ages:
        surv = survival[age]
        ax.plot(age, surv, 'ko', markersize=5)
        ax.annotate(f'{int(surv)}', xy=(age, surv), xytext=(age + 3, surv + 30),
                    fontsize=7, arrowprops=dict(arrowstyle='->', lw=0.5))

    ax.set_xlabel('Age (years)')
    ax.set_ylabel('Survivors (from 1000 births)')
    ax.set_title("Halley's Life Table (Breslau, 1693)", fontsize=10)
    ax.set_xlim(0, 85)
    ax.set_ylim(0, 1100)
    ax.grid(True, alpha=0.3)

    # Annotation
    ax.text(50, 900, 'First actuarial\nlife table', fontsize=8, style='italic')

    plt.tight_layout()
    save_figure(fig, 'halley-life-table', chapter=11)


if __name__ == "__main__":
    transit_parallax()
    halley_comet_orbit()
    magnetic_variation()
    halley_life_table()
