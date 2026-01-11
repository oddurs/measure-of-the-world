#!/usr/bin/env python3
"""Generate figures for Chapter 1: The Deadly Ignorance of Position."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


def latitude_geometry():
    """Geometric relationship between latitude and celestial pole altitude.

    Shows a cross-section of Earth with an observer, their local horizon,
    and the direction to the celestial pole, demonstrating why pole altitude
    equals latitude.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(5, 5))

    # Parameters
    R = 1.0  # Earth radius (normalized)
    lat = 45  # Observer latitude in degrees
    lat_rad = np.radians(lat)

    # Draw Earth as a circle
    theta = np.linspace(0, 2 * np.pi, 100)
    ax.plot(R * np.cos(theta), R * np.sin(theta), 'k-', linewidth=1.5)
    ax.fill(R * np.cos(theta), R * np.sin(theta), color='#e8e8e8', alpha=0.5)

    # Observer position on Earth's surface
    obs_x = R * np.cos(lat_rad)
    obs_y = R * np.sin(lat_rad)
    ax.plot(obs_x, obs_y, 'ko', markersize=6, zorder=5)
    ax.annotate('Observer', xy=(obs_x, obs_y), xytext=(obs_x + 0.15, obs_y + 0.15),
                fontsize=9, ha='left')

    # Earth's axis (vertical line through center)
    ax.annotate('', xy=(0, 1.6), xytext=(0, -1.2),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1.2))
    ax.text(0.08, 1.5, "Earth's axis", fontsize=8, color='#555555', ha='left')

    # Celestial pole direction from observer (parallel to Earth's axis)
    pole_length = 0.9
    pole_end_x = obs_x
    pole_end_y = obs_y + pole_length
    ax.annotate('', xy=(pole_end_x, pole_end_y), xytext=(obs_x, obs_y),
                arrowprops=dict(arrowstyle='->', color='#1a1a1a', lw=1.5))
    ax.text(pole_end_x + 0.08, pole_end_y - 0.05, 'To celestial\npole',
            fontsize=8, ha='left', va='top')

    # Horizon line (tangent to Earth at observer's position)
    # Tangent is perpendicular to radius, so direction is (-sin(lat), cos(lat))
    horizon_length = 0.8
    tan_dx = -np.sin(lat_rad)
    tan_dy = np.cos(lat_rad)
    h1_x = obs_x - horizon_length * tan_dx
    h1_y = obs_y - horizon_length * tan_dy
    h2_x = obs_x + horizon_length * tan_dx
    h2_y = obs_y + horizon_length * tan_dy
    ax.plot([h1_x, h2_x], [h1_y, h2_y], 'k-', linewidth=1.2)
    ax.text(h2_x + 0.05, h2_y, 'Horizon', fontsize=8, ha='left', va='center')

    # Draw the latitude angle at Earth's center
    # Arc from equator (x-axis) to observer's radial line
    arc_radius = 0.3
    arc_theta = np.linspace(0, lat_rad, 30)
    arc_x = arc_radius * np.cos(arc_theta)
    arc_y = arc_radius * np.sin(arc_theta)
    ax.plot(arc_x, arc_y, 'k-', linewidth=1)
    ax.text(0.38, 0.12, r'$\phi$', fontsize=11, ha='center', va='center')

    # Draw radial line from center to observer
    ax.plot([0, obs_x], [0, obs_y], 'k--', linewidth=0.8, alpha=0.6)

    # Draw the pole altitude angle at observer
    # This is the angle between horizon and pole direction
    # The horizon tangent direction is (-sin(lat), cos(lat))
    # The pole direction is (0, 1)
    # The angle between them equals latitude
    arc2_radius = 0.25
    # Arc from horizon direction to vertical (pole direction)
    # Horizon direction angle from horizontal: 90 + lat degrees
    # Pole direction angle from horizontal: 90 degrees
    horizon_angle = np.pi/2 + lat_rad  # angle of horizon tangent from +x axis
    pole_angle = np.pi/2  # vertical
    # We want arc from pole direction up to horizon direction
    arc2_theta = np.linspace(pole_angle, horizon_angle, 30)
    arc2_x = obs_x + arc2_radius * np.cos(arc2_theta)
    arc2_y = obs_y + arc2_radius * np.sin(arc2_theta)
    ax.plot(arc2_x, arc2_y, 'k-', linewidth=1)

    # Label for altitude angle h (same as phi)
    label_angle = (pole_angle + horizon_angle) / 2
    label_x = obs_x + 0.35 * np.cos(label_angle)
    label_y = obs_y + 0.35 * np.sin(label_angle)
    ax.text(label_x, label_y, r'$h$', fontsize=11, ha='center', va='center')

    # Equator line
    ax.plot([-1.3, 1.3], [0, 0], 'k:', linewidth=0.8, alpha=0.5)
    ax.text(1.25, -0.1, 'Equator', fontsize=8, ha='right', va='top', alpha=0.7)

    # Center point
    ax.plot(0, 0, 'k.', markersize=3)

    # Key insight annotation
    ax.text(0, -1.55, r'$h = \phi$  (pole altitude = latitude)',
            fontsize=10, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc'))

    # Clean up axes
    ax.set_xlim(-1.5, 1.8)
    ax.set_ylim(-1.7, 1.8)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'latitude-geometry', chapter=1)


