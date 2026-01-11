#!/usr/bin/env python3
"""Generate figures for Chapter 12: Bradley and the Aberration of Starlight."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Arc, Wedge
import numpy as np


def aberration_geometry():
    """Diagram showing how Earth's motion causes aberration of starlight.

    Uses the rain/moving carriage analogy - light appears to come from
    a shifted direction due to Earth's orbital velocity.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 5))

    # Earth (moving to the right)
    earth_x, earth_y = 0, 0
    earth = Circle((earth_x, earth_y), 0.3, facecolor='#1f77b4',
                   edgecolor='black', linewidth=1.5)
    ax.add_patch(earth)
    ax.text(earth_x, earth_y - 0.5, 'Earth', fontsize=9, ha='center')

    # Earth's velocity vector (horizontal)
    ax.annotate('', xy=(1.5, 0), xytext=(0.4, 0),
                arrowprops=dict(arrowstyle='->', color='#d62728', lw=2))
    ax.text(1.0, 0.25, r'$v_E$', fontsize=11, ha='center', color='#d62728')
    ax.text(1.0, -0.3, '(30 km/s)', fontsize=8, ha='center', color='#d62728')

    # True direction of starlight (vertical, from above)
    star_x, star_y = 0, 4
    ax.plot(star_x, star_y, '*', color='gold', markersize=15,
            markeredgecolor='black', markeredgewidth=0.5)
    ax.text(star_x + 0.3, star_y, 'True star\nposition', fontsize=8, ha='left')

    # True light ray (vertical)
    ax.annotate('', xy=(0, 0.4), xytext=(0, 3.5),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.5,
                               linestyle='--'))
    ax.text(-0.4, 2, r'$c$', fontsize=11, ha='center', color='gray')

    # Apparent direction (tilted)
    # Aberration angle ~ v/c ~ 30/300000 ~ 10^-4 radians ~ 20.5 arcsec
    # For visualization, exaggerate the angle
    apparent_angle = 0.3  # radians (exaggerated for visibility)
    apparent_x = star_x + 3.5 * np.sin(apparent_angle)
    apparent_y = star_y

    # Apparent star position
    ax.plot(apparent_x, apparent_y, '*', color='gold', markersize=12,
            markeredgecolor='black', markeredgewidth=0.5, alpha=0.6)
    ax.text(apparent_x + 0.3, apparent_y, 'Apparent\nposition',
            fontsize=8, ha='left', alpha=0.8)

    # Apparent light ray
    ax.annotate('', xy=(0.3, 0.4), xytext=(apparent_x - 0.2, 3.5),
                arrowprops=dict(arrowstyle='->', color='#ff7f0e', lw=2))

    # Aberration angle arc
    arc = Arc((0, 3.5), 1.0, 1.0, angle=0, theta1=-90, theta2=-90 +
              np.degrees(apparent_angle), color='green', lw=2)
    ax.add_patch(arc)
    ax.text(0.5, 3.2, r'$\theta_{ab}$', fontsize=10, color='green')

    # Vector diagram (inset)
    inset_x, inset_y = -2.5, 1.5
    ax.text(inset_x, inset_y + 1.5, 'Velocity addition:', fontsize=9,
            fontweight='bold', ha='center')

    # c vector (vertical)
    ax.annotate('', xy=(inset_x, inset_y - 1), xytext=(inset_x, inset_y + 1),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))
    ax.text(inset_x - 0.25, inset_y, r'$c$', fontsize=10, ha='right', color='gray')

    # v_E vector (horizontal)
    ax.annotate('', xy=(inset_x + 0.6, inset_y - 1), xytext=(inset_x, inset_y - 1),
                arrowprops=dict(arrowstyle='->', color='#d62728', lw=1.5))
    ax.text(inset_x + 0.3, inset_y - 1.3, r'$v_E$', fontsize=10,
            ha='center', color='#d62728')

    # Resultant
    ax.annotate('', xy=(inset_x + 0.6, inset_y - 1), xytext=(inset_x, inset_y + 1),
                arrowprops=dict(arrowstyle='->', color='#ff7f0e', lw=1.5))
    ax.text(inset_x + 0.5, inset_y, 'Apparent', fontsize=8,
            ha='left', color='#ff7f0e')

    # Formula
    ax.text(0, -1.5, r'$\theta_{aberration} = \frac{v_E}{c} \approx 20.5$ arcseconds',
            fontsize=11, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-4, 3)
    ax.set_ylim(-2.2, 5)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'aberration-geometry', chapter=12)


