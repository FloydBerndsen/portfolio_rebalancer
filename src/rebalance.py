from pathlib import Path

import numpy as np
import pandas as pd


def current_allocation(holdings: pd.DataFrame):
    df = pd.DataFrame()
    df["stock"] = holdings["stock"]
    df["price"] = holdings["price"]
    df["total"] = holdings["quantity"] * holdings["price"]
    df["pct_of_total"] = df["total"] / sum(df["total"])
    return df


def rebalance(current_allocation: pd.DataFrame, target_allocation: dict):
    """Compares current allocation to target allocation,
    calculates which stocks to buy and sell to achieve target allocation"""
    df = pd.DataFrame()
    df["stock"] = current_allocation["stock"]
    df["price"] = current_allocation["price"]
    df["total"] = current_allocation["total"]
    df["target"] = sum(current_allocation["total"]) * current_allocation["stock"].map(
        target_allocation
    )
    df["difference"] = df["total"] - df["target"]
    df["buy"] = df[["difference", "price"]].apply(
        lambda x: x["difference"] / x["price"] if x["difference"] > 0 else 0, axis=1
    )
    df["sell"] = df[["difference", "price"]].apply(
        lambda x: x["difference"] / x["price"] * -1 if x["difference"] < 0 else 0,
        axis=1,
    )
    return df


if __name__ == "__main__":
    file = Path.cwd() / "data" / "example_data.csv"
    data = pd.read_csv(file)
    target_allocation = {"A": 0.25, "B": 0.25, "C": 0.25, "D": 0.25}

    print(
        rebalance(
            current_allocation=current_allocation(data),
            target_allocation=target_allocation,
        )
    )