def dead_reckoning_error():
    """Cumulative error growth in dead reckoning navigation.

    Visualizes how position uncertainty accumulates over a transatlantic
    voyage, based on historical data from 17th-18th century navigation records.
    """
    setup_style()
    fig, ax = plt.subplots()

    # Data points from historical records (days, min_error_nm, max_error_nm)
    # Based on table in chapter: tab:dead-reckoning-error
    data_points = np.array([
        [0, 0, 0],
        [5, 10, 20],
        [10, 30, 50],
        [20, 60, 100],
        [30, 100, 150],
        [40, 150, 250],
    ])

    days = data_points[:, 0]
    error_min = data_points[:, 1]
    error_max = data_points[:, 2]
    error_mid = (error_min + error_max) / 2

    # Interpolate for smooth curves
    days_smooth = np.linspace(0, 45, 100)
    error_min_smooth = np.interp(days_smooth, days, error_min)
    error_max_smooth = np.interp(days_smooth, days, error_max)
    error_mid_smooth = np.interp(days_smooth, days, error_mid)

    # Plot error range as shaded region
    ax.fill_between(days_smooth, error_min_smooth, error_max_smooth,
                    alpha=0.3, color='C0', label='Typical error range')

    # Plot midpoint line
    ax.plot(days_smooth, error_mid_smooth, 'C0-', linewidth=1.5,
            label='Mean estimated error')

    # Danger threshold: 1 degree longitude at English Channel latitude (~51°N)
    # 1° longitude = 60 nm × cos(51°) ≈ 38 nm
    danger_threshold = 40  # nautical miles
    ax.axhline(y=danger_threshold, color='C3', linestyle='--', linewidth=1.2,
               label=f'Critical threshold ({danger_threshold} nm)')

    # Mark the Scilly disaster context
    ax.axvline(x=40, color='gray', linestyle=':', linewidth=0.8, alpha=0.7)
    ax.annotate('Typical Atlantic\ncrossing', xy=(40, 20), fontsize=8,
                ha='center', color='gray')

    # Labels and formatting
    ax.set_xlabel('Days at sea')
    ax.set_ylabel('Position error (nautical miles)')
    ax.set_xlim(0, 45)
    ax.set_ylim(0, 280)
    ax.legend(loc='upper left', frameon=True, fancybox=False, edgecolor='black')

    # Add grid
    ax.grid(True, alpha=0.3)

    save_figure(fig, 'dead-reckoning-error', chapter=1)


if __name__ == "__main__":
    latitude_geometry()
    dead_reckoning_error()
