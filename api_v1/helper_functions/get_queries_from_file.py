#!/usr/bin/python3

def get_queries(query_file):
    """
    retrieves queries from a file
    """
    query_path = f"./mysql_queries/{query_file}"
    try:
        with open(query_path, 'r') as f:
            return (f.read())
    except FileNotFoundError:
        print(f"""ERROR: The file path you provided is not valid.
        there is no file at {query_path}""")
