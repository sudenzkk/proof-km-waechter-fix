"""Compare breakdown and non-breakdown vehicle metrics in fleet_history.csv.

Breakdowns in this sample coincide with higher service mileage, daily use, and load;
odometer and age averages are nearly identical. These associations do not prove cause.
"""

from pathlib import Path

import pandas as pd


FEATURES = [
    "odometer_km",
    "age_years",
    "km_since_service",
    "avg_daily_km",
    "load_factor",
]


def main():
    data_path = Path(__file__).with_name("fleet_history.csv")
    df = pd.read_csv(data_path)

    no_breakdown = df[df["broke_down"] == 0]
    breakdown = df[df["broke_down"] == 1]

    means = pd.DataFrame(
        {
            "No breakdown": no_breakdown[FEATURES].mean(),
            "Broke down": breakdown[FEATURES].mean(),
        }
    )
    means["Difference (broke down - no breakdown)"] = (
        means["Broke down"] - means["No breakdown"]
    )

    print(f"Vehicles: {len(df)} total; {len(no_breakdown)} without breakdown; "
          f"{len(breakdown)} with breakdown")
    print("\nFeature means by breakdown outcome:")
    print(means.to_string(float_format=lambda value: f"{value:.2f}"))
    print(
        "\nInterpretation: km_since_service, avg_daily_km, and load_factor "
        "have notably higher means among vehicles that broke down. "
        "Odometer and age means are nearly the same between groups, so they "
        "do not distinguish breakdowns well in this dataset. These are "
        "descriptive associations, not evidence that any feature causes breakdowns."
    )


if __name__ == "__main__":
    main()
