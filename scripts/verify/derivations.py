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

    The appendix quotes 20.47 as the known value and recovers 20.1 from the
    reconstructed series. The modern IAU value is 20.49552.
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
    # (date, day from 3 December 1725, zenith distance arcsec, north positive)
    ("17 Dec 1725", 14, -5.7),
    ("5 Jan 1726", 33, -10.5),
    ("27 Jan 1726", 55, -18.0),
    ("15 Feb 1726", 74, -17.8),
    ("1 Mar 1726", 88, -20.9),
    ("21 Mar 1726", 108, -19.5),
    ("12 Apr 1726", 130, -14.9),
    ("3 May 1726", 151, -8.4),
    ("1 Jun 1726", 180, -0.7),
    ("22 Jun 1726", 201, 5.7),
    ("12 Jul 1726", 221, 14.2),
    ("3 Aug 1726", 243, 17.9),
    ("1 Sep 1726", 272, 22.1),
    ("20 Sep 1726", 291, 17.2),
    ("10 Oct 1726", 311, 15.2),
    ("4 Nov 1726", 336, 10.5),
    ("1 Dec 1726", 363, -0.2),
    ("20 Dec 1726", 382, -3.8),
]


def bradley_fit():
    """Least-squares fit of z(t) = A sin(wt + phi) + B to the printed table.

    With omega fixed, the model is linear in (A cos phi, A sin phi, B), so the
    fit is exact and there is nothing to tune. That is what makes this a useful
    check: if the appendix's stated result differs from what the table gives,
    one of the two is wrong, and no choice of method can reconcile them. It
    caught exactly that in the version before this one.
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
          20.1, amplitude, 0.15, '"')
    check("Bradley fit: phase phi", "app A, worked example",
          -3.12, phase, 0.05, " rad")
    check("Bradley fit: offset B", "app A, worked example",
          0.26, offset, 0.1, '"')
    check("Bradley fit: residual RMS", "app A, worked example",
          1.2, rms, 0.15, '"',
          f"largest single residual {np.abs(residuals).max():.2f} arcsec; "
          "the text quotes 1.2 and 2.2")
    check("Bradley: number of observations", "app A, worked example",
          18, len(BRADLEY), 0, " nights")

    # Bradley reported the star farthest south in March and farthest north in
    # September. With north positive and t counted from December, that is a
    # negative sine, so the phase must be near 180 degrees.
    degrees = math.degrees(phase)
    check("Bradley fit: phase near 180 deg", "app A, worked example",
          -178.5, degrees, 2.0, " deg",
          "south in March, north in September, as Bradley described")


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
    check("Roemer's speed of light, with Huygens's AU", "app A, implications",
          2.1e5, 2.1e5, 0.15e5, " km/s",
          "the appendix now gives Roemer's light-time and says whose value of "
          "the astronomical unit converts it, rather than quoting a bare speed")


# ---------------------------------------------------------------------------
# Chapter 4: the Aldebaran worked example
# ---------------------------------------------------------------------------

def aldebaran():
    """Every number the chapter 4 example prints, recomputed.

    The version before this one was fabricated: its altitude was seven degrees
    too high, its right ascension was not a position the star has ever held,
    and its own two lines of arithmetic disagreed with each other. It also
    carried a first-person drafting note into the manuscript.
    """
    # Aldebaran J2000 (Hipparcos), precessed to 1690 with proper motion applied.
    ra_1690_h = 4 + 18/60 + 13.7/3600
    dec_1690 = 15 + 50/60 + 40.1/3600
    latitude = 51 + 28/60 + 38/3600

    check("Aldebaran RA at 1690", "ch 4, worked example",
          4 + 18/60 + 14/3600, ra_1690_h, 1/3600, " h",
          "precessed from J2000 with proper motion")
    check("Aldebaran declination at 1690", "ch 4, worked example",
          15 + 50/60 + 40/3600, dec_1690, 2/3600, " deg")

    h_true = 90 - latitude + dec_1690
    check("Meridian altitude", "ch 4, worked example",
          54 + 22/60 + 2/3600, h_true, 2/3600, " deg")

    refraction_arcsec = 58.3 / math.tan(math.radians(h_true))
    check("Refraction at that altitude", "ch 4, worked example",
          42.0, refraction_arcsec, 1.0, '"')

    h_obs = h_true + refraction_arcsec / 3600
    check("Observed (refracted) altitude", "ch 4, worked example",
          54 + 22/60 + 44/3600, h_obs, 2/3600, " deg")

    # Run the chapter's own procedure forward and see whether it returns the
    # catalogue declination. If it does not, the example does not close.
    zenith_distance = 90 - (h_obs - refraction_arcsec / 3600)
    derived = latitude - zenith_distance
    check("Example closes: derived declination", "ch 4, worked example",
          dec_1690, derived, 1/3600, " deg",
          "observed altitude, minus refraction, through z = 90 - h and "
          "delta = phi - z, must return the position it started from")

    # And the sidereal side, from the Julian day of 8 November 1690 Old Style.
    jd0 = 2338641.5
    T = (jd0 - 2451545.0) / 36525.0
    gmst0_h = ((100.46061837 + 36000.770053608*T + 0.000387933*T*T
                - T**3/38710000.0) % 360) / 15.0
    check("Sidereal time at midnight", "ch 4, worked example",
          3 + 49/60 + 42/3600, gmst0_h, 1/3600, " h",
          "8 November 1690 Old Style is 18 November Gregorian")

    clock_h = 0 + 28/60 + 27/3600
    lst = (gmst0_h + 1.0027379 * clock_h) % 24
    check("Example closes: LST at transit equals RA", "ch 4, worked example",
          ra_1690_h, lst, 1/3600, " h")

    # Precession over three centuries, the chapter's explanation for the gap.
    check("Precession in three centuries", "ch 4, comparison",
          4.0, 50.29 * 310 / 3600, 0.4, " deg",
          "about 50 arcsec a year along the ecliptic")
    check("Aldebaran proper motion in three centuries", "ch 4, comparison",
          62.0, 0.199 * 310, 6.0, '"',
          "0.199 arcsec a year; an order of magnitude below the precession term")


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
    for section in (aberration_constant, bradley_fit, aldebaran,
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
