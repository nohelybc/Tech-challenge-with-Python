import logging

def flat_lists(lists: list) -> list:
    try:
        flat_list = []
        for item in lists:
            if type(item) == list:
                flat_list = flat_list + flat_lists(item)
            else:
                flat_list.append(item)
        return flat_list
    except Exception as e:
        logging.error(f' An error has occurred: {e}')