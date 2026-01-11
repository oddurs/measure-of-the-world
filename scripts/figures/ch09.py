#!/usr/bin/env python3
"""Generate figures for Chapter 9: Harrison's Chronometers: H1 through H5."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Arc, Circle, Rectangle
import numpy as np


def chronometer_evolution():
    """Timeline showing the evolution of Harrison's chronometers.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 4))

    # Chronometer data
    chronometers = [
        ('H1', 1735, 'Linked balance\nGrasshopper escapement', '#1f77b4'),
        ('H2', 1739, 'Centrifugal\nforce problem', '#ff7f0e'),
        ('H3', 1757, 'Bimetallic\ncompensation', '#2ca02c'),
        ('H4', 1759, 'Watch design\nDiamond pallets', '#d62728'),
        ('H5', 1770, 'Final\nrefinement', '#9467bd'),
    ]

    # Draw timeline
    years = [c[1] for c in chronometers]
    ax.plot([1730, 1775], [0, 0], 'k-', linewidth=2)

    # Mark decades
    for year in range(1730, 1780, 10):
        ax.plot([year, year], [-0.05, 0.05], 'k-', linewidth=1)
        ax.text(year, -0.15, str(year), fontsize=8, ha='center', va='top')

    # Plot chronometers
    for i, (name, year, description, color) in enumerate(chronometers):
        y_offset = 0.4 if i % 2 == 0 else -0.4

        # Vertical line
        ax.plot([year, year], [0, y_offset * 0.8], color=color, linewidth=2)

        # Marker
        ax.plot(year, 0, 'o', color=color, markersize=10)

        # Name and description
        va = 'bottom' if y_offset > 0 else 'top'
        ax.text(year, y_offset, f'{name}\n{description}', fontsize=8,
                ha='center', va=va, color=color, fontweight='bold')

    # Development periods
    # H1-H2 development
    ax.annotate('', xy=(1739, 0.1), xytext=(1735, 0.1),
                arrowprops=dict(arrowstyle='<->', color='gray', lw=0.8))
    ax.text(1737, 0.15, '4 years', fontsize=7, ha='center', color='gray')

    # H3 long development
    ax.annotate('', xy=(1757, -0.1), xytext=(1740, -0.1),
                arrowprops=dict(arrowstyle='<->', color='gray', lw=0.8))
    ax.text(1748.5, -0.18, '18 years', fontsize=7, ha='center', color='gray')

    ax.set_xlim(1725, 1780)
    ax.set_ylim(-0.7, 0.7)
    ax.axis('off')

    save_figure(fig, 'chronometer-evolution', chapter=9)


