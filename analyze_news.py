"""Utility script to summarize scraped news CSV files."""
from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path
from typing import Iterable

import pandas as pd


STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "has",
    "in",
    "is",
    "it",
    "of",
    "on",
    "that",
    "the",
    "to",
    "was",
    "were",
    "with",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Summarize a scraped news CSV file with coverage details, frequency counts, "
            "and the most common words in article titles."
        )
    )
    parser.add_argument(
        "csv_path",
        type=Path,
        nargs="?",
        default=Path("news_data.csv"),
        help="Path to the CSV file containing scraped news data (default: news_data.csv)",
    )
    parser.add_argument(
        "--top-words",
        type=int,
        default=10,
        help="Number of top title words to display (default: 10)",
    )
    return parser.parse_args()


def load_news(csv_path: Path) -> pd.DataFrame:
    data_frame = pd.read_csv(csv_path)
    expected_columns = {"Date-Time", "Title", "Description"}
    missing = expected_columns - set(data_frame.columns)
    if missing:
        missing_list = ", ".join(sorted(missing))
        raise ValueError(f"Missing expected columns in {csv_path}: {missing_list}")
    return data_frame


def normalize_dates(date_strings: pd.Series) -> pd.Series:
    timestamps = pd.to_datetime(date_strings, errors="coerce")
    return timestamps.dt.date


def summarize_dates(dates: pd.Series) -> tuple[int, str, str]:
    clean_dates = dates.dropna()
    if clean_dates.empty:
        return 0, "N/A", "N/A"
    return (
        len(clean_dates),
        clean_dates.min().isoformat(),
        clean_dates.max().isoformat(),
    )


def average_title_length(titles: pd.Series) -> float:
    non_null_titles = titles.dropna().astype(str)
    if non_null_titles.empty:
        return 0.0
    return float(non_null_titles.str.len().mean())


def extract_top_words(titles: Iterable[str], limit: int) -> list[tuple[str, int]]:
    word_pattern = re.compile(r"[A-Za-z]{3,}")
    counter: Counter[str] = Counter()
    for title in titles:
        for word in word_pattern.findall(str(title).lower()):
            if word not in STOPWORDS:
                counter[word] += 1
    return counter.most_common(limit)


def build_report(data_frame: pd.DataFrame, top_word_limit: int) -> str:
    dates = normalize_dates(data_frame["Date-Time"])
    date_count, first_date, last_date = summarize_dates(dates)
    per_day_counts = dates.value_counts().sort_index()
    avg_title_len = average_title_length(data_frame["Title"])
    top_words = extract_top_words(data_frame["Title"], top_word_limit)

    lines = [
        "News dataset summary",
        "-------------------",
        f"Total articles: {len(data_frame)}",
        f"Articles with valid dates: {date_count}",
        f"Coverage window: {first_date} to {last_date}",
        f"Average title length: {avg_title_len:.1f} characters",
        "",
        "Articles per day:",
    ]

    if per_day_counts.empty:
        lines.append("  No valid dates available.")
    else:
        for day, count in per_day_counts.items():
            lines.append(f"  {day}: {count}")

    lines.extend(["", f"Top {top_word_limit} title words:"])
    if not top_words:
        lines.append("  No title words found.")
    else:
        for word, count in top_words:
            lines.append(f"  {word}: {count}")

    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    data_frame = load_news(args.csv_path)
    report = build_report(data_frame, args.top_words)
    print(report)


if __name__ == "__main__":
    main()
