#!/usr/bin/env python3
"""Generate figures for Chapter 5: Building the Historia Coelestis Britannica."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np


def reduction_pipeline():
    """Flowchart showing the data reduction process from raw observation
    to final catalog coordinates.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 5))

    # Box positions and sizes
    box_width = 1.8
    box_height = 0.5

    # Define the pipeline stages
    stages = [
        ('Raw Observation', 0, 4, '#e6f3ff'),
        ('Clock\nCorrection', -1.5, 3, '#fff2e6'),
        ('Refraction\nCorrection', 1.5, 3, '#fff2e6'),
        ('Sidereal Time\nConversion', -1.5, 2, '#e6ffe6'),
        ('Altitude to\nDeclination', 1.5, 2, '#e6ffe6'),
        ('Precession\nCorrection', 0, 1, '#ffe6e6'),
        ('Catalog Position', 0, 0, '#e6e6ff'),
    ]

    # Draw boxes
    for label, x, y, color in stages:
        box = FancyBboxPatch((x - box_width/2, y - box_height/2),
                             box_width, box_height,
                             boxstyle="round,pad=0.05,rounding_size=0.1",
                             facecolor=color, edgecolor='black', linewidth=1)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center', fontsize=9,
                fontweight='bold' if y in [0, 4] else 'normal')

    # Draw arrows
    arrows = [
        # From raw observation
        (0, 4 - box_height/2, -1.5, 3 + box_height/2),
        (0, 4 - box_height/2, 1.5, 3 + box_height/2),
        # From corrections
        (-1.5, 3 - box_height/2, -1.5, 2 + box_height/2),
        (1.5, 3 - box_height/2, 1.5, 2 + box_height/2),
        # To precession
        (-1.5, 2 - box_height/2, 0, 1 + box_height/2),
        (1.5, 2 - box_height/2, 0, 1 + box_height/2),
        # To final
        (0, 1 - box_height/2, 0, 0 + box_height/2),
    ]

    for x1, y1, x2, y2 in arrows:
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color='black', lw=1.2))

    # Add side annotations
    ax.text(-2.8, 3, 'Time\nmeasurement', fontsize=8, ha='center', va='center',
            style='italic', color='#666666')
    ax.text(2.8, 3, 'Altitude\nmeasurement', fontsize=8, ha='center', va='center',
            style='italic', color='#666666')

    # Add output labels
    ax.text(-1.5, 1.6, r'$\alpha$ (RA)', fontsize=10, ha='center', color='#2ca02c')
    ax.text(1.5, 1.6, r'$\delta$ (Dec)', fontsize=10, ha='center', color='#2ca02c')

    ax.set_xlim(-3.5, 3.5)
    ax.set_ylim(-0.8, 4.8)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'reduction-pipeline', chapter=5)


def precession_drift():
    """Visualization of how precession shifts star positions over decades.

    Shows the systematic drift in right ascension and declination.
    """
    setup_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.5))

    # Precession rate: ~50 arcsec/year in RA, ~20 arcsec/year in Dec
    years = np.arange(1676, 1720, 1)
    base_year = 1690

    # Calculate drift from base epoch
    delta_years = years - base_year
    ra_drift = 50 * delta_years  # arcseconds
    dec_drift = 20 * np.cos(np.radians(45)) * delta_years  # simplified, for star at RA=45deg

    # Plot RA drift
    ax1.plot(years, ra_drift, 'b-', linewidth=1.5)
    ax1.axhline(y=0, color='gray', linestyle='--', linewidth=0.8)
    ax1.axvline(x=base_year, color='red', linestyle=':', linewidth=1, alpha=0.7)
    ax1.fill_between(years, ra_drift, 0, alpha=0.2)

    ax1.set_xlabel('Year')
    ax1.set_ylabel('RA drift (arcseconds)')
    ax1.set_title('Right Ascension')
    ax1.text(base_year + 1, -50, 'Catalog\nepoch', fontsize=8, color='red')
    ax1.grid(True, alpha=0.3)

    # Plot Dec drift
    ax2.plot(years, dec_drift, 'orange', linewidth=1.5)
    ax2.axhline(y=0, color='gray', linestyle='--', linewidth=0.8)
    ax2.axvline(x=base_year, color='red', linestyle=':', linewidth=1, alpha=0.7)
    ax2.fill_between(years, dec_drift, 0, alpha=0.2, color='orange')

    ax2.set_xlabel('Year')
    ax2.set_ylabel('Dec drift (arcseconds)')
    ax2.set_title('Declination')
    ax2.text(base_year + 1, -30, 'Catalog\nepoch', fontsize=8, color='red')
    ax2.grid(True, alpha=0.3)

    # Common annotation
    fig.text(0.5, 0.02, 'Precession rate: approximately 50 arcsec/year',
             ha='center', fontsize=8, style='italic')

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.18)

    save_figure(fig, 'precession-drift', chapter=5)


