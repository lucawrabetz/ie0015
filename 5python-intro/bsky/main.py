import os
from typing import Any, Callable
import time
import numpy as np
import pandas as pd
from atproto import Client

HANDLES = ["lizzobeeating.bsky.social", "georgetakei.bsky.social"]


def read_data(filename: str = "twitter") -> pd.DataFrame:
    """
    filename must be just the name, and must be present in the current directory as filename + ".csv"
    """
    csvfile: str = filename + ".csv"

    if not os.path.exists(csvfile):
        raise ValueError

    twitter = pd.read_csv(csvfile)

    return twitter


def timer(func: Callable):
    """A function to time the execution of another function."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result

    return wrapper


def calculate_likes_per_share_iter(twitter):
    """Calculate 'likes_per_share' using iteration."""
    likes_per_share = []
    for _, row in twitter.iterrows():
        shares = row["number_of_shares"]
        if shares == 0:
            likes_per_share.append(0)
        else:
            likes_per_share.append(row["number_of_likes"] / shares)
    return likes_per_share


def calculate_likes_per_share_numpy(twitter):
    """Calculate 'likes_per_share' using NumPy vectorization."""
    likes = twitter["number_of_likes"]
    shares = twitter["number_of_shares"]
    return np.where(shares == 0, 0, likes / shares)


def calculate_likes_per_share_pandas(twitter):
    """Calculate 'likes_per_share' using Pandas column operation."""
    likes = twitter["number_of_likes"]
    shares = twitter["number_of_shares"]
    return (likes / shares).replace([np.inf, -np.inf], np.nan).fillna(0)


calculate_likes_per_share_iter = timer(calculate_likes_per_share_iter)
calculate_likes_per_share_numpy = timer(calculate_likes_per_share_numpy)
calculate_likes_per_share_pandas = timer(calculate_likes_per_share_pandas)


def main(client: Client) -> None:
    twitter = read_data()
    twitter = read_data()
    twitter["likes_per_share_iter"] = calculate_likes_per_share_iter(twitter)
    twitter["likes_per_share_numpy"] = calculate_likes_per_share_numpy(twitter)
    twitter["likes_per_share_pandas"] = calculate_likes_per_share_pandas(twitter)

    # for handle in HANDLES:
    #     print(f"\nProfile Posts of {handle}:\n\n")
    #     profile_feed = client.get_author_feed(actor=handle)
    #     import pdb

    #     pdb.set_trace()
    #     for feed_view in profile_feed.feed:
    #         print("-", feed_view.post.record.text)


if __name__ == "__main__":
    # at_client = Client(base_url="https://api.bsky.app")
    main(client=None)
