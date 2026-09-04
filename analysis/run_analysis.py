import pandas as pd

from harness.scorer import disparity_by_trade, false_rejection_rate

DEMO_DATA_PATH = "demo_data/synthetic_sample.csv"


def main():
    df = pd.read_csv(DEMO_DATA_PATH)
    print(f"Loaded {len(df)} judgements across {df['trade'].nunique()} trades\n")

    for result in disparity_by_trade(df):
        print(
            f"{result.trade:<20} "
            f"domestic={result.domestic_selection_rate:.2f}  "
            f"international={result.international_selection_rate:.2f}  "
            f"gap={result.gap:+.2f}  "
            f"p={result.p_value:.4f}"
        )

    overall_fr = false_rejection_rate(df, "international")
    print(f"\nOverall false-rejection rate, international credentials: {overall_fr:.2%}")


if __name__ == "__main__":
    main()