def temperature_compensation():
    """Diagram showing how bimetallic compensation works.
    """
    setup_style()
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 4))

    # Left: Bimetallic strip behavior
    ax1.set_xlim(-0.5, 2.5)
    ax1.set_ylim(-1, 1.5)

    # Cold state (straight)
    ax1.plot([0, 1], [0.8, 0.8], 'b-', linewidth=8, alpha=0.7, label='Steel (low expansion)')
    ax1.plot([0, 1], [0.7, 0.7], 'orange', linewidth=8, alpha=0.7, label='Brass (high expansion)')
    ax1.text(0.5, 1.1, 'Cold', fontsize=9, ha='center', fontweight='bold')

    # Hot state (curved)
    theta = np.linspace(0, np.pi/3, 50)
    r = 1.5
    x_steel = 0.3 + r * np.sin(theta)
    y_steel = -0.5 + r * np.cos(theta)
    x_brass = 0.3 + (r - 0.1) * np.sin(theta)
    y_brass = -0.5 + (r - 0.1) * np.cos(theta)

    ax1.plot(x_steel, y_steel, 'b-', linewidth=8, alpha=0.7)
    ax1.plot(x_brass, y_brass, 'orange', linewidth=8, alpha=0.7)
    ax1.text(1.3, -0.3, 'Hot', fontsize=9, ha='center', fontweight='bold')

    # Arrow showing bending
    ax1.annotate('', xy=(1.5, 0.2), xytext=(1.3, 0.6),
                 arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
    ax1.text(1.7, 0.5, 'Brass expands\nmore', fontsize=7, color='red')

    ax1.legend(loc='lower left', fontsize=7)
    ax1.axis('off')
    ax1.set_title('Bimetallic Strip', fontsize=10)

    # Right: Effect on period
    temp_change = np.linspace(-30, 30, 100)

    # Uncompensated
    alpha_brass = 19e-6
    period_change_uncomp = 2.5 * alpha_brass * temp_change * 86400  # seconds/day

    # Compensated
    period_change_comp = 0.1 * alpha_brass * temp_change * 86400  # 25x reduction

    ax2.plot(temp_change, period_change_uncomp, 'r-', linewidth=1.5,
             label='Uncompensated')
    ax2.plot(temp_change, period_change_comp, 'g-', linewidth=1.5,
             label='Compensated (H4)')
    ax2.axhline(y=0, color='gray', linestyle='--', linewidth=0.8)

    ax2.set_xlabel('Temperature change (C)')
    ax2.set_ylabel('Daily rate error (seconds)')
    ax2.set_title('Temperature Effect on Rate', fontsize=10)
    ax2.legend(fontsize=8)
    ax2.grid(True, alpha=0.3)

    # Annotation
    ax2.text(20, 30, '25x\nimprovement', fontsize=8, ha='center', color='green')

    plt.tight_layout()
    save_figure(fig, 'temperature-compensation', chapter=9)


def trial_performance():
    """Bar chart comparing performance of Harrison's chronometers in trials.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 4))

    # Trial data
    trials = ['H1\nJamaica\n1735', 'H4\nJamaica\n1762', 'H4\nBarbados\n1764',
              'H5\nKing\n1772']
    errors = [54, 5.1, 39.2, 4.5]  # seconds accumulated
    durations = ['months', '81 days', '5 months', '10 weeks']
    colors = ['#1f77b4', '#d62728', '#d62728', '#9467bd']

    bars = ax.bar(trials, errors, color=colors, edgecolor='black', linewidth=0.5)

    # Target line (2 minutes = 120 seconds for 6-week voyage)
    ax.axhline(y=120, color='gray', linestyle='--', linewidth=1, alpha=0.7)
    ax.text(3.5, 125, 'Prize threshold\n(2 min for 6 weeks)', fontsize=7,
            ha='right', color='gray')

    # Value labels
    for bar, err in zip(bars, errors):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 2,
                f'{err}s', ha='center', fontsize=9, fontweight='bold')

    ax.set_ylabel('Accumulated error (seconds)')
    ax.set_title("Harrison's Chronometer Trial Results", fontsize=10)
    ax.set_ylim(0, 140)
    ax.grid(True, axis='y', alpha=0.3)

    # Annotation
    ax.text(0.5, -0.12, 'H4 Jamaica trial: 5.1s over 81 days = 0.06s/day',
            fontsize=8, style='italic', ha='center', transform=ax.transAxes)

    plt.tight_layout()
    save_figure(fig, 'trial-performance', chapter=9)


def linked_balance():
    """Diagram showing the linked balance principle.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 4))

    # Two balance wheels oscillating in anti-phase
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.5, 1.5)

    # Left wheel
    wheel1 = Circle((-0.8, 0), 0.5, fill=False, edgecolor='#1f77b4', linewidth=2)
    ax.add_patch(wheel1)
    # Rotation arrow (clockwise)
    arc1 = Arc((-0.8, 0), 0.7, 0.7, angle=0, theta1=30, theta2=120,
               color='#1f77b4', linewidth=1.5)
    ax.add_patch(arc1)
    ax.annotate('', xy=(-0.55, 0.35), xytext=(-0.45, 0.45),
                arrowprops=dict(arrowstyle='->', color='#1f77b4', lw=1.5))
    ax.text(-0.8, 0.8, 'Wheel 1\n(clockwise)', fontsize=8, ha='center', color='#1f77b4')

    # Right wheel
    wheel2 = Circle((0.8, 0), 0.5, fill=False, edgecolor='#d62728', linewidth=2)
    ax.add_patch(wheel2)
    # Rotation arrow (counter-clockwise)
    arc2 = Arc((0.8, 0), 0.7, 0.7, angle=0, theta1=60, theta2=150,
               color='#d62728', linewidth=1.5)
    ax.add_patch(arc2)
    ax.annotate('', xy=(1.05, 0.35), xytext=(0.95, 0.45),
                arrowprops=dict(arrowstyle='->', color='#d62728', lw=1.5))
    ax.text(0.8, 0.8, 'Wheel 2\n(counter-clockwise)', fontsize=8, ha='center', color='#d62728')

    # Connecting axis
    ax.plot([-0.3, 0.3], [0, 0], 'k-', linewidth=3)
    ax.text(0, -0.15, 'Shared axis', fontsize=8, ha='center')

    # Key principle
    ax.text(0, -1.0, 'Anti-phase oscillation cancels external vibrations:\n' +
            r'$\theta_2(t) = -\theta_1(t) \Rightarrow$ center of mass fixed',
            fontsize=9, ha='center', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'linked-balance', chapter=9)


def error_sources():
    """Pie chart showing sources of residual error in H4.
    """
    setup_style()
    fig, ax = plt.subplots(figsize=(5, 5))

    sources = ['Thermal lag', 'Escapement\nfriction', 'Bearing\nwear', 'Elasticity\ncreep']
    contributions = [35, 30, 20, 15]  # Approximate percentages
    colors = ['#ff7f0e', '#1f77b4', '#2ca02c', '#d62728']

    wedges, texts, autotexts = ax.pie(contributions, labels=sources, autopct='%1.0f%%',
                                       colors=colors, startangle=90,
                                       wedgeprops=dict(edgecolor='black', linewidth=0.5))

    # Style the percentage text
    for autotext in autotexts:
        autotext.set_fontsize(9)
        autotext.set_fontweight('bold')

    ax.set_title('H4 Residual Error Sources\n(5.1 seconds over 81 days)', fontsize=10)

    save_figure(fig, 'error-sources', chapter=9)


if __name__ == "__main__":
    chronometer_evolution()
    temperature_compensation()
    trial_performance()
    linked_balance()
    error_sources()
