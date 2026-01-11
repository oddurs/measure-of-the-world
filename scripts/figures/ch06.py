#!/usr/bin/env python3
"""Generate figures for Chapter 6: The Clock Problem, Part One: Pendulum Limitations."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, Arc, Circle, Wedge
import numpy as np


def pendulum_physics():
    """Diagram showing pendulum geometry, forces, and the restoring torque.
    """
    setup_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 4))

    # Left panel: Pendulum geometry and forces
    L = 1.0  # pendulum length (normalized)
    theta = 25  # degrees
    theta_rad = np.radians(theta)

    # Pivot point
    pivot = (0, 0)

    # Bob position
    bob_x = L * np.sin(theta_rad)
    bob_y = -L * np.cos(theta_rad)

    # Draw pendulum rod
    ax1.plot([0, bob_x], [0, bob_y], 'k-', linewidth=2)

    # Draw pivot
    ax1.plot(0, 0, 'ko', markersize=8)

    # Draw bob
    ax1.plot(bob_x, bob_y, 'o', color='#1f77b4', markersize=20)

    # Draw vertical reference
    ax1.plot([0, 0], [0, -L - 0.2], 'k--', linewidth=0.8, alpha=0.5)

    # Draw angle arc
    arc_radius = 0.25
    arc = Arc((0, 0), 2*arc_radius, 2*arc_radius,
              angle=0, theta1=-90, theta2=-90+theta,
              color='green', linewidth=1.5)
    ax1.add_patch(arc)
    ax1.text(0.1, -0.35, r'$\theta$', fontsize=12, color='green')

    # Draw gravity force (mg)
    arrow_scale = 0.3
    ax1.annotate('', xy=(bob_x, bob_y - arrow_scale),
                 xytext=(bob_x, bob_y),
                 arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax1.text(bob_x + 0.08, bob_y - arrow_scale/2, r'$mg$', fontsize=11, color='red')

    # Draw restoring force component (tangential)
    # Tangent direction at bob: perpendicular to rod
    tangent_x = np.cos(theta_rad)
    tangent_y = np.sin(theta_rad)
    restoring_mag = 0.2
    ax1.annotate('', xy=(bob_x - restoring_mag * tangent_x, bob_y - restoring_mag * tangent_y),
                 xytext=(bob_x, bob_y),
                 arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    ax1.text(bob_x - 0.35, bob_y + 0.05, r'$-mg\sin\theta$', fontsize=10, color='blue')

    # Length label
    ax1.text(-0.15, -0.5, r'$L$', fontsize=12)

    ax1.set_xlim(-0.8, 0.8)
    ax1.set_ylim(-1.4, 0.2)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('Forces on Pendulum', fontsize=10)

    # Right panel: Period formula and key relationship
    ax2.text(0.5, 0.85, 'Simple Harmonic Motion', fontsize=11,
             ha='center', fontweight='bold', transform=ax2.transAxes)

    ax2.text(0.5, 0.65, r'$\frac{d^2\theta}{dt^2} = -\frac{g}{L}\theta$',
             fontsize=14, ha='center', transform=ax2.transAxes)

    ax2.text(0.5, 0.45, 'Period:', fontsize=10,
             ha='center', transform=ax2.transAxes)

    ax2.text(0.5, 0.25, r'$T = 2\pi\sqrt{\frac{L}{g}}$',
             fontsize=16, ha='center', transform=ax2.transAxes,
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#e6f3ff',
                       edgecolor='#1f77b4'))

    ax2.text(0.5, 0.05, 'Independent of mass and amplitude\n(for small angles)',
             fontsize=9, ha='center', transform=ax2.transAxes, style='italic')

    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')

    plt.tight_layout()
    save_figure(fig, 'pendulum-physics', chapter=6)


def temperature_error():
    """Show how thermal expansion accumulates into clock error over a day.
    """
    setup_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.5))

    # Left: Temperature change vs daily error for brass pendulum
    delta_T = np.linspace(0, 20, 100)  # Temperature change in Celsius
    alpha_brass = 19e-6  # /C
    L0 = 1.0  # meter

    # Fractional period change = 0.5 * fractional length change
    frac_period_change = 0.5 * alpha_brass * delta_T

    # Daily error = frac_period_change * 86400 seconds
    daily_error = frac_period_change * 86400

    ax1.plot(delta_T, daily_error, 'b-', linewidth=1.5)
    ax1.fill_between(delta_T, 0, daily_error, alpha=0.2)

    # Mark typical indoor temperature swing
    ax1.axvline(x=10, color='red', linestyle='--', linewidth=1, alpha=0.7)
    ax1.text(10.5, 6, '10C swing:\n8 seconds/day', fontsize=8, color='red')

    ax1.set_xlabel('Temperature change (C)')
    ax1.set_ylabel('Daily error (seconds)')
    ax1.set_title('Brass Pendulum', fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 20)
    ax1.set_ylim(0, 18)

    # Right: Compare brass vs compensated pendulum
    metals = ['Brass\n(uncompensated)', 'Gridiron\n(brass+steel)', 'Mercury\n(Graham)']
    errors = [8, 0.5, 0.1]  # seconds per day for 10C swing
    colors = ['#d62728', '#ff7f0e', '#2ca02c']

    bars = ax2.bar(metals, errors, color=colors, edgecolor='black', linewidth=0.5)

    # Add value labels
    for bar, err in zip(bars, errors):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, height + 0.3,
                 f'{err}s', ha='center', fontsize=9)

    ax2.set_ylabel('Daily error (seconds)')
    ax2.set_title('Compensation Methods\n(10C temperature swing)', fontsize=10)
    ax2.set_ylim(0, 10)
    ax2.grid(True, axis='y', alpha=0.3)

    plt.tight_layout()
    save_figure(fig, 'temperature-error', chapter=6)


def gravity_latitude():
    """Show how gravitational acceleration varies with latitude.
    """
    setup_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.5))

    # Left: g vs latitude
    latitude = np.linspace(0, 90, 100)
    lat_rad = np.radians(latitude)

    # Approximate formula for g variation
    # g(phi) = g_eq * (1 + 0.00193 * sin^2(phi))
    g_eq = 9.7803
    g = g_eq * (1 + 0.00193 * np.sin(lat_rad)**2 + 0.00134 * np.sin(2*lat_rad)**2)

    ax1.plot(latitude, g, 'k-', linewidth=1.5)

    # Mark key locations
    locations = [(0, 9.780, 'Equator'), (18, 9.784, 'Jamaica'),
                 (51.5, 9.812, 'London'), (90, 9.832, 'Pole')]
    for lat, gval, name in locations:
        ax1.plot(lat, gval, 'o', markersize=6)
        if name == 'Jamaica':
            ax1.annotate(name, xy=(lat, gval), xytext=(lat+5, gval-0.01),
                        fontsize=8, ha='left')
        elif name == 'Equator':
            ax1.annotate(name, xy=(lat, gval), xytext=(lat+5, gval+0.005),
                        fontsize=8, ha='left')
        else:
            ax1.annotate(name, xy=(lat, gval), xytext=(lat+3, gval+0.005),
                        fontsize=8, ha='left')

    ax1.set_xlabel('Latitude (degrees)')
    ax1.set_ylabel(r'Gravitational acceleration $g$ (m/s$^2$)')
    ax1.set_title('Gravity Variation', fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(-5, 95)
    ax1.set_ylim(9.77, 9.84)

    # Right: Clock error for London clock at different latitudes
    g_london = 9.812
    latitudes = [0, 18, 30, 45, 60, 90]
    g_values = [9.780, 9.784, 9.793, 9.806, 9.819, 9.832]

    # Period change: dT/T = -0.5 * dg/g
    # Daily error = dT/T * 86400
    daily_errors = []
    for gval in g_values:
        frac_change = 0.5 * (g_london - gval) / g_london
        daily_error = frac_change * 86400
        daily_errors.append(daily_error)

    colors = ['#d62728' if e > 0 else '#2ca02c' for e in daily_errors]
    bars = ax2.barh(range(len(latitudes)), daily_errors, color=colors,
                    edgecolor='black', linewidth=0.5, height=0.6)

    ax2.set_yticks(range(len(latitudes)))
    ax2.set_yticklabels([f'{lat}N' for lat in latitudes])
    ax2.axvline(x=0, color='black', linewidth=0.8)
    ax2.set_xlabel('Daily error (seconds)')
    ax2.set_ylabel('Latitude')
    ax2.set_title('London Clock at Other Latitudes', fontsize=10)
    ax2.grid(True, axis='x', alpha=0.3)

    # Add annotation
    ax2.text(70, 0.8, 'Clock\nloses time', fontsize=8, color='#d62728', ha='center')
    ax2.text(-55, 4.8, 'Clock\ngains time', fontsize=8, color='#2ca02c', ha='center')

    plt.tight_layout()
    save_figure(fig, 'gravity-latitude', chapter=6)


def ship_motion():
    """Show how ship acceleration affects effective gravity and pendulum behavior.
    """
    setup_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 4))

    # Left: Vector diagram of effective gravity
    ax1.set_xlim(-1.5, 1.5)
    ax1.set_ylim(-1.5, 0.5)

    # Ship acceleration (forward)
    a_ship = 0.5  # m/s^2 (normalized for display)
    g = 1.0  # normalized gravity

    # Draw ship deck (tilted slightly to show it's a ship)
    deck_y = -1.2
    ax1.plot([-1.3, 1.3], [deck_y, deck_y], 'k-', linewidth=3)
    ax1.text(0, deck_y - 0.15, 'Ship deck', fontsize=8, ha='center')

    # Pendulum pivot
    pivot_x, pivot_y = 0, 0

    # True gravity vector (down)
    ax1.annotate('', xy=(0, -g), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='blue', lw=2.5))
    ax1.text(0.1, -0.5, r'$\vec{g}$', fontsize=12, color='blue')

    # Ship acceleration (forward, but fictitious force is backward)
    a_scale = 0.4
    ax1.annotate('', xy=(-a_scale, 0), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='red', lw=2.5))
    ax1.text(-a_scale/2, 0.15, r'$-\vec{a}_{ship}$', fontsize=11, color='red')

    # Effective gravity (vector sum)
    g_eff_x = -a_scale
    g_eff_y = -g
    ax1.annotate('', xy=(g_eff_x, g_eff_y), xytext=(0, 0),
                 arrowprops=dict(arrowstyle='->', color='green', lw=2.5))
    ax1.text(g_eff_x - 0.2, g_eff_y/2, r'$\vec{g}_{eff}$', fontsize=12, color='green')

    # Draw angle of tilt
    arc_radius = 0.3
    tilt_angle = np.degrees(np.arctan(a_scale / g))
    arc = Arc((0, 0), 2*arc_radius, 2*arc_radius,
              angle=-90, theta1=0, theta2=tilt_angle,
              color='gray', linewidth=1)
    ax1.add_patch(arc)
    ax1.text(0.05, -0.4, r'$\alpha$', fontsize=10, color='gray')

    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('Effective Gravity', fontsize=10)

    # Right: Pendulum behavior in different conditions
    conditions = ['Stationary\n(laboratory)', 'Calm sea\n(gentle roll)',
                  'Moderate swell', 'Heavy seas']
    stability = [100, 60, 20, 5]  # relative stability (arbitrary units)
    colors = ['#2ca02c', '#90EE90', '#ff7f0e', '#d62728']

    bars = ax2.barh(conditions, stability, color=colors, edgecolor='black',
                    linewidth=0.5, height=0.6)

    ax2.set_xlabel('Pendulum stability (arbitrary units)')
    ax2.set_title('Why Pendulums Fail at Sea', fontsize=10)
    ax2.set_xlim(0, 110)
    ax2.grid(True, axis='x', alpha=0.3)

    # Annotation
    ax2.text(50, -0.5, 'Effective gravity direction changes constantly at sea',
             fontsize=8, style='italic', ha='center', transform=ax2.get_xaxis_transform())

    plt.tight_layout()
    save_figure(fig, 'ship-motion', chapter=6)


if __name__ == "__main__":
    pendulum_physics()
    temperature_error()
    gravity_latitude()
    ship_motion()
