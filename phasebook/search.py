from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    if (args): 
        matched_users = []
        unique_ids = set()

        for user in USERS:
            match_weight = calculate_match_weight(user, args)

            if match_weight and user["id"] not in unique_ids:
                matched_users.append((user, match_weight))
                unique_ids.add(user["id"])
    
        matched_users.sort(key=lambda user: user[1], reverse=True)

        return [user_info[0] for user_info in matched_users]
    else:
        return USERS


def calculate_match_weight(user, search_params): 
    """Calculate the match weight for a user based on search parameters.

    Parameters:
        user (dict): a dictionary representing a user with keys:
            id: string
            name: string
            age: string
            occupation: string
        
        search_params (dict): a dictionary containing the following parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        an int that represents the match weight for the user, where higher weights indicate high priority matches.
    """

    match_priority = {"id": 4, "name": 3, "age": 2, "occupation": 1}
    
    if "id" in search_params and str(user["id"]) == search_params["id"]:
        return match_priority["id"]
    elif "name" in search_params and search_params["name"].lower() in user["name"].lower():
        return match_priority["name"]
    elif "age" in search_params and user["age"] in range(int(search_params["age"]) - 1, int(search_params["age"]) + 2):
        return match_priority["age"]
    elif "occupation" in search_params and search_params["occupation"].lower() in user["occupation"].lower():
        return match_priority["occupation"]
    else:
        return 0