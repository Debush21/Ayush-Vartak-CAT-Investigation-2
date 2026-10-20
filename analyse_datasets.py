
import statistics_library as stats

FILES = {
    "Normal": "normal.txt",
    "Plus Constant": "plus_constant.txt",
    "Times Constant": "times_constant.txt",
    "Extreme Outlier": "extreme_outlier.txt",
    "Duplicated Values": "duplicated_values.txt",
    "Reflected About 4000": "reflected_about_4000.txt",
    "ax_b": "ax_b.txt"
}

MEASURES = [
    ("Mean", stats.mean),
    ("Median", stats.median),
    ("Minimum", stats.minimum),
    ("Maximum", stats.maximum),
    ("Range", stats.data_range),
    ("Lower Quartile", stats.lower_quartile),
    ("Upper Quartile", stats.upper_quartile),
    ("IQR", stats.interquartile_range),
    ("Variance", stats.variance),
    ("Standard Deviation", stats.standard_deviation)
]


def read_data(filename):
    with open(filename, "r") as file:
        return [
            float(value)
            for line in file
            for value in line.split()
        ]


def main():
    headers = ["Dataset"] + [name for name, _ in MEASURES]
    rows = []

    for dataset_name, filename in FILES.items():
        data = read_data(filename)

        results = [function(data) for _, function in MEASURES]

        rows.append([
            dataset_name,
            *[
                f"{value:.4f}" if value is not None else "N/A"
                for value in results
            ]
        ])

    # Print a neatly aligned table
    widths = [
        max(len(str(row[i])) for row in [headers] + rows)
        for i in range(len(headers))
    ]

    def print_row(row):
        print(" | ".join(
            str(value).ljust(widths[i])
            for i, value in enumerate(row)
        ))

    print_row(headers)
    print("-+-".join("-" * width for width in widths))

    for row in rows:
        print_row(row)


if __name__ == "__main__":
    main()
