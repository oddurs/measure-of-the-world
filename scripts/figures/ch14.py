#!/usr/bin/env python3
"""Generate figures for Chapter 14: The Great Equatorial and Spectroscopy."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Wedge, Arc, FancyArrowPatch
import numpy as np


def chromatic_aberration():
    """Diagram showing chromatic aberration in a simple lens.

    Different wavelengths focus at different distances.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 4))

    # Simple lens (vertical line with curves)
    lens_x = 0
    lens_height = 1.5

    # Lens shape (simplified as vertical line with thicker center)
    ax.plot([lens_x, lens_x], [-lens_height, lens_height], 'k-', linewidth=4)

    # Incoming parallel rays (white light)
    for y in [0.8, 0, -0.8]:
        ax.annotate('', xy=(lens_x - 0.1, y), xytext=(-3, y),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))

    # Focused rays - different colors focus at different distances
    colors_data = [
        ('blue', '#0000FF', 2.5, 0.15),   # Blue focuses closest
        ('green', '#00AA00', 3.0, 0.1),   # Green in middle
        ('red', '#FF0000', 3.5, 0.05),    # Red focuses furthest
    ]

    for name, color, focus_x, offset in colors_data:
        # Rays from top of lens
        ax.plot([lens_x, focus_x], [0.8, 0], '-', color=color, linewidth=1.5, alpha=0.7)
        ax.plot([lens_x, focus_x], [-0.8, 0], '-', color=color, linewidth=1.5, alpha=0.7)
        ax.plot([lens_x, focus_x], [0, 0], '-', color=color, linewidth=1, alpha=0.5)

        # Focus point
        ax.plot(focus_x, 0, 'o', color=color, markersize=8)

    # Labels for focal points
    ax.annotate('Blue\nfocus', xy=(2.5, 0), xytext=(2.5, -1),
                fontsize=8, ha='center', color='blue',
                arrowprops=dict(arrowstyle='->', color='blue', lw=0.8))
    ax.annotate('Red\nfocus', xy=(3.5, 0), xytext=(3.5, -1),
                fontsize=8, ha='center', color='red',
                arrowprops=dict(arrowstyle='->', color='red', lw=0.8))

    # Optical axis
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.5)

    # Labels
    ax.text(-2, 1.3, 'White\nlight', fontsize=9, ha='center')
    ax.text(0, 1.7, 'Simple\nlens', fontsize=9, ha='center')

    # Distance annotation
    ax.annotate('', xy=(3.5, 0.5), xytext=(2.5, 0.5),
                arrowprops=dict(arrowstyle='<->', color='black', lw=1.5))
    ax.text(3.0, 0.7, 'Chromatic\naberration', fontsize=8, ha='center')

    ax.set_xlim(-3.5, 4.5)
    ax.set_ylim(-1.8, 2)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'chromatic-aberration', chapter=14)


