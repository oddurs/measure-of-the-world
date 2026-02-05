#!/usr/bin/env python3
"""Generate figures for Chapter 21: Clocks and Chronometers."""

from common import setup_style, save_figure
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Arc, Wedge, FancyArrowPatch
import numpy as np


def pendulum_physics():
    """Simple harmonic motion of a pendulum."""
    setup_style()
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))

    # Left: pendulum diagram
    ax = axes[0]

    # Pivot point
    pivot_x, pivot_y = 0, 3
    ax.plot(pivot_x, pivot_y, 'ko', markersize=8)
    ax.plot([-0.5, 0.5], [pivot_y + 0.1, pivot_y + 0.1], 'k-', linewidth=3)

    # Pendulum at rest (vertical)
    L = 2.5
    ax.plot([pivot_x, pivot_x], [pivot_y, pivot_y - L], 'k--', linewidth=1, alpha=0.5)

    # Pendulum at angle theta
    theta = 20  # degrees
    bob_x = pivot_x + L * np.sin(np.radians(theta))
    bob_y = pivot_y - L * np.cos(np.radians(theta))

    ax.plot([pivot_x, bob_x], [pivot_y, bob_y], 'k-', linewidth=2)
    ax.add_patch(Circle((bob_x, bob_y), 0.2, facecolor='#1f77b4',
                         edgecolor='black', linewidth=1.5))

    # Arc showing angle
    arc = Arc((pivot_x, pivot_y), 1, 1, angle=270, theta1=0, theta2=theta,
              color='red', linewidth=2)
    ax.add_patch(arc)
    ax.text(0.3, pivot_y - 0.7, r'$\theta$', fontsize=12, color='red')

    # Length label
    mid_x = (pivot_x + bob_x) / 2 + 0.2
    mid_y = (pivot_y + bob_y) / 2
    ax.text(mid_x, mid_y, 'L', fontsize=11, ha='left')

    # Gravity arrow
    ax.annotate('', xy=(bob_x, bob_y - 0.6), xytext=(bob_x, bob_y - 0.2),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(bob_x + 0.2, bob_y - 0.5, 'mg', fontsize=10, color='green')

    # Swing arrow
    ax.annotate('', xy=(bob_x - 0.5, bob_y + 0.3),
                xytext=(bob_x - 0.2, bob_y + 0.1),
                arrowprops=dict(arrowstyle='->', color='purple', lw=2,
                                connectionstyle='arc3,rad=-0.3'))

    ax.set_xlim(-1.5, 2)
    ax.set_ylim(-0.5, 3.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Pendulum', fontsize=10)

    # Right: equations and period
    ax = axes[1]
    ax.axis('off')

    equations = [
        (r'Restoring torque: $\tau = -mgL\sin\theta$', 0.9),
        (r'For small $\theta$: $\sin\theta \approx \theta$', 0.75),
        (r'Equation of motion:', 0.6),
        (r'$\ddot{\theta} + \frac{g}{L}\theta = 0$', 0.5),
        (r'Period: $T = 2\pi\sqrt{\frac{L}{g}}$', 0.3),
        (r'Isochronism: Period independent', 0.15),
        (r'of amplitude (for small $\theta$)', 0.05),
    ]

    for text, y in equations:
        ax.text(0.1, y, text, fontsize=10, transform=ax.transAxes, va='center')

    plt.tight_layout()
    save_figure(fig, 'pendulum-physics', chapter=21)


def gridiron_pendulum():
    """Temperature compensation using alternating brass and steel rods."""
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 5))

    # Pivot
    pivot_x, pivot_y = 0, 4
    ax.plot([-0.3, 0.3], [pivot_y, pivot_y], 'k-', linewidth=4)

    # Rod positions
    rod_width = 0.08
    rod_spacing = 0.25

    # Draw alternating brass and steel rods
    materials = [
        ('brass', '#B8860B', -0.5),  # brass expands down
        ('steel', '#708090', -0.25),  # steel expands up
        ('brass', '#B8860B', 0),
        ('steel', '#708090', 0.25),
        ('brass', '#B8860B', 0.5),
    ]

    for name, color, x_offset in materials:
        # Each rod
        rod_x = pivot_x + x_offset
        ax.add_patch(Rectangle((rod_x - rod_width/2, pivot_y - 2.5),
                                rod_width, 2.5,
                                facecolor=color, edgecolor='black', linewidth=0.5))

    # Cross bars connecting rods
    for y in [pivot_y - 0.5, pivot_y - 1.5, pivot_y - 2.5]:
        ax.plot([-0.5, 0.5], [y, y], 'k-', linewidth=2)

    # Bob
    bob = Circle((0, pivot_y - 3), 0.3, facecolor='#1f77b4',
                 edgecolor='black', linewidth=2)
    ax.add_patch(bob)
    ax.text(0, pivot_y - 3, 'Bob', fontsize=8, ha='center', va='center', color='white')

    # Labels
    ax.text(-0.5, pivot_y - 0.2, 'Brass', fontsize=7, ha='center', color='#B8860B')
    ax.text(-0.25, pivot_y - 0.2, 'Steel', fontsize=7, ha='center', color='#708090')

    # Expansion arrows for hot
    ax.annotate('', xy=(-0.5, pivot_y - 2.7), xytext=(-0.5, pivot_y - 2.3),
                arrowprops=dict(arrowstyle='->', color='red', lw=1.5))
    ax.annotate('', xy=(-0.25, pivot_y - 0.3), xytext=(-0.25, pivot_y - 0.7),
                arrowprops=dict(arrowstyle='->', color='blue', lw=1.5))

    # Explanation box
    ax.text(1.5, 2.5, 'Temperature Compensation:\n\n'
            r'Brass: $\alpha \approx 19 \times 10^{-6}$/K' + '\n'
            r'Steel: $\alpha \approx 12 \times 10^{-6}$/K' + '\n\n'
            'Brass expands down,\n'
            'Steel expands up.\n'
            'Net effect on bob: ~zero',
            fontsize=8, ha='left', va='top',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-1.5, 3.5)
    ax.set_ylim(0, 4.5)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'gridiron-pendulum', chapter=21)


