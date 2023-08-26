import json


def getword(search_term):
    # Load the JSON data into a Python list
    with open('/workspaces/eng-az-dict-api/src/dictapi/dictapi/dict/words25aug.json', encoding='utf-8') as f:
        data = json.load(f)

    # Convert the list to a dictionary with the word as the key
    word_dict = {word['word']: word for word in data}

    # Use a dictionary comprehension to filter the data based on the search term
    results = [value for key, value in word_dict.items(
    ) if search_term in (key, value['translation'])]
    if len(results) == 0:
        results = [{'word': 'No results found.'}]
    elif len(results) == 1:
        results = results[0]
    else:
        results = results
    # Return the results
    return results