def achromatic_doublet():
    """Diagram of an achromatic doublet lens.

    Crown glass + flint glass combination corrects chromatic aberration.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 4))

    # Two-element lens
    lens_x = 0

    # Crown glass (positive, larger)
    crown = mpatches.FancyBboxPatch((-0.15, -1.2), 0.3, 2.4,
                                     boxstyle="round,pad=0,rounding_size=0.1",
                                     facecolor='#87CEEB', edgecolor='black',
                                     linewidth=1.5, alpha=0.7)
    ax.add_patch(crown)
    ax.text(0, 1.5, 'Crown\nglass', fontsize=8, ha='center', color='#4169E1')

    # Flint glass (negative, thinner)
    flint = mpatches.FancyBboxPatch((0.15, -1.0), 0.15, 2.0,
                                     boxstyle="round,pad=0,rounding_size=0.05",
                                     facecolor='#DDA0DD', edgecolor='black',
                                     linewidth=1.5, alpha=0.7)
    ax.add_patch(flint)
    ax.text(0.35, 1.3, 'Flint\nglass', fontsize=8, ha='left', color='#8B008B')

    # Incoming parallel rays
    for y in [0.8, 0, -0.8]:
        ax.annotate('', xy=(-0.2, y), xytext=(-3, y),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))

    # Corrected focus - all colors meet at same point
    focus_x = 3.0
    colors = [('#0000FF', 0.85), ('#00AA00', 0.8), ('#FF0000', 0.75)]

    for color, y_start in colors:
        ax.plot([0.3, focus_x], [y_start, 0], '-', color=color,
                linewidth=1.5, alpha=0.7)
        ax.plot([0.3, focus_x], [-y_start, 0], '-', color=color,
                linewidth=1.5, alpha=0.7)

    # Common focus point
    ax.plot(focus_x, 0, 'ko', markersize=10)
    ax.text(focus_x, -0.4, 'Common\nfocus', fontsize=9, ha='center')

    # Optical axis
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.5)

    # Labels
    ax.text(-2, 1.0, 'White\nlight', fontsize=9, ha='center')

    # Annotation box
    ax.text(1.5, -1.5, 'Achromatic doublet:\nCrown + Flint glass\nbrings R and B to same focus',
            fontsize=8, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-3.5, 4)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'achromatic-doublet', chapter=14)


def equatorial_mount():
    """Diagram of an equatorial telescope mount.

    Shows polar axis and declination axis.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 6))

    # Ground
    ax.axhline(0, color='#8B4513', linewidth=3)
    ax.fill_between([-3, 3], [-0.5, -0.5], [0, 0], color='#D2B48C', alpha=0.5)

    # Pier
    pier = mpatches.Rectangle((-0.3, 0), 0.6, 1.5,
                               facecolor='gray', edgecolor='black',
                               linewidth=1.5)
    ax.add_patch(pier)
    ax.text(0, 0.75, 'Pier', fontsize=8, ha='center', color='white')

    # Polar axis (tilted to latitude angle, ~51.5 degrees for Greenwich)
    lat = 51.5
    polar_length = 2.5
    polar_end_x = polar_length * np.sin(np.radians(lat))
    polar_end_y = 1.5 + polar_length * np.cos(np.radians(lat))

    ax.plot([0, polar_end_x], [1.5, polar_end_y], 'b-', linewidth=6)
    ax.text(polar_end_x + 0.3, polar_end_y, 'Polar axis\n(points to NCP)',
            fontsize=8, ha='left', color='blue')

    # Declination axis (perpendicular to polar axis)
    dec_length = 1.2
    dec_angle = lat + 90  # perpendicular
    dec_mid_x = 0.5 * polar_end_x
    dec_mid_y = 1.5 + 0.5 * (polar_end_y - 1.5)

    dec_x1 = dec_mid_x + dec_length * np.sin(np.radians(dec_angle))
    dec_y1 = dec_mid_y + dec_length * np.cos(np.radians(dec_angle))
    dec_x2 = dec_mid_x - dec_length * np.sin(np.radians(dec_angle))
    dec_y2 = dec_mid_y - dec_length * np.cos(np.radians(dec_angle))

    ax.plot([dec_x1, dec_x2], [dec_y1, dec_y2], 'r-', linewidth=4)
    ax.text(dec_x1 + 0.2, dec_y1 + 0.2, 'Dec axis', fontsize=8, color='red')

    # Telescope tube
    tube_angle = lat - 20  # pointing slightly away from pole
    tube_length = 1.8
    tube_end_x = dec_mid_x + tube_length * np.sin(np.radians(tube_angle))
    tube_end_y = dec_mid_y + tube_length * np.cos(np.radians(tube_angle))

    ax.plot([dec_mid_x, tube_end_x], [dec_mid_y, tube_end_y],
            color='#8B4513', linewidth=8, solid_capstyle='round')
    ax.text(tube_end_x + 0.3, tube_end_y, 'Telescope', fontsize=8)

    # Counterweight
    cw_x = dec_mid_x - 0.8 * np.sin(np.radians(tube_angle))
    cw_y = dec_mid_y - 0.8 * np.cos(np.radians(tube_angle))
    cw = Circle((cw_x, cw_y), 0.25, facecolor='gray', edgecolor='black')
    ax.add_patch(cw)
    ax.text(cw_x - 0.4, cw_y, 'Weight', fontsize=7, ha='right')

    # Celestial pole indicator
    ax.annotate('', xy=(polar_end_x + 0.5, polar_end_y + 0.3),
                xytext=(polar_end_x, polar_end_y),
                arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))
    ax.plot(polar_end_x + 0.5, polar_end_y + 0.3, '*', color='gold',
            markersize=10, markeredgecolor='black')
    ax.text(polar_end_x + 0.8, polar_end_y + 0.5, 'Polaris', fontsize=7)

    # Rotation arrows
    # Polar axis rotation (RA tracking)
    arc1 = Arc((dec_mid_x, dec_mid_y), 0.8, 0.8, angle=lat-90,
               theta1=-30, theta2=30, color='blue', lw=2)
    ax.add_patch(arc1)

    # Latitude angle
    ax.annotate('', xy=(0.8, 1.5 + 0.8), xytext=(0, 1.5),
                arrowprops=dict(arrowstyle='-', color='green', lw=1,
                               connectionstyle='arc3,rad=0.2'))
    ax.text(0.5, 1.7, r'$\phi = 51.5^\circ$', fontsize=8, color='green')

    # Horizon line
    ax.text(2.5, 0.1, 'Horizon', fontsize=8, ha='right')

    ax.set_xlim(-2, 4)
    ax.set_ylim(-0.8, 5.5)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'equatorial-mount', chapter=14)