def aberration_ellipse():
    """Shows how a star traces an aberration ellipse over a year.

    As Earth orbits, its velocity direction changes, causing the
    apparent stellar position to trace out an ellipse.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 6))

    # Central true position
    ax.plot(0, 0, '*', color='gold', markersize=20,
            markeredgecolor='black', markeredgewidth=1)
    ax.text(0.1, -0.1, 'True\nposition', fontsize=8, ha='left', va='top')

    # Aberration circle (for a star at pole of ecliptic)
    # For stars off the ecliptic pole, it's an ellipse
    kappa = 20.5  # arcseconds
    theta = np.linspace(0, 2*np.pi, 100)

    # Circle for star at ecliptic pole
    x_circle = kappa * np.cos(theta)
    y_circle = kappa * np.sin(theta)
    ax.plot(x_circle, y_circle, 'b-', linewidth=2, alpha=0.7,
            label='Star at ecliptic pole')

    # Ellipse for star at 45° from ecliptic pole
    x_ellipse = kappa * np.cos(theta)
    y_ellipse = kappa * np.sin(theta) * np.sin(np.radians(45))
    ax.plot(x_ellipse, y_ellipse, 'r--', linewidth=2, alpha=0.7,
            label='Star at 45° ecliptic latitude')

    # Mark positions at different times of year
    months = ['Mar', 'Jun', 'Sep', 'Dec']
    angles = [0, np.pi/2, np.pi, 3*np.pi/2]

    for month, angle in zip(months, angles):
        x = kappa * np.cos(angle)
        y = kappa * np.sin(angle)
        ax.plot(x, y, 'ko', markersize=8)

        # Position label slightly outside
        offset = 1.15
        ax.text(x * offset, y * offset, month, fontsize=9,
                ha='center', va='center')

    # Earth orbit (inset in corner)
    inset_ax = fig.add_axes([0.12, 0.12, 0.25, 0.25])
    sun = Circle((0, 0), 0.15, facecolor='#FFD700', edgecolor='black')
    inset_ax.add_patch(sun)

    # Earth orbit
    orbit_theta = np.linspace(0, 2*np.pi, 100)
    inset_ax.plot(np.cos(orbit_theta), np.sin(orbit_theta), 'b-', lw=1)

    # Earth at March position
    inset_ax.plot(1, 0, 'o', color='#1f77b4', markersize=8)
    inset_ax.annotate('', xy=(1, 0.6), xytext=(1, 0.1),
                      arrowprops=dict(arrowstyle='->', color='#d62728', lw=1.5))

    inset_ax.set_xlim(-1.5, 1.5)
    inset_ax.set_ylim(-1.5, 1.5)
    inset_ax.set_aspect('equal')
    inset_ax.axis('off')
    inset_ax.text(0, -1.4, 'Earth orbit', fontsize=7, ha='center')

    ax.set_xlim(-35, 35)
    ax.set_ylim(-35, 35)
    ax.set_xlabel('Apparent displacement (arcseconds)', fontsize=10)
    ax.set_ylabel('Apparent displacement (arcseconds)', fontsize=10)
    ax.axhline(0, color='gray', lw=0.5, alpha=0.5)
    ax.axvline(0, color='gray', lw=0.5, alpha=0.5)
    ax.legend(loc='upper right', fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_aspect('equal')

    save_figure(fig, 'aberration-ellipse', chapter=12)


def bradley_observations():
    """Bradley's observations of gamma Draconis showing the annual cycle.

    Plots the sinusoidal variation due to aberration with the fitted model.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 4))

    # Time axis (months from Jan 1726)
    months = np.array([0, 2, 5, 8, 11, 14, 17])  # Selected observation epochs
    month_labels = ['Dec 1725', 'Feb', 'May', 'Aug', 'Nov 1726', 'Feb 1727', 'May']

    # Zenith distance observations (illustrative, based on text)
    # Positive = north of zenith
    observations = np.array([-20.5, -10, 15, 20, 5, -15, -20])

    # Model: z = kappa * sin(2*pi*t/12 + phi)
    t_model = np.linspace(0, 18, 200)
    kappa = 20.5
    phi = -0.5  # Phase offset
    z_model = kappa * np.sin(2 * np.pi * t_model / 12 + phi)

    # Plot
    ax.plot(t_model, z_model, 'b-', linewidth=1.5, label='Aberration model')
    ax.plot(months, observations, 'ko', markersize=8, label="Bradley's observations")

    # Zero line
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.5)

    # Amplitude markers
    ax.axhline(20.5, color='red', linestyle=':', linewidth=1, alpha=0.5)
    ax.axhline(-20.5, color='red', linestyle=':', linewidth=1, alpha=0.5)
    ax.text(18.5, 20.5, r'$+\kappa$', fontsize=9, va='center', color='red')
    ax.text(18.5, -20.5, r'$-\kappa$', fontsize=9, va='center', color='red')

    ax.set_xlabel('Months from December 1725', fontsize=10)
    ax.set_ylabel('Zenith distance (arcseconds)', fontsize=10)
    ax.set_xlim(-1, 19)
    ax.set_ylim(-30, 30)
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, alpha=0.3)

    # Annotation
    ax.text(9, -26, r'$z(t) = 20.5 \sin(2\pi t/T + \phi)$ where $T = 1$ year',
            fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    plt.tight_layout()
    save_figure(fig, 'bradley-observations', chapter=12)


def stellar_effects_comparison():
    """Compare parallax, aberration, and nutation amplitudes.

    Bar chart showing the relative sizes of these effects.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 4))

    effects = ['Parallax\n(nearby star)', 'Aberration', 'Nutation']
    amplitudes = [0.3, 20.5, 9.2]  # arcseconds
    colors = ['#2ca02c', '#1f77b4', '#ff7f0e']

    bars = ax.bar(effects, amplitudes, color=colors, edgecolor='black', linewidth=1)

    # Value labels
    for bar, amp in zip(bars, amplitudes):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 0.5,
                f'{amp}"', ha='center', va='bottom', fontsize=10)

    # Detection threshold line
    ax.axhline(2, color='red', linestyle='--', linewidth=1.5, alpha=0.7)
    ax.text(2.5, 2.5, 'Detection threshold\n(~2 arcsec)', fontsize=8,
            ha='right', color='red')

    ax.set_ylabel('Amplitude (arcseconds)', fontsize=10)
    ax.set_ylim(0, 25)
    ax.grid(True, axis='y', alpha=0.3)

    # Annotation
    ax.text(0.5, -4, 'Bradley detected aberration and nutation,\nbut parallax remained below threshold',
            fontsize=9, ha='center', transform=ax.transAxes,
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    plt.tight_layout()
    save_figure(fig, 'stellar-effects-comparison', chapter=12)


def nutation_diagram():
    """Diagram showing Earth's nutation - the 18.6-year wobble.

    Shows how the Moon's orbital plane causes a periodic nod in Earth's axis.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 5))

    # Earth
    earth = Circle((0, 0), 1, facecolor='#1f77b4', edgecolor='black',
                   linewidth=1.5, alpha=0.7)
    ax.add_patch(earth)

    # Equatorial bulge (ellipse)
    bulge = mpatches.Ellipse((0, 0), 2.3, 1.8, angle=0,
                              facecolor='none', edgecolor='#1f77b4',
                              linewidth=1, linestyle='--', alpha=0.5)
    ax.add_patch(bulge)
    ax.text(1.3, 0.6, 'Equatorial\nbulge', fontsize=7, ha='center', alpha=0.7)

    # Mean rotation axis
    ax.annotate('', xy=(0, 2.5), xytext=(0, -1.5),
                arrowprops=dict(arrowstyle='->', color='black', lw=2))
    ax.text(0.15, 2.3, 'Mean axis', fontsize=9, ha='left')

    # Nutating axis (slight wobble)
    nutation_angle = 0.15  # radians
    ax.annotate('', xy=(nutation_angle * 2, 2.4), xytext=(0, -1.5),
                arrowprops=dict(arrowstyle='->', color='#d62728', lw=2,
                               linestyle='--'))

    # Nutation cone
    cone_theta = np.linspace(0, 2*np.pi, 100)
    cone_radius = 0.3
    cone_x = cone_radius * np.cos(cone_theta)
    cone_y = 2.5 + cone_radius * np.sin(cone_theta) * 0.3
    ax.plot(cone_x, cone_y, 'r-', linewidth=1, alpha=0.7)
    ax.text(0.5, 2.7, 'Nutation\n(9" amplitude)', fontsize=8,
            ha='left', color='#d62728')

    # Moon orbit (inclined ellipse in background)
    moon_theta = np.linspace(0, 2*np.pi, 100)
    moon_x = 3 * np.cos(moon_theta)
    moon_y = 0.8 * np.sin(moon_theta) + 0.5
    ax.plot(moon_x, moon_y, 'gray', linewidth=1, alpha=0.5)
    ax.plot(2.5, 1.0, 'o', color='#888888', markersize=10)
    ax.text(2.7, 1.2, 'Moon', fontsize=8, color='gray')

    # Torque arrow
    ax.annotate('', xy=(1.5, 0.3), xytext=(2.2, 0.8),
                arrowprops=dict(arrowstyle='->', color='green', lw=1.5))
    ax.text(2.0, 0.2, 'Gravitational\ntorque', fontsize=8, color='green', ha='center')

    # Period annotation
    ax.text(0, -2.5, 'Period: 18.6 years\n(Lunar nodal regression)',
            fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-4, 4)
    ax.set_ylim(-3, 3.5)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'nutation-diagram', chapter=12)


