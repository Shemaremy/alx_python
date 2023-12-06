def best_score(a_dictionary):
    if not a_dictionary:
        return None 

    maximum=max(a_dictionary, key=a_dictionary.get)
    return maximum 