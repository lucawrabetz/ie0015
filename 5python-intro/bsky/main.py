import os
from typing import Callable
import time
import numpy as np
import pandas as pd
from atproto import Client

HANDLES = ["lizzobeeating.bsky.social", "georgetakei.bsky.social", "mcuban.bsky.social"]
TWITTER_CSV = "twitter.csv"
TWITTER_COLUMNS = [
    "author",
    "content",
    "country",
    "date_time",
    "id",
    "language",
    "latitude",
    "longitude",
    "number_of_likes",
    "number_of_shares",
    "likes_per_share",
]


def read_local_data(filename: str = TWITTER_CSV) -> pd.DataFrame:
    """
    filename must be just the name, and must be present in the current directory as filename + ".csv"
    """
    if not os.path.exists(filename):
        raise ValueError

    twitter = pd.read_csv(filename)

    return twitter


def timer(func: Callable) -> Callable:
    """A function to time the execution of another function."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result

    return wrapper


def calculate_likes_per_share_iter(twitter: pd.DataFrame) -> list[float]:
    """Calculate 'likes_per_share' using iteration."""
    likes_per_share: list[float] = []
    for _, row in twitter.iterrows():
        shares = row["number_of_shares"]
        if shares == 0:
            likes_per_share.append(np.nan)
        else:
            likes_per_share.append(row["number_of_likes"] / shares)
    return likes_per_share


def calculate_likes_per_share_numpy(twitter) -> np.ndarray:
    """Calculate 'likes_per_share' using NumPy vectorization."""
    likes = twitter["number_of_likes"]
    shares = twitter["number_of_shares"]
    return np.where(shares == 0, np.nan, likes / shares)


def calculate_likes_per_share_pandas(twitter) -> list[float]:
    """Calculate 'likes_per_share' using Pandas column operation."""
    likes = twitter["number_of_likes"]
    shares = twitter["number_of_shares"]
    return (likes / shares).replace([np.inf, -np.inf], np.nan)


calculate_likes_per_share_iter = timer(calculate_likes_per_share_iter)
calculate_likes_per_share_numpy = timer(calculate_likes_per_share_numpy)
calculate_likes_per_share_pandas = timer(calculate_likes_per_share_pandas)


def main(client: Client | None = None) -> None:
    twitter = read_local_data()

    if client is None:
        return

    for handle in HANDLES:
        print(f"\nProfile Posts of {handle}:\n\n")
        profile_feed = client.get_author_feed(actor=handle)
        import pdb

        pdb.set_trace()
        for feed_view in profile_feed.feed:
            print("-", feed_view.post.record.text)


if __name__ == "__main__":
    at_client = Client(base_url="https://api.bsky.app")
    main(client=at_client)