def error_averaging():
    """Show how averaging multiple observations reduces uncertainty.

    Demonstrates the 1/sqrt(n) improvement in precision.
    """
    setup_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.5))

    np.random.seed(42)

    # Simulate individual observations with ~15 arcsec random error
    true_position = 0  # arbitrary reference
    single_error = 15  # arcseconds
    n_obs = 30

    observations = np.random.normal(true_position, single_error, n_obs)
    obs_numbers = np.arange(1, n_obs + 1)

    # Plot individual observations
    ax1.scatter(obs_numbers, observations, s=30, alpha=0.7, c='#1f77b4',
                edgecolors='black', linewidth=0.5)
    ax1.axhline(y=true_position, color='red', linestyle='-', linewidth=1.5,
                label='True position')
    ax1.axhline(y=np.mean(observations), color='green', linestyle='--', linewidth=1.5,
                label=f'Mean (n={n_obs})')

    # Error bands
    ax1.axhspan(-single_error, single_error, alpha=0.1, color='gray')
    ax1.text(n_obs + 1, 0, r'$\pm 15$ arcsec', fontsize=8, va='center', color='gray')

    ax1.set_xlabel('Observation number')
    ax1.set_ylabel('Position error (arcseconds)')
    ax1.set_title('Individual Observations')
    ax1.legend(loc='upper right', fontsize=8)
    ax1.set_xlim(0, n_obs + 5)
    ax1.set_ylim(-45, 45)
    ax1.grid(True, alpha=0.3)

    # Plot running average and uncertainty
    running_mean = np.cumsum(observations) / obs_numbers
    running_std = np.array([np.std(observations[:i], ddof=1) / np.sqrt(i)
                           if i > 1 else single_error for i in obs_numbers])

    ax2.plot(obs_numbers, running_mean, 'g-', linewidth=1.5, label='Running mean')
    ax2.fill_between(obs_numbers, running_mean - running_std, running_mean + running_std,
                     alpha=0.3, color='green', label='Standard error')
    ax2.axhline(y=true_position, color='red', linestyle='-', linewidth=1.5)

    # Theoretical 1/sqrt(n) curve
    theoretical_error = single_error / np.sqrt(obs_numbers)
    ax2.plot(obs_numbers, theoretical_error, 'k:', linewidth=1, alpha=0.5)
    ax2.plot(obs_numbers, -theoretical_error, 'k:', linewidth=1, alpha=0.5)

    ax2.set_xlabel('Number of observations')
    ax2.set_ylabel('Position error (arcseconds)')
    ax2.set_title('Averaging Improvement')
    ax2.legend(loc='upper right', fontsize=8)
    ax2.set_xlim(0, n_obs + 2)
    ax2.set_ylim(-20, 20)
    ax2.grid(True, alpha=0.3)

    # Annotation
    ax2.text(25, -15, r'Error $\propto 1/\sqrt{n}$', fontsize=9, style='italic')

    plt.tight_layout()

    save_figure(fig, 'error-averaging', chapter=5)


if __name__ == "__main__":
    reduction_pipeline()
    precession_drift()
    error_averaging()