def zenith_sector():
    """Simplified diagram of the zenith sector instrument.

    Shows the key components: telescope, graduated arc, and pivot.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(5, 6))

    # Vertical reference (wall/mounting)
    ax.plot([-0.5, -0.5], [-2, 4], 'k-', linewidth=3)
    ax.text(-0.7, 4, 'Wall mount', fontsize=8, ha='right', va='bottom')

    # Pivot point
    pivot = Circle((-0.5, 3), 0.15, facecolor='gray', edgecolor='black',
                   linewidth=2)
    ax.add_patch(pivot)
    ax.text(-0.3, 3.3, 'Pivot', fontsize=8, ha='left')

    # Telescope tube (can pivot slightly)
    angle = 5  # degrees from vertical
    length = 4
    telescope_end_x = -0.5 + length * np.sin(np.radians(angle))
    telescope_end_y = 3 - length * np.cos(np.radians(angle))

    ax.plot([-0.5, telescope_end_x], [3, telescope_end_y],
            color='#8B4513', linewidth=8, solid_capstyle='round')
    ax.text(telescope_end_x + 0.3, telescope_end_y - 0.2, 'Eyepiece',
            fontsize=8, ha='left')

    # Objective end
    ax.plot([-0.5, -0.5 - 0.3*np.sin(np.radians(angle))],
            [3, 3 + 0.3*np.cos(np.radians(angle))],
            color='#8B4513', linewidth=8, solid_capstyle='round')
    ax.text(-0.3, 3.4, 'Objective', fontsize=8, ha='left')

    # Graduated arc
    arc_radius = 3.5
    arc = Arc((-0.5, 3), 2*arc_radius, 2*arc_radius, angle=0,
              theta1=260, theta2=280, color='#1f77b4', linewidth=3)
    ax.add_patch(arc)

    # Tick marks on arc
    for deg in range(-10, 11, 5):
        theta = np.radians(270 + deg)
        x1 = -0.5 + (arc_radius - 0.1) * np.cos(theta)
        y1 = 3 + (arc_radius - 0.1) * np.sin(theta)
        x2 = -0.5 + (arc_radius + 0.1) * np.cos(theta)
        y2 = 3 + (arc_radius + 0.1) * np.sin(theta)
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=1)

    ax.text(2.2, -0.3, 'Graduated\narc', fontsize=8, ha='center', color='#1f77b4')

    # Star ray from zenith
    ax.annotate('', xy=(-0.5, 3.3), xytext=(-0.5, 5),
                arrowprops=dict(arrowstyle='->', color='gold', lw=2))
    ax.text(-0.3, 4.5, 'Starlight\n(from zenith)', fontsize=8, ha='left', color='#B8860B')

    # Zenith indicator
    ax.plot([-0.5, -0.5], [3, 5.5], 'k--', linewidth=0.5, alpha=0.5)
    ax.text(-0.5, 5.6, 'Zenith', fontsize=9, ha='center')

    # Features annotation
    ax.text(0, -2.5, 'Zenith sector:\n- Observes stars near overhead\n- Minimal refraction correction\n- Arc readable to ~1 arcsec',
            fontsize=8, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-2, 4)
    ax.set_ylim(-3, 6)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'zenith-sector', chapter=12)


def speed_of_light():
    """Visualization of how aberration gives the speed of light.

    Shows the relationship between aberration angle, Earth velocity, and c.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 4))

    # Flow diagram
    boxes = [
        ('Measure\naberration\nangle', 0, 2, '#e6f3ff'),
        ('Known:\nEarth velocity\n$v_E = 30$ km/s', 0, 1, '#fff2e6'),
        (r'$\theta = \frac{v_E}{c}$', 0, 0, '#ffe6e6'),
        (r'$c = \frac{v_E}{\theta}$' + '\n= 300,000 km/s', 0, -1, '#e6ffe6'),
    ]

    box_width = 2.5
    box_height = 0.7

    for label, x, y, color in boxes:
        box = FancyBboxPatch((x - box_width/2, y - box_height/2),
                             box_width, box_height,
                             boxstyle="round,pad=0.05,rounding_size=0.1",
                             facecolor=color, edgecolor='black', linewidth=1)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=9)

    # Arrows
    for i in range(len(boxes) - 1):
        y1 = boxes[i][2] - box_height/2
        y2 = boxes[i+1][2] + box_height/2
        ax.annotate('', xy=(0, y2), xytext=(0, y1),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.2))

    # Values on right side
    ax.text(2, 2, r'$\theta = 20.5'' = 10^{-4}$ rad', fontsize=9, ha='left', va='center')
    ax.text(2, -1, 'First astronomical\nspeed of light!', fontsize=9, ha='left',
            va='center', style='italic')

    ax.set_xlim(-2, 4)
    ax.set_ylim(-2, 3)
    ax.axis('off')

    save_figure(fig, 'speed-of-light', chapter=12)


if __name__ == "__main__":
    aberration_geometry()
    aberration_ellipse()
    bradley_observations()
    stellar_effects_comparison()
    nutation_diagram()
    zenith_sector()
    speed_of_light()
