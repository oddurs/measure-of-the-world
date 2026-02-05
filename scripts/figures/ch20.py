#!/usr/bin/env python3
"""Generate figures for Chapter 20: Telescope Optics and Mountings."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Arc, Wedge, Ellipse
import numpy as np


def chromatic_aberration():
    """Diagram showing chromatic aberration in a simple lens."""
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 4))

    # Lens
    lens_x = 2
    lens_height = 2
    ax.plot([lens_x, lens_x], [-lens_height/2, lens_height/2], 'b-', linewidth=4)

    # Lens curves (simplified)
    theta = np.linspace(-np.pi/6, np.pi/6, 20)
    curve_r = 4
    ax.plot(lens_x - 0.1 + curve_r - curve_r*np.cos(theta),
            curve_r*np.sin(theta), 'b-', linewidth=2)
    ax.plot(lens_x + 0.1 - curve_r + curve_r*np.cos(theta),
            curve_r*np.sin(theta), 'b-', linewidth=2)

    ax.text(lens_x, -1.3, 'Single lens', fontsize=9, ha='center')

    # Incoming parallel rays (white light)
    for y in [-0.6, 0, 0.6]:
        ax.annotate('', xy=(lens_x - 0.1, y), xytext=(0, y),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))

    ax.text(0.5, 1, 'White light', fontsize=8, ha='center', color='gray')

    # Blue rays (focus closer)
    blue_focus = 4.5
    for y in [-0.6, 0, 0.6]:
        ax.plot([lens_x + 0.1, blue_focus], [y, 0], 'b-', linewidth=1.5, alpha=0.7)
    ax.plot(blue_focus, 0, 'bo', markersize=8)
    ax.text(blue_focus, 0.3, 'Blue focus', fontsize=7, ha='center', color='blue')

    # Red rays (focus farther)
    red_focus = 5.5
    for y in [-0.6, 0, 0.6]:
        ax.plot([lens_x + 0.1, red_focus], [y, 0], 'r-', linewidth=1.5, alpha=0.7)
    ax.plot(red_focus, 0, 'ro', markersize=8)
    ax.text(red_focus, -0.3, 'Red focus', fontsize=7, ha='center', color='red')

    # Distance annotation
    ax.annotate('', xy=(red_focus, -0.8), xytext=(blue_focus, -0.8),
                arrowprops=dict(arrowstyle='<->', color='green', lw=2))
    ax.text((blue_focus + red_focus)/2, -1.1, r'$\Delta f$ (blur)',
            fontsize=9, ha='center', color='green')

    # Equation
    ax.text(4, 1.5, r'$n(\lambda) = A + \frac{B}{\lambda^2}$',
            fontsize=10, ha='center')
    ax.text(4, 1, 'Blue bends more than red', fontsize=8, ha='center', color='gray')

    ax.set_xlim(-0.5, 7)
    ax.set_ylim(-1.8, 2)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'chromatic-aberration', chapter=20)


def achromatic_doublet():
    """How crown + flint glass corrects chromatic aberration."""
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 4))

    # Crown lens (converging)
    crown_x = 1.8
    lens_height = 1.8
    ax.fill([crown_x - 0.15, crown_x + 0.1, crown_x + 0.1, crown_x - 0.15],
            [-lens_height/2, -lens_height/2 * 0.9, lens_height/2 * 0.9, lens_height/2],
            color='#87CEEB', alpha=0.7, edgecolor='black', linewidth=1)
    ax.text(crown_x, -1.2, 'Crown\n(converging)', fontsize=7, ha='center', color='#4682B4')

    # Flint lens (diverging)
    flint_x = 2.2
    ax.fill([flint_x - 0.1, flint_x + 0.15, flint_x + 0.15, flint_x - 0.1],
            [-lens_height/2 * 0.9, -lens_height/2, lens_height/2, lens_height/2 * 0.9],
            color='#DDA0DD', alpha=0.7, edgecolor='black', linewidth=1)
    ax.text(flint_x, -1.2, 'Flint\n(diverging)', fontsize=7, ha='center', color='#8B008B')

    # Incoming parallel rays
    for y in [-0.5, 0, 0.5]:
        ax.annotate('', xy=(crown_x - 0.2, y), xytext=(0, y),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))

    ax.text(0.5, 1, 'White light', fontsize=8, ha='center', color='gray')

    # All colors focus at same point
    focus_x = 5
    colors = ['blue', 'green', 'red']
    for y, color in zip([-0.5, 0, 0.5], colors):
        ax.plot([flint_x + 0.2, focus_x], [y, 0], '-', color=color,
                linewidth=1.5, alpha=0.7)

    # Single focus point
    ax.plot(focus_x, 0, 'ko', markersize=10)
    ax.text(focus_x, 0.4, 'Common\nfocus', fontsize=8, ha='center', fontweight='bold')

    # Explanation
    ax.text(3.5, -1.5, 'Crown dispersion + Flint dispersion = 0\n'
            'Net power = converging (positive)',
            fontsize=8, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-2, 1.8)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'achromatic-doublet', chapter=20)


def reflector_design():
    """Newton's reflecting telescope design."""
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 5))

    # Tube
    tube_length = 5
    tube_width = 1.5
    ax.add_patch(Rectangle((0, -tube_width/2), tube_length, tube_width,
                            fill=False, edgecolor='black', linewidth=2))

    # Primary mirror (parabolic, at back)
    mirror_x = 0.3
    theta = np.linspace(-0.6, 0.6, 30)
    mirror_y = theta
    mirror_curve = 0.1 * theta**2  # parabola
    ax.fill(mirror_x + mirror_curve, mirror_y, color='#C0C0C0', edgecolor='black',
            linewidth=2)
    ax.text(0.1, -1, 'Primary mirror\n(parabolic)', fontsize=8, ha='center')

    # Secondary mirror (flat, angled)
    sec_x, sec_y = 4, 0
    sec_size = 0.25
    angle = 45
    ax.add_patch(Rectangle((sec_x - sec_size/2, sec_y - sec_size*0.7),
                            sec_size, sec_size*1.4,
                            angle=angle, facecolor='#C0C0C0',
                            edgecolor='black', linewidth=1.5))
    ax.text(sec_x + 0.5, sec_y + 0.5, 'Secondary\n(flat)', fontsize=7, ha='left')

    # Incoming parallel rays
    for y in [-0.4, 0, 0.4]:
        ax.annotate('', xy=(tube_length - 0.2, y), xytext=(tube_length + 1, y),
                    arrowprops=dict(arrowstyle='<-', color='orange', lw=1.5))

    ax.text(tube_length + 0.5, 0.8, 'Starlight', fontsize=8, ha='center', color='orange')

    # Rays to primary
    for y in [-0.4, 0, 0.4]:
        ax.plot([tube_length - 0.2, mirror_x + 0.1], [y, y], 'r-', linewidth=1, alpha=0.7)

    # Rays from primary to secondary
    for y in [-0.4, 0, 0.4]:
        ax.plot([mirror_x + 0.1, sec_x], [y, 0], 'r-', linewidth=1, alpha=0.7)

    # Rays from secondary to eyepiece
    eyepiece_y = tube_width/2 + 0.5
    ax.plot([sec_x, sec_x], [0, eyepiece_y], 'r-', linewidth=1.5, alpha=0.7)

    # Eyepiece
    ax.add_patch(Rectangle((sec_x - 0.15, eyepiece_y), 0.3, 0.3,
                            facecolor='#4682B4', edgecolor='black', linewidth=1))
    ax.text(sec_x, eyepiece_y + 0.5, 'Eyepiece', fontsize=8, ha='center')

    # Eye
    ax.plot(sec_x, eyepiece_y + 0.7, 'ko', markersize=8)
    ax.text(sec_x + 0.3, eyepiece_y + 0.7, 'Observer', fontsize=7, ha='left')

    # Focus point
    ax.plot(sec_x, 0, 'g*', markersize=10)
    ax.text(sec_x - 0.3, -0.3, 'Focus', fontsize=7, ha='right', color='green')

    # Note
    ax.text(2.5, -1.3, 'No chromatic aberration:\nmirrors reflect all wavelengths equally',
            fontsize=8, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-0.5, 7)
    ax.set_ylim(-1.8, 2)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'reflector-design', chapter=20)


