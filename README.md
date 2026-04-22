# celestial_birthday

For a given start date (e.g. a birthday) and a given period of interest (e.g. the next couple of years), this program computes the integer-orbit completion dates for all planets. It then identifies clusters of these events and plots them on a timeline.

This is useful if you feel like celebrating _extra_ birthdays, computed relative to other planet orbital periods.

## Usage

```bash
python celestial_birthday.py
```

The program will read the start date from the command line or use a default value. It will then compute the integer-orbit completion dates for all planets and plot them on a timeline. It will also identify clusters of these events and print them to the console.

## Configuration

The program uses the following configuration:

- `start_date`: The start date for the computation. This can be provided as a command line argument or set in the `default_date` variable in the `main` function.
- `end_date`: The end date for the computation. This is set to 3 years from the start date by default.
- `window_days`: The window size for detecting clusters. This is set to 10 days by default.
- `min_planets`: The minimum number of planets required to form a cluster. This is set to 2 by default.

## Output

The program will produce the following output:

- A plot of the integer-orbit completion dates for all planets.
- A list of clusters of integer-orbit completion dates.

## Example

```bash
python celestial_birthday.py
```

Output:

```
Start date: 1975-01-01
Earth       51 orbits  →  2026-01-01
Mercury    212 orbits  →  2026-01-22
Venus       83 orbits  →  2026-01-23
Mercury    213 orbits  →  2026-04-20
Mercury    214 orbits  →  2026-07-17
Venus       84 orbits  →  2026-09-04
Mercury    215 orbits  →  2026-10-13
Earth       52 orbits  →  2027-01-01
Mercury    216 orbits  →  2027-01-09
Mercury    217 orbits  →  2027-04-07
Venus       85 orbits  →  2027-04-17
Mercury    218 orbits  →  2027-07-04
Mars        28 orbits  →  2027-08-31
Mercury    219 orbits  →  2027-09-30
Venus       86 orbits  →  2027-11-28
Mercury    220 orbits  →  2027-12-27
Earth       53 orbits  →  2028-01-01
Mercury    221 orbits  →  2028-03-24
Mercury    222 orbits  →  2028-06-20
Venus       87 orbits  →  2028-07-09
Mercury    223 orbits  →  2028-09-16
Mercury    224 orbits  →  2028-12-13

Cluster 2026-01-22 → 2026-01-23
  Mercury   212 orbits  2026-01-22
  Venus      83 orbits  2026-01-23

Cluster 2027-01-01 → 2027-01-09
  Earth      52 orbits  2027-01-01
  Mercury   216 orbits  2027-01-09

Cluster 2027-04-07 → 2027-04-17
  Mercury   217 orbits  2027-04-07
  Venus      85 orbits  2027-04-17

Cluster 2027-12-27 → 2028-01-01
  Mercury   220 orbits  2027-12-27
  Earth      53 orbits  2028-01-01
```