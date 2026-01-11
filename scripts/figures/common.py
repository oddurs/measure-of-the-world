"""Shared utilities for matplotlib figure generation."""

from pathlib import Path
import matplotlib.pyplot as plt
import scienceplots

# Paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
OUTPUT_DIR = PROJECT_ROOT / "src" / "figures" / "generated"


def setup_style():
    """Configure consistent matplotlib style using SciencePlots."""
    # Use science style with LaTeX rendering for publication-quality typography
    plt.style.use(['science'])

    # Override with book-appropriate settings
    plt.rcParams.update({
        'figure.figsize': (6, 4),
        'figure.dpi': 300,
        'font.family': 'serif',
        'font.size': 10,
        'axes.labelsize': 11,
        'axes.titlesize': 12,
        'legend.fontsize': 9,
        'xtick.labelsize': 9,
        'ytick.labelsize': 9,
        'lines.linewidth': 1.5,
        'axes.linewidth': 0.8,
        'grid.linewidth': 0.5,
        'grid.alpha': 0.3,
    })


def save_figure(fig, name: str, chapter: int):
    """Save figure with consistent naming convention.

    Args:
        fig: matplotlib Figure object
        name: descriptive name (e.g., 'longitude-error')
        chapter: chapter number (1-25)
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    filename = f"ch{chapter:02d}-{name}.png"
    fig.savefig(OUTPUT_DIR / filename, bbox_inches='tight', dpi=300)
    plt.close(fig)
    print(f"Generated: {filename}")
