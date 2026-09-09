"""Recompute the book's worked examples and compare against what it prints.

Every check is self-contained: it states where in the manuscript the claim
appears, recomputes it from first principles or from the book's own tabulated
data, and reports agreement or disagreement with a tolerance.

This catches two kinds of error that reading cannot. First, a result that
does not follow from the numbers given, which means either the numbers or the
result is wrong. Second, a result quoted to more precision than its inputs
support.

Run: .venv/bin/python3 scripts/verify/derivations.py
Exit code is non-zero if any check fails.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

ARCSEC_PER_RAD = 648000 / math.pi  # 206264.806...


@dataclass
class Result:
    name: str
    where: str
    printed: str
    computed: str
    ok: bool
    note: str = ""


results: list[Result] = []


def check(name, where, printed_value, computed_value, tol, unit="", note=""):
    if isinstance(printed_value, (int, float)) and isinstance(computed_value, (int, float)):
        ok = abs(printed_value - computed_value) <= tol
        printed_str = f"{printed_value:g}{unit}"
        computed_str = f"{computed_value:.6g}{unit}"
    else:
        ok = printed_value == computed_value
        printed_str, computed_str = str(printed_value), str(computed_value)
    results.append(Result(name, where, printed_str, computed_str, ok, note))


# ---------------------------------------------------------------------------
# Appendix A: constant of aberration
# ---------------------------------------------------------------------------

def aberration_constant():
    """kappa = v_earth / c, in arc-seconds.

    The book quotes 20.47 arcsec as the known value and 20.5 as Bradley's
    result. The modern IAU value is 20.49552 arcsec.
    """
    au = 149_597_870.7  # km, IAU 2012 definition
    year = 365.25636 * 86400  # sidereal year, seconds
    c = 299_792.458  # km/s
    v_mean = 2 * math.pi * au / year
    kappa = v_mean / c * ARCSEC_PER_RAD
    check("Constant of aberration", "app A, aberration",
          20.47, kappa, 0.06, '"',
          "circular-orbit approximation; IAU value is 20.49552")
    check("Earth mean orbital speed", "ch 12, app A",
          29.78, v_mean, 0.05, " km/s")


# ---------------------------------------------------------------------------
# Appendix A: the Bradley worked example
# ---------------------------------------------------------------------------

BRADLEY = [
    # (label, julian day as printed, zenith distance arcsec)
    ("January 5", 37.4, +5.7),
    ("January 27", 59.4, +8.8),
    ("February 15", 79.4, +11.2),
    ("March 1", 93.4, +17.3),
    ("April 2", 125.4, +18.1),
    ("May 3", 156.4, +15.4),
    ("June 1", 185.4, +10.1),
    ("July 2", 216.4, +0.5),
    ("August 3", 248.4, -10.2),
    ("September 1", 277.4, -16.9),
    ("October 3", 309.4, -20.0),
    ("November 4", 341.4, -19.5),
    ("December 1", 368.4, -20.5),
]


def bradley_fit():
    """Least-squares fit of z(t) = A sin(wt + phi) + B to the printed table.

    The book states A = 20.5, phi = -1.05 rad, B = -0.2, and residuals of
    1 to 2 arcsec. With omega fixed, the model is linear in
    (A cos phi, A sin phi, B), so the fit is exact and there is nothing to
    tune.
    """
    t = np.array([row[1] for row in BRADLEY])
    z = np.array([row[2] for row in BRADLEY])
    omega = 2 * math.pi / 365.25

    design = np.column_stack([np.sin(omega * t), np.cos(omega * t), np.ones_like(t)])
    (a_sin, a_cos, offset), *_ = np.linalg.lstsq(design, z, rcond=None)
    amplitude = math.hypot(a_sin, a_cos)
    phase = math.atan2(a_cos, a_sin)
    residuals = z - design @ [a_sin, a_cos, offset]
    rms = float(np.sqrt(np.mean(residuals**2)))

    check("Bradley fit: amplitude A", "app A, worked example",
          20.5, amplitude, 0.5, '"')
    check("Bradley fit: phase phi", "app A, worked example",
          -1.05, phase, 0.15, " rad")
    check("Bradley fit: offset B", "app A, worked example",
          -0.2, offset, 0.5, '"')
    check("Bradley fit: residual RMS", "app A, worked example",
          "1 to 2 arcsec",
          f"{rms:.2f} arcsec (max {np.abs(residuals).max():.2f})",
          0, note="book says residuals are typically 1-2 arcsec")

    check("Bradley: number of observations", "app A, worked example",
          23, len(BRADLEY), 0, " nights",
          "text says 23 clear nights; the table prints 13 rows")

    # The dates are labelled 1726 but the Julian days run past 365, so the
    # series must span more than one calendar year.
    check("Bradley: date labels consistent with day numbers",
          "app A, table of raw data",
          "all dates in 1726", "day 368.4 labelled 1 December 1726",
          0, note="day 368 is past the end of the year the table's header gives")

    # Phase check: aberration in zenith distance should peak when the Earth's
    # velocity is perpendicular to the line of sight. The printed phase and
    # the fitted one must at least agree in sign and rough size.
    degrees = math.degrees(phase)
    check("Bradley fit: phase in degrees", "app A, worked example",
          -60.0, degrees, 8.0, " deg",
          "book writes phi = -1.05 rad = -60 deg")


def phase_conversion():
    """The book writes 'phi = -1.05 radians = -60 degrees'."""
    check("Radian to degree conversion", "app A, worked example",
          -60.0, math.degrees(-1.05), 0.5, " deg",
          "-1.05 rad is -60.16 deg, so the rounding is fine")


# ---------------------------------------------------------------------------
# Speed of light from the aberration angle
# ---------------------------------------------------------------------------

def speed_of_light():
    """c = v / theta, with theta = 20.5 arcsec and v = 29.78 km/s."""
    theta = 20.5 / ARCSEC_PER_RAD
    c = 29.78 / theta
    check("Speed of light from aberration", "app A; ch 12",
          3.00e5, c, 0.02e5, " km/s")

    # The book compares against Roemer. Roemer himself gave a light-crossing
    # time, not a speed; the figure attributed to him depends on the value of
    # the astronomical unit then in use.
    check("Roemer's speed of light", "app A, implications",
          2.75e5, 2.20e5, 0.1e5, " km/s",
          "book says Roemer got 2.75e5 km/s; the figure usually derived from "
          "his 1676 light-time with Huygens's AU is about 2.1-2.2e5 km/s. "
          "Needs a source or correction")


# ---------------------------------------------------------------------------
# Refraction
# ---------------------------------------------------------------------------

def refraction():
    """R = 58.3 cot(h) arcsec, as used in ch 4 and its figure."""
    for altitude, printed in ((10, 331), (20, 160), (45, 58), (90, 0)):
        computed = 58.3 / math.tan(math.radians(altitude)) if altitude < 90 else 0.0
        check(f"Refraction at {altitude} deg", "ch 4, refraction curve",
              printed, computed, 1.0, '"')


# ---------------------------------------------------------------------------
# Pendulum
# ---------------------------------------------------------------------------

def pendulum():
    """Seconds pendulum length, and the daily error from thermal expansion."""
    g = 9.81
    length = g * (1.0 ** 2) / (math.pi ** 2)  # half-period of 1 s
    check("Seconds pendulum length", "ch 6, ch 21",
          0.994, length, 0.01, " m",
          "period 2 s, g = 9.81 m/s^2")

    # Brass, alpha = 19e-6 /K, over a 10 K rise. Rate error per day:
    # dT/T = (1/2) dL/L, so seconds per day = 86400 * alpha * dTemp / 2.
    alpha_brass = 19e-6
    seconds_per_day = 86400 * alpha_brass * 10 / 2
    check("Brass pendulum error, 10 K swing", "ch 6, figure ch06-temperature-error",
          8.0, seconds_per_day, 0.5, " s/day")

    # Gravity varies from equator to pole; a clock rated in London runs
    # differently elsewhere. Ratio of periods gives seconds per day.
    g_equator, g_pole, g_london = 9.7803, 9.8322, 9.8119
    for name, g_local, in (("equator", g_equator), ("pole", g_pole)):
        drift = 86400 * (math.sqrt(g_london / g_local) - 1)
        print(f"    [info] seconds pendulum moved London to {name}: {drift:+.1f} s/day")


# ---------------------------------------------------------------------------
# Time and angle
# ---------------------------------------------------------------------------

def time_and_longitude():
    check("Earth rotation rate", "ch 1, ch 17",
          15.0, 360 / 24, 0.001, " deg/hour")
    check("One hour of longitude at the equator", "ch 1",
          900, 15 * 60, 1, " nautical miles",
          "15 deg x 60 nautical miles per degree")
    sidereal = 86400 / 1.0027379093
    check("Sidereal day, seconds part", "ch 18",
          4.0, sidereal % 60, 0.5, " s",
          "book prints 23h 56m 04s")
    # A chronometer losing 3 s/day over a six-week passage.
    error_seconds = 3 * 42
    check("Longitude error, 3 s/day over 6 weeks", "ch 7, prize thresholds",
          31.5, error_seconds / 3600 * 15 * 60, 1.0, " nautical miles",
          "126 s of time is 0.525 deg is 31.5 nautical miles at the equator")


# ---------------------------------------------------------------------------
# Parallax
# ---------------------------------------------------------------------------

def parallax():
    check("Parsec definition", "ch 13, app I",
          3.086e16, 1 / (1 / ARCSEC_PER_RAD) * 149_597_870_700, 0.002e16, " m")
    check("Light-year", "app I",
          9.461e15, 299_792_458 * 365.25 * 86400, 0.002e15, " m")
    # Bessel 1838 gave 0.3136 arcsec for 61 Cygni. Appendix H rounds this to
    # "approximately 0.3 arcseconds", which is fine, but the distance that
    # follows is worth stating somewhere in the text and currently is not.
    bessel_parsecs = 1 / 0.3136
    check("61 Cygni distance from Bessel's parallax", "app H, 1838 entry",
          10.2, bessel_parsecs * 3.2616, 0.3, " light-years",
          "Bessel's 0.3136 arcsec gives 10.4 ly; the modern parallax is "
          "0.286 arcsec, so 11.4 ly. The book gives the parallax but never "
          "the distance it implies")


def main() -> int:
    print("Recomputing the book's worked examples\n")
    for section in (aberration_constant, bradley_fit, phase_conversion,
                    speed_of_light, refraction, pendulum, time_and_longitude,
                    parallax):
        section()

    width = max(len(r.name) for r in results)
    failed = 0
    for result in results:
        mark = "ok  " if result.ok else "FAIL"
        if not result.ok:
            failed += 1
        print(f"{mark}  {result.name:<{width}}  book: {result.printed:<22} computed: {result.computed}")
        if result.note:
            print(f"      {' ' * width}  note: {result.note}")

    print(f"\n{len(results) - failed} agree, {failed} disagree")
    if failed:
        print("\nA disagreement is not automatically an error in the book: check the")
        print("assumptions in this script first. But each one needs a decision.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
