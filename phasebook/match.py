import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    """Check if all numbers in fave_numbers_2 are present in fave_numbers_1.

    Parameters:
        fave_numbers_1 (iterable): The first set of favorite numbers.
        fave_numbers_2 (iterable): The second set of favorite numbers.

    Returns:
        a bool where True if all numbers in fave_numbers_2 are present in fave_numbers_1, else False.
    """

    fave_numbers_1_set = set (fave_numbers_1)
    return all(number in fave_numbers_1_set for number in fave_numbers_2)