def optical_aberrations():
    """Common optical aberrations: spherical, coma, astigmatism."""
    setup_style()
    fig, axes = plt.subplots(1, 3, figsize=(9, 3))

    # Spherical aberration
    ax = axes[0]
    ax.set_title('Spherical\nAberration', fontsize=9)

    # Lens
    ax.plot([0, 0], [-1, 1], 'b-', linewidth=3)

    # Rays at different heights focus at different points
    for y, focus in [(-0.8, 1.5), (-0.4, 1.8), (0, 2), (0.4, 1.8), (0.8, 1.5)]:
        ax.plot([0, focus], [y, 0], 'r-', linewidth=1, alpha=0.7)

    ax.text(1.5, -0.8, 'Edge rays\nfocus closer', fontsize=7, ha='center')
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-1.2, 1.2)
    ax.axis('off')

    # Coma
    ax = axes[1]
    ax.set_title('Coma', fontsize=9)

    # Perfect point (on axis)
    ax.plot(1.5, 0, 'go', markersize=6)

    # Comatic image (off axis) - comet shape
    theta = np.linspace(0, 2*np.pi, 50)
    r = 0.3 * (1 + 0.5 * np.cos(theta))
    ax.fill(1.5 + r * np.cos(theta) + 0.2,
            0.8 + r * np.sin(theta) * 0.5,
            color='red', alpha=0.5)
    ax.plot(1.5, 0.8, 'ro', markersize=4)

    ax.annotate('', xy=(1.5, 0.5), xytext=(1.5, 0.2),
                arrowprops=dict(arrowstyle='->', color='gray', lw=1))
    ax.text(0.5, 0.4, 'Off-axis\npoint', fontsize=7, ha='center')
    ax.text(2.2, 0.8, 'Comet-shaped\nblur', fontsize=7, ha='left', color='red')

    ax.set_xlim(-0.2, 3)
    ax.set_ylim(-0.5, 1.5)
    ax.axis('off')

    # Astigmatism
    ax = axes[2]
    ax.set_title('Astigmatism', fontsize=9)

    # Two focal lines at different distances
    # Tangential focus
    ax.plot([1, 1.4], [0.5, 0.5], 'b-', linewidth=3)
    ax.text(1.2, 0.7, 'Tangential\nfocus', fontsize=6, ha='center', color='blue')

    # Sagittal focus
    ax.plot([1.8, 1.8], [0.3, 0.7], 'r-', linewidth=3)
    ax.text(1.8, 0.2, 'Sagittal\nfocus', fontsize=6, ha='center', color='red')

    # Best focus (circle of least confusion)
    circle = Circle((1.5, 0.5), 0.15, fill=False, edgecolor='green', linewidth=2)
    ax.add_patch(circle)
    ax.text(1.5, 0.1, 'Best focus\n(compromise)', fontsize=6, ha='center', color='green')

    ax.set_xlim(0.5, 2.5)
    ax.set_ylim(-0.3, 1.2)
    ax.axis('off')

    plt.tight_layout()
    save_figure(fig, 'optical-aberrations', chapter=20)