def spectroscope_prism():
    """Diagram of a prism spectroscope.

    Shows dispersion of white light into spectrum.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 4))

    # Prism (triangle)
    prism_x = [0, 1.5, 0.75]
    prism_y = [0, 0, 1.3]
    prism = plt.Polygon(list(zip(prism_x, prism_y)), facecolor='#E0E0E0',
                        edgecolor='black', linewidth=2, alpha=0.7)
    ax.add_patch(prism)
    ax.text(0.75, 0.4, 'Prism', fontsize=9, ha='center')

    # Incoming white light (from slit)
    ax.annotate('', xy=(0.2, 0.6), xytext=(-1.5, 0.6),
                arrowprops=dict(arrowstyle='->', color='gray', lw=2))
    ax.text(-1.5, 0.8, 'White light\n(from star)', fontsize=8, ha='center')

    # Slit
    ax.plot([-1.2, -1.2], [0.5, 0.7], 'k-', linewidth=3)
    ax.text(-1.2, 0.35, 'Slit', fontsize=7, ha='center')

    # Dispersed rays (spectrum)
    colors = [
        ('#8B00FF', 50, 'Violet'),
        ('#0000FF', 45, 'Blue'),
        ('#00FF00', 40, 'Green'),
        ('#FFFF00', 35, 'Yellow'),
        ('#FF0000', 30, 'Red'),
    ]

    for color, angle, name in colors:
        end_x = 1.3 + 2 * np.cos(np.radians(angle))
        end_y = 0.4 + 2 * np.sin(np.radians(angle))
        ax.plot([1.3, end_x], [0.4, end_y], '-', color=color, linewidth=2)

    # Spectrum band
    spectrum_x = 3.2
    for i, (color, angle, name) in enumerate(colors):
        y = 0.5 + i * 0.3
        ax.fill([spectrum_x, spectrum_x + 0.3, spectrum_x + 0.3, spectrum_x],
                [y - 0.12, y - 0.12, y + 0.12, y + 0.12],
                color=color)

    ax.text(spectrum_x + 0.5, 1.0, 'Spectrum', fontsize=9, ha='left')

    # Eyepiece
    ax.plot([3.5, 3.5], [0.3, 2.0], 'k-', linewidth=3)
    ax.text(3.7, 1.2, 'Eyepiece', fontsize=8, ha='left')

    ax.set_xlim(-2, 4.5)
    ax.set_ylim(-0.5, 2.5)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'spectroscope-prism', chapter=14)


def emission_absorption():
    """Comparison of emission and absorption spectra.

    Shows the relationship between the two types.
    """
    setup_style()
    fig, axes = plt.subplots(3, 1, figsize=(7, 4), height_ratios=[1, 1, 1])

    wavelengths = np.linspace(400, 700, 300)

    # Continuous spectrum (hot source)
    ax = axes[0]
    for i, wl in enumerate(wavelengths):
        color = wavelength_to_rgb(wl)
        ax.axvline(wl, color=color, linewidth=1.2)
    ax.set_xlim(400, 700)
    ax.set_ylabel('Continuous', fontsize=9)
    ax.text(350, 0.5, '(hot solid)', fontsize=8, ha='right', va='center',
            transform=ax.get_yaxis_transform())
    ax.set_yticks([])

    # Emission spectrum (hot gas)
    ax = axes[1]
    ax.set_facecolor('black')
    emission_lines = [434, 486, 518, 589, 656]  # H-gamma, H-beta, Mg, Na, H-alpha
    for line in emission_lines:
        color = wavelength_to_rgb(line)
        ax.axvline(line, color=color, linewidth=3)
    ax.set_xlim(400, 700)
    ax.set_ylabel('Emission', fontsize=9)
    ax.text(350, 0.5, '(hot gas)', fontsize=8, ha='right', va='center',
            transform=ax.get_yaxis_transform())
    ax.set_yticks([])

    # Absorption spectrum (cool gas in front of hot source)
    ax = axes[2]
    for i, wl in enumerate(wavelengths):
        color = wavelength_to_rgb(wl)
        ax.axvline(wl, color=color, linewidth=1.2)
    # Dark lines at same positions
    for line in emission_lines:
        ax.axvline(line, color='black', linewidth=3)
    ax.set_xlim(400, 700)
    ax.set_ylabel('Absorption', fontsize=9)
    ax.text(350, 0.5, '(cool gas)', fontsize=8, ha='right', va='center',
            transform=ax.get_yaxis_transform())
    ax.set_yticks([])
    ax.set_xlabel('Wavelength (nm)', fontsize=9)

    plt.tight_layout()
    save_figure(fig, 'emission-absorption', chapter=14)


def wavelength_to_rgb(wavelength):
    """Convert wavelength in nm to RGB color."""
    if wavelength < 380:
        return (0, 0, 0)
    elif wavelength < 440:
        r = -(wavelength - 440) / (440 - 380)
        g = 0.0
        b = 1.0
    elif wavelength < 490:
        r = 0.0
        g = (wavelength - 440) / (490 - 440)
        b = 1.0
    elif wavelength < 510:
        r = 0.0
        g = 1.0
        b = -(wavelength - 510) / (510 - 490)
    elif wavelength < 580:
        r = (wavelength - 510) / (580 - 510)
        g = 1.0
        b = 0.0
    elif wavelength < 645:
        r = 1.0
        g = -(wavelength - 645) / (645 - 580)
        b = 0.0
    elif wavelength < 780:
        r = 1.0
        g = 0.0
        b = 0.0
    else:
        return (0, 0, 0)

    return (r, g, b)


def doppler_shift():
    """Diagram showing the Doppler shift of spectral lines.

    Blue shift for approaching, red shift for receding.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 4))

    # Reference spectrum (at rest)
    y_rest = 2
    ax.axhline(y_rest, color='gray', linewidth=0.5, xmin=0.1, xmax=0.9)

    # Spectral lines at rest
    rest_lines = [450, 500, 550, 600, 656]
    for line in rest_lines:
        ax.plot([line, line], [y_rest - 0.15, y_rest + 0.15], 'k-', linewidth=2)

    ax.text(400, y_rest, 'At rest', fontsize=9, ha='center', va='center')

    # Blue-shifted spectrum (approaching)
    y_blue = 3
    shift_blue = -15
    ax.axhline(y_blue, color='gray', linewidth=0.5, xmin=0.1, xmax=0.9)

    for line in rest_lines:
        ax.plot([line + shift_blue, line + shift_blue],
                [y_blue - 0.15, y_blue + 0.15], 'b-', linewidth=2)
        # Arrow showing shift
        if line == 550:
            ax.annotate('', xy=(line + shift_blue, y_blue - 0.3),
                        xytext=(line, y_rest + 0.3),
                        arrowprops=dict(arrowstyle='->', color='blue', lw=1))

    ax.text(400, y_blue, 'Approaching', fontsize=9, ha='center',
            va='center', color='blue')

    # Red-shifted spectrum (receding)
    y_red = 1
    shift_red = 20
    ax.axhline(y_red, color='gray', linewidth=0.5, xmin=0.1, xmax=0.9)

    for line in rest_lines:
        ax.plot([line + shift_red, line + shift_red],
                [y_red - 0.15, y_red + 0.15], 'r-', linewidth=2)
        # Arrow showing shift
        if line == 550:
            ax.annotate('', xy=(line + shift_red, y_red + 0.3),
                        xytext=(line, y_rest - 0.3),
                        arrowprops=dict(arrowstyle='->', color='red', lw=1))

    ax.text(400, y_red, 'Receding', fontsize=9, ha='center',
            va='center', color='red')

    # Formula
    ax.text(550, 0, r'$\Delta\lambda = \lambda_0 \frac{v_r}{c}$',
            fontsize=11, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    # Wavelength labels
    ax.set_xlabel('Wavelength (nm)', fontsize=10)
    ax.set_xlim(380, 720)
    ax.set_ylim(-0.5, 3.8)
    ax.set_yticks([])

    save_figure(fig, 'doppler-shift', chapter=14)


def diffraction_grating():
    """Diagram showing diffraction grating principle.

    Parallel grooves produce interference pattern.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 4))

    # Grating (vertical line with grooves)
    grating_x = 0
    n_grooves = 8
    groove_spacing = 0.3

    for i in range(n_grooves):
        y = (i - n_grooves/2 + 0.5) * groove_spacing
        ax.plot([grating_x - 0.1, grating_x + 0.1], [y, y], 'k-', linewidth=2)

    ax.text(0, 1.5, 'Diffraction\ngrating', fontsize=9, ha='center')

    # Incoming light (normal incidence)
    for i in range(3):
        y = (i - 1) * groove_spacing
        ax.annotate('', xy=(grating_x - 0.15, y), xytext=(-2, y),
                    arrowprops=dict(arrowstyle='->', color='gray', lw=1.5))

    ax.text(-1.5, 0.8, 'Incident\nlight', fontsize=8, ha='center')

    # Diffracted orders
    orders = [
        (0, 0, 'black', 'm=0'),
        (1, 25, 'blue', 'm=1'),
        (-1, -25, 'blue', 'm=-1'),
        (2, 55, 'red', 'm=2 (red)'),
    ]

    for m, angle, color, label in orders:
        length = 2
        end_x = grating_x + length * np.cos(np.radians(90 - angle))
        end_y = length * np.sin(np.radians(90 - angle)) * np.sign(angle) if angle != 0 else 0

        # Multiple rays from grating
        for i in range(-2, 3):
            y_start = i * groove_spacing * 0.5
            ax.plot([grating_x + 0.1, end_x], [y_start, end_y + y_start * 0.3],
                    '-', color=color, linewidth=1, alpha=0.6)

        ax.text(end_x + 0.2, end_y, label, fontsize=8, ha='left', color=color)

    # Grating equation
    ax.text(1.5, -1.5, r'$d \sin\theta = m\lambda$',
            fontsize=11, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    # d label
    ax.annotate('', xy=(0.2, groove_spacing * 1.5), xytext=(0.2, groove_spacing * 0.5),
                arrowprops=dict(arrowstyle='<->', color='green', lw=1.5))
    ax.text(0.35, groove_spacing, 'd', fontsize=10, color='green')

    ax.set_xlim(-2.5, 3)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'diffraction-grating', chapter=14)


if __name__ == "__main__":
    chromatic_aberration()
    achromatic_doublet()
    equatorial_mount()
    spectroscope_prism()
    emission_absorption()
    doppler_shift()
    diffraction_grating()
