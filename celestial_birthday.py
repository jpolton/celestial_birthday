from datetime import datetime, timedelta
from itertools import combinations
import matplotlib.pyplot as plt

# Mean sidereal orbital periods in days
PLANET_PERIODS = {
    "Mercury": 87.9691,
    "Venus": 224.701,
    "Earth": 365.25636,
    "Mars": 686.98,
    "Jupiter": 4332.589,
    "Saturn": 10759.22,
    "Uranus": 30688.5,
    "Neptune": 60182,
}

def integer_orbit_completions(
    start_date: datetime,
    start_year: int,
    end_year: int,
):
    """
    Compute integer-orbit completion dates for all planets.

    Parameters
    ----------
    start_date : datetime
        Epoch date from which orbits are counted
    start_year : int
        First calendar year to include (e.g. 2026)
    end_year : int
        Last calendar year to include (e.g. 2028)

    Returns
    -------
    list of dicts
        {"planet": planet_name, "orbits": orbit_number, "date": completion_datetime}
    """

    window_start = datetime(start_year, 1, 1)
    window_end   = datetime(end_year, 12, 31)

    results = []

    for planet, period_days in PLANET_PERIODS.items():
        # Estimate bounds for N to avoid unnecessary looping
        n_min = int(((window_start - start_date).days) // period_days) - 1
        n_max = int(((window_end   - start_date).days) // period_days) + 1

        for n in range(max(1, n_min), n_max + 1):
            completion_date = start_date + timedelta(days=period_days * n)

            if window_start <= completion_date <= window_end:
                results.append({"planet": planet, "orbits": n, "date": completion_date})

    # Sort chronologically
    results.sort(key=lambda x: x["date"])
    return results


def detect_clusters(completions, window_days=7, min_planets=2):
    """
    Detect clusters of integer-orbit completions.

    Parameters
    ----------
    completions : list of dicts
        Output from integer_orbit_completions
    window_days : int
        Maximum separation (days) between events
    min_planets : int
        Minimum number of distinct planets in a cluster

    Returns
    -------
    list of dicts describing clusters
    """

    clusters = []
    n = len(completions)

    for i in range(n):
        cluster = [completions[i]]
        start_time = completions[i]["date"]

        for j in range(i + 1, n):
            if (completions[j]["date"] - start_time).days <= window_days:
                cluster.append(completions[j])
            else:
                break

        planets_in_cluster = {c["planet"] for c in cluster}

        if len(planets_in_cluster) >= min_planets:
            clusters.append({
                "start": min(c["date"] for c in cluster),
                "end":   max(c["date"] for c in cluster),
                "events": cluster
            })

    return clusters

def overlay_clusters(ax, clusters, color="orange", alpha=0.2):
    for c in clusters:
        ax.axvspan(c["start"], c["end"], color=color, alpha=alpha)

def plot_orbit_timeline(completions):
    planets = sorted(set(e["planet"] for e in completions))
    planet_index = {p: i for i, p in enumerate(planets)}

    x = [e["date"] for e in completions]
    y = [planet_index[e["planet"]] for e in completions]

    plt.figure(figsize=(12, 4))
    plt.scatter(x, y, s=20)

    plt.yticks(range(len(planets)), planets)
    plt.xlabel("Date")
    plt.title("Integer Orbital Completions by Planet")
    plt.tight_layout()
    #plt.show()

def plot_clusters(start_date, completions, clusters):
    planets = sorted(set(e["planet"] for e in completions))
    planet_index = {p: i for i, p in enumerate(planets)}

    x = [e["date"] for e in completions]
    y = [planet_index[e["planet"]] for e in completions]
    
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.scatter(x, y, s=20)
    for e in completions:
        ax.text(e["date"], planet_index[e["planet"]], f' {e["orbits"]}', va='center', fontsize=8)

    overlay_clusters(ax, clusters)

    ax.set_yticks(range(len(planets)))
    ax.set_yticklabels(planets)
    ax.set_title(f"{start_date.date()}: Integer Orbit Completions with Clusters Highlighted")
    plt.show()


if __name__ == "__main__":

    default_date = "1975-01-01"
    try:
        with open("birthdays.txt", "r") as f:
            """
            file birthdays.txt has format:
            YYYY-MM-DD
            YYYY-MM-DD
            with as many rows as you like.
            If the file does not exist, the program reads default_date variable.
            """
            birthdays = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        birthdays = [default_date]

    for bday_str in birthdays:
        start_date = datetime.strptime(bday_str, "%Y-%m-%d")
        results = integer_orbit_completions(start_date, 2026, 2028)


        clusters = detect_clusters(
            results,
            window_days=10,      # ±10‑day clustering window
            min_planets=2        # at least two planets
        )

        #plot_orbit_timeline(results) # plot all orbital completions
        plot_clusters(start_date, results, clusters) # plot all orbital completions. Highlight clusters

        print(f"Start date: {start_date.strftime('%Y-%m-%d')}")
        for r in results:
            print(f"{r['planet']:8s}  {r['orbits']:4d} orbits  →  {r['date'].strftime('%Y-%m-%d')}")

        for c in clusters:
            print(
                f"\nCluster {c['start'].date()} → {c['end'].date()}"
            )
            for e in c["events"]:
                print(
                    f"  {e['planet']:7s}  {e['orbits']:4d} orbits  {e['date'].date()}"
                )
        print()
        input(f'Press Enter to continue')