def mount_comparison():
    """Comparison of altazimuth and equatorial mounts."""
    setup_style()
    fig, axes = plt.subplots(1, 2, figsize=(8, 5))

    # Altazimuth mount
    ax = axes[0]
    ax.set_title('Altazimuth Mount', fontsize=10, fontweight='bold')

    # Base
    ax.add_patch(Rectangle((-1, 0), 2, 0.3, facecolor='#808080', edgecolor='black'))

    # Azimuth axis (vertical)
    ax.plot([0, 0], [0.3, 1.5], 'k-', linewidth=4)
    ax.add_patch(Circle((0, 0.3), 0.15, facecolor='#606060', edgecolor='black'))

    # Azimuth rotation arrow
    arc = Arc((0, 0.9), 1, 1, angle=0, theta1=0, theta2=90,
              color='blue', linewidth=2)
    ax.add_patch(arc)
    ax.text(0.7, 0.9, 'Azimuth', fontsize=7, color='blue')

    # Fork
    ax.plot([-0.4, -0.4], [1.5, 2.2], 'k-', linewidth=3)
    ax.plot([0.4, 0.4], [1.5, 2.2], 'k-', linewidth=3)
    ax.plot([-0.4, 0.4], [1.5, 1.5], 'k-', linewidth=3)

    # Altitude axis (horizontal)
    ax.add_patch(Circle((-0.4, 2.2), 0.1, facecolor='#606060', edgecolor='black'))
    ax.add_patch(Circle((0.4, 2.2), 0.1, facecolor='#606060', edgecolor='black'))

    # Altitude rotation arrow
    arc2 = Arc((0, 2.2), 0.8, 0.8, angle=0, theta1=45, theta2=135,
               color='red', linewidth=2)
    ax.add_patch(arc2)
    ax.text(0.1, 2.7, 'Altitude', fontsize=7, color='red')

    # Telescope tube
    tube_angle = 60
    tube_len = 1.5
    dx = tube_len * np.cos(np.radians(tube_angle))
    dy = tube_len * np.sin(np.radians(tube_angle))
    ax.plot([0, dx], [2.2, 2.2 + dy], 'k-', linewidth=6)

    # Note
    ax.text(0, -0.5, 'Both axes rotate\nField rotation occurs',
            fontsize=8, ha='center', color='gray')

    ax.set_xlim(-2, 2.5)
    ax.set_ylim(-0.8, 4)
    ax.set_aspect('equal')
    ax.axis('off')

    # Equatorial mount
    ax = axes[1]
    ax.set_title('Equatorial Mount', fontsize=10, fontweight='bold')

    # Base
    ax.add_patch(Rectangle((-1, 0), 2, 0.3, facecolor='#808080', edgecolor='black'))

    # Polar axis (tilted toward pole)
    lat = 51.5  # Greenwich latitude
    polar_len = 1.8
    ax.plot([0, polar_len * np.cos(np.radians(lat))],
            [0.3, 0.3 + polar_len * np.sin(np.radians(lat))],
            'k-', linewidth=4)

    # Polar axis label
    ax.text(1.5, 1.5, 'Polar axis\n(to celestial pole)', fontsize=7, ha='left', color='blue')

    # RA rotation arrow
    arc = Arc((0.6, 1.2), 0.8, 0.8, angle=lat, theta1=0, theta2=90,
              color='blue', linewidth=2)
    ax.add_patch(arc)
    ax.text(0.3, 0.7, 'RA', fontsize=7, color='blue')

    # Declination axis (perpendicular to polar)
    dec_x = polar_len * np.cos(np.radians(lat))
    dec_y = 0.3 + polar_len * np.sin(np.radians(lat))
    ax.add_patch(Circle((dec_x, dec_y), 0.12, facecolor='#606060', edgecolor='black'))

    # Dec rotation arrow
    arc2 = Arc((dec_x, dec_y), 0.6, 0.6, angle=0, theta1=45, theta2=135,
               color='red', linewidth=2)
    ax.add_patch(arc2)
    ax.text(dec_x + 0.4, dec_y + 0.3, 'Dec', fontsize=7, color='red')

    # Telescope tube
    tube_angle = 70
    tube_len = 1.2
    dx = tube_len * np.cos(np.radians(tube_angle))
    dy = tube_len * np.sin(np.radians(tube_angle))
    ax.plot([dec_x, dec_x + dx], [dec_y, dec_y + dy], 'k-', linewidth=6)

    # Note
    ax.text(0, -0.5, 'Polar axis tracks stars\nNo field rotation',
            fontsize=8, ha='center', color='gray')

    ax.set_xlim(-2, 3)
    ax.set_ylim(-0.8, 4)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    save_figure(fig, 'mount-comparison', chapter=20)