def escapement_types():
    """Comparison of escapement mechanisms."""
    setup_style()
    fig, axes = plt.subplots(1, 3, figsize=(9, 3.5))

    # Verge escapement
    ax = axes[0]
    ax.set_title('Verge Escapement', fontsize=9)

    # Escape wheel
    wheel = Circle((0, 0), 0.8, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(wheel)

    # Teeth
    n_teeth = 12
    for i in range(n_teeth):
        angle = 2 * np.pi * i / n_teeth
        x1 = 0.7 * np.cos(angle)
        y1 = 0.7 * np.sin(angle)
        x2 = 0.95 * np.cos(angle + 0.1)
        y2 = 0.95 * np.sin(angle + 0.1)
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=1.5)

    # Verge (vertical staff with two pallets)
    ax.plot([0, 0], [-1.2, 1.2], 'b-', linewidth=3)
    ax.plot([-0.3, 0.3], [0.7, 0.7], 'r-', linewidth=4)  # upper pallet
    ax.plot([-0.3, 0.3], [-0.7, -0.7], 'r-', linewidth=4)  # lower pallet

    ax.text(0.5, 0.8, 'Pallet', fontsize=7, color='red')
    ax.text(0.3, 0, 'Verge', fontsize=7, color='blue')
    ax.text(0, -1.5, 'Recoil occurs', fontsize=7, ha='center', color='gray')

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.8, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    # Deadbeat escapement
    ax = axes[1]
    ax.set_title('Deadbeat Escapement', fontsize=9)

    # Escape wheel
    wheel = Circle((0, 0), 0.8, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(wheel)

    # Teeth
    for i in range(n_teeth):
        angle = 2 * np.pi * i / n_teeth
        x1 = 0.7 * np.cos(angle)
        y1 = 0.7 * np.sin(angle)
        x2 = 0.95 * np.cos(angle + 0.08)
        y2 = 0.95 * np.sin(angle + 0.08)
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=1.5)

    # Anchor
    ax.plot([0, 0], [1.2, 1.5], 'b-', linewidth=3)
    ax.plot([-0.6, 0], [0.6, 1.2], 'b-', linewidth=3)
    ax.plot([0.6, 0], [0.6, 1.2], 'b-', linewidth=3)

    # Curved pallets
    theta1 = np.linspace(0.3, 0.7, 10)
    ax.plot(0.85 * np.cos(np.pi/2 + theta1), 0.85 * np.sin(np.pi/2 + theta1),
            'r-', linewidth=3)
    theta2 = np.linspace(-0.3, -0.7, 10)
    ax.plot(0.85 * np.cos(np.pi/2 + theta2), 0.85 * np.sin(np.pi/2 + theta2),
            'r-', linewidth=3)

    ax.text(0, 1.7, 'Pivot', fontsize=7, ha='center')
    ax.text(0, -1.5, 'No recoil\n(dead pallets)', fontsize=7, ha='center', color='gray')

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.8, 2)
    ax.set_aspect('equal')
    ax.axis('off')

    # Detent escapement
    ax = axes[2]
    ax.set_title('Detent (Chronometer)', fontsize=9)

    # Escape wheel
    wheel = Circle((0, 0), 0.8, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(wheel)

    # Teeth (pointed)
    for i in range(n_teeth):
        angle = 2 * np.pi * i / n_teeth
        x1 = 0.65 * np.cos(angle)
        y1 = 0.65 * np.sin(angle)
        x2 = 0.95 * np.cos(angle)
        y2 = 0.95 * np.sin(angle)
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=1.5)

    # Detent lever
    ax.plot([0.9, 1.5], [-0.2, -0.2], 'g-', linewidth=3)
    ax.plot([1.5, 1.5], [-0.4, 0], 'g-', linewidth=3)  # spring

    # Passing spring
    ax.plot([0.5, 0.9], [0.5, 0.3], 'orange', linewidth=2)

    ax.text(1.3, 0.1, 'Detent', fontsize=7, color='green')
    ax.text(0.7, 0.6, 'Passing\nspring', fontsize=6, color='orange')
    ax.text(0, -1.5, 'Nearly frictionless\n(one impulse/cycle)', fontsize=7,
            ha='center', color='gray')

    ax.set_xlim(-1.5, 2)
    ax.set_ylim(-1.8, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    save_figure(fig, 'escapement-types', chapter=21)


def fusee_mechanism():
    """How the fusee maintains constant driving force."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 4))

    # Mainspring barrel
    barrel_x, barrel_y = 1, 1.5
    barrel = Circle((barrel_x, barrel_y), 0.7, fill=False,
                    edgecolor='blue', linewidth=2)
    ax.add_patch(barrel)
    ax.text(barrel_x, barrel_y, 'Main-\nspring', fontsize=7,
            ha='center', va='center', color='blue')

    # Spiral spring inside (simplified)
    theta = np.linspace(0, 3*np.pi, 50)
    r = 0.15 + 0.15 * theta / (3*np.pi)
    spring_x = barrel_x + r * np.cos(theta)
    spring_y = barrel_y + r * np.sin(theta)
    ax.plot(spring_x, spring_y, 'b-', linewidth=1, alpha=0.7)

    # Fusee (cone)
    fusee_x, fusee_y = 4, 1.5
    # Draw as trapezoid (side view of cone)
    fusee_pts = np.array([
        [fusee_x - 0.3, fusee_y - 0.8],
        [fusee_x + 0.3, fusee_y - 0.8],
        [fusee_x + 0.5, fusee_y + 0.8],
        [fusee_x - 0.5, fusee_y + 0.8],
    ])
    ax.fill(fusee_pts[:, 0], fusee_pts[:, 1], color='#DEB887',
            edgecolor='black', linewidth=2)
    ax.text(fusee_x, fusee_y, 'Fusee\n(cone)', fontsize=7,
            ha='center', va='center')

    # Chain/cord connecting them
    # Top of fusee (when spring is wound tight)
    ax.plot([barrel_x + 0.7, fusee_x - 0.5], [barrel_y + 0.3, fusee_y + 0.6],
            'k-', linewidth=2)
    # Bottom of fusee (when spring is nearly unwound)
    ax.plot([barrel_x + 0.7, fusee_x - 0.3], [barrel_y - 0.3, fusee_y - 0.6],
            'k--', linewidth=1, alpha=0.5)

    ax.text(2.5, 2.3, 'Chain', fontsize=8, ha='center')

    # Annotations
    ax.annotate('High torque\n(spring wound)', xy=(barrel_x + 0.8, barrel_y + 0.5),
                xytext=(barrel_x + 1.5, barrel_y + 1.2),
                fontsize=7, ha='center',
                arrowprops=dict(arrowstyle='->', color='blue', lw=1))

    ax.annotate('Small radius\n= small lever arm', xy=(fusee_x - 0.45, fusee_y + 0.6),
                xytext=(fusee_x + 1, fusee_y + 1.3),
                fontsize=7, ha='center',
                arrowprops=dict(arrowstyle='->', color='#DEB887', lw=1))

    ax.annotate('Low torque\n(spring unwound)', xy=(barrel_x + 0.8, barrel_y - 0.5),
                xytext=(barrel_x + 1.5, barrel_y - 1.2),
                fontsize=7, ha='center', alpha=0.7,
                arrowprops=dict(arrowstyle='->', color='blue', lw=1, alpha=0.5))

    ax.annotate('Large radius\n= large lever arm', xy=(fusee_x - 0.25, fusee_y - 0.6),
                xytext=(fusee_x + 1, fusee_y - 1.3),
                fontsize=7, ha='center', alpha=0.7,
                arrowprops=dict(arrowstyle='->', color='#DEB887', lw=1, alpha=0.5))

    # Result
    ax.text(2.5, -0.3, 'Result: Constant output torque\n'
            r'$\tau_{out} = F \times r_{fusee}$ = constant',
            fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-1, 3.2)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'fusee-mechanism', chapter=21)


def clock_precision_evolution():
    """Evolution of timekeeping precision from medieval to atomic."""
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 5))

    data = [
        (1400, 15*60, 'Verge'),  # 15 min/day
        (1700, 1, 'Pendulum\n(deadbeat)'),  # 1 sec/day
        (1770, 0.5, 'Marine\nchronometer'),
        (1960, 0.001, 'Quartz'),  # 1 ms/day
        (1970, 1e-6, 'Cesium\natomic'),  # 1 microsec/day
    ]

    years = [d[0] for d in data]
    errors = [d[1] for d in data]
    labels = [d[2] for d in data]

    ax.semilogy(years, errors, 'b-o', linewidth=2, markersize=10)

    for year, err, label in data:
        y_offset = 2 if err > 0.01 else 0.3
        ax.annotate(label, xy=(year, err),
                    xytext=(year, err * y_offset),
                    fontsize=8, ha='center', va='bottom')

    ax.set_xlabel('Year', fontsize=10)
    ax.set_ylabel('Daily error (seconds)', fontsize=10)
    ax.set_xlim(1300, 2000)
    ax.set_ylim(1e-7, 2000)
    ax.grid(True, alpha=0.3, which='both')

    # Reference lines
    ax.axhline(60, color='gray', linestyle=':', linewidth=1, alpha=0.7)
    ax.text(1320, 70, '1 minute', fontsize=7, color='gray')
    ax.axhline(1, color='gray', linestyle=':', linewidth=1, alpha=0.7)
    ax.text(1320, 1.2, '1 second', fontsize=7, color='gray')

    plt.tight_layout()
    save_figure(fig, 'clock-precision-evolution', chapter=21)


def balance_wheel():
    """Balance wheel and hairspring oscillator."""
    setup_style()
    fig, ax = plt.subplots(figsize=(6, 5))

    # Balance wheel
    wheel_r = 1.5
    wheel = Circle((0, 0), wheel_r, fill=False, edgecolor='#1f77b4', linewidth=4)
    ax.add_patch(wheel)

    # Spokes
    for angle in [0, 90, 180, 270]:
        rad = np.radians(angle)
        ax.plot([0, wheel_r * np.cos(rad)], [0, wheel_r * np.sin(rad)],
                color='#1f77b4', linewidth=2)

    # Center pivot
    ax.add_patch(Circle((0, 0), 0.1, facecolor='black'))

    # Hairspring (spiral)
    theta = np.linspace(0, 6*np.pi, 200)
    r = 0.15 + 0.1 * theta / (2*np.pi)
    spring_x = r * np.cos(theta)
    spring_y = r * np.sin(theta)
    ax.plot(spring_x, spring_y, 'r-', linewidth=1.5)

    # Anchor point of hairspring
    ax.plot(spring_x[-1], spring_y[-1], 'ro', markersize=6)
    ax.text(spring_x[-1] + 0.2, spring_y[-1] + 0.2, 'Fixed\npoint', fontsize=7)

    # Labels
    ax.text(0, wheel_r + 0.3, 'Balance wheel', fontsize=9, ha='center')
    ax.text(0.8, 0.3, 'Hairspring', fontsize=8, color='red')

    # Oscillation arrows
    arc = Arc((0, 0), 3.5, 3.5, angle=0, theta1=20, theta2=70,
              color='green', linewidth=2)
    ax.add_patch(arc)
    ax.annotate('', xy=(1.1, 1.5), xytext=(1.5, 1.1),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))

    arc2 = Arc((0, 0), 3.5, 3.5, angle=0, theta1=-70, theta2=-20,
               color='green', linewidth=2)
    ax.add_patch(arc2)
    ax.annotate('', xy=(1.5, -1.1), xytext=(1.1, -1.5),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))

    ax.text(2, 0, 'Oscillates', fontsize=8, color='green', ha='left')

    # Equation
    ax.text(0, -2.5, r'Period: $T = 2\pi\sqrt{\frac{I}{\kappa}}$' + '\n'
            r'$I$ = moment of inertia, $\kappa$ = spring constant',
            fontsize=9, ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                      edgecolor='#cccccc'))

    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-3.2, 2.2)
    ax.set_aspect('equal')
    ax.axis('off')

    save_figure(fig, 'balance-wheel', chapter=21)


if __name__ == "__main__":
    pendulum_physics()
    gridiron_pendulum()
    escapement_types()
    fusee_mechanism()
    clock_precision_evolution()
    balance_wheel()
