from dataclasses import dataclass

import pandas as pd
from scipy.stats import chi2_contingency


@dataclass
class DisparityResult:
    trade: str
    domestic_selection_rate: float
    international_selection_rate: float
    gap: float
    p_value: float


def selection_rate(df: pd.DataFrame, origin: str) -> float:
    subset = df[df["credential_origin"] == origin]
    if subset.empty:
        return float("nan")
    return (subset["decision"] == "ACCEPT").mean()


def false_rejection_rate(df: pd.DataFrame, origin: str) -> float:
    subset = df[df["credential_origin"] == origin]
    if subset.empty:
        return float("nan")
    return (subset["decision"] == "REJECT").mean()


def disparity_by_trade(df: pd.DataFrame) -> list[DisparityResult]:
    results = []
    for trade, group in df.groupby("trade"):
        domestic_rate = selection_rate(group, "domestic")
        international_rate = selection_rate(group, "international")

        contingency = pd.crosstab(group["credential_origin"], group["decision"])
        _, p_value, _, _ = chi2_contingency(contingency)

        results.append(
            DisparityResult(
                trade=trade,
                domestic_selection_rate=domestic_rate,
                international_selection_rate=international_rate,
                gap=domestic_rate - international_rate,
                p_value=p_value,
            )
        )
    return results