def telescope_evolution():
    """Evolution of telescope aperture 1668-1900."""
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 5))

    data = [
        (1668, 1, 'Newton', 'Reflector'),
        (1758, 2.5, 'Dollond', 'Refractor'),
        (1785, 40, 'Herschel', 'Reflector'),
        (1820, 9.6, 'Fraunhofer', 'Refractor'),
        (1845, 72, 'Rosse', 'Reflector'),
        (1859, 28, 'Greenwich', 'Refractor'),
        (1888, 36, 'Lick', 'Refractor'),
        (1897, 40, 'Yerkes', 'Refractor'),
        (1908, 60, 'Mt. Wilson', 'Reflector'),
    ]

    years = [d[0] for d in data]
    apertures = [d[1] for d in data]
    names = [d[2] for d in data]
    types = [d[3] for d in data]

    colors = ['red' if t == 'Reflector' else 'blue' for t in types]

    ax.scatter(years, apertures, c=colors, s=100, zorder=5)

    for year, ap, name, typ in data:
        offset = 3 if ap < 50 else -5
        ax.annotate(f'{name}\n({ap}")',
                    xy=(year, ap), xytext=(year, ap + offset),
                    fontsize=7, ha='center', va='bottom' if offset > 0 else 'top')

    ax.set_xlabel('Year', fontsize=10)
    ax.set_ylabel('Aperture (inches)', fontsize=10)
    ax.set_xlim(1650, 1920)
    ax.set_ylim(0, 80)
    ax.grid(True, alpha=0.3)

    # Legend
    ax.scatter([], [], c='red', s=80, label='Reflector')
    ax.scatter([], [], c='blue', s=80, label='Refractor')
    ax.legend(loc='upper left', fontsize=9)

    plt.tight_layout()
    save_figure(fig, 'telescope-evolution', chapter=20)


if __name__ == "__main__":
    chromatic_aberration()
    achromatic_doublet()
    reflector_design()
    optical_aberrations()
    mount_comparison()
    telescope_evolution()
