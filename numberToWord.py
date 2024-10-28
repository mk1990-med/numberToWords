import ast

# Dictionaries used to convert numbers to words
units =  {1: "un", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq", 6: "six",
         7:  "sept", 8: "huit", 9:  "neuf", 11: "onze", 12:  "douze", 13: "treize",
         14: "quatorze", 15: "quinze", 16: "seize"}
tens = {
    10: "dix", 20: "vingt", 30: "trente", 40: "quarante", 50: "cinquante", 60: "soixante",
    70: "soixante-dix", 80: "quatre-vingt", 90: "quatre-vingt-dix"
}
high_numbers = {
    100: "cent", 1000: "mille", 1000000: "million", 1000000000: "milliard", 1000000000000: "billion",
    1000000000000000: "billiard", 1000000000000000000: "trillion"
}
exception = {
    71: "soixante-et-onze", 72: "soixante-douze", 73: "soixante-treize", 74: "soixante-quatorze",
    75: "soixante-quinze", 76: "soixante-seize", 81: "quatre-vingt-un", 91: "quatre-vingt-onze", 92: "quatre-vingt-douze",
    93: "quatre-vingt-treize", 94: "quatre-vingt-quatorze", 95: "quatre-vingt-quinze",
    96: "quatre-vingt-seize"
}
MAX_NUMBER = 1000000000000000000000

def number_to_words(nbr: int, rec = False):
    """
    method can be used to convert a number to French number-words
    :param nbr: number to convert
    :param rec: is equal to True iff it is a recursive call
    :return: a string representing the French number-words
    """
    # case nbr is equal to zero or is negative or too big
    if nbr == 0:
        return "zéro"
    elif nbr < 0:
        return "moins " + number_to_words(-nbr)
    elif nbr >= MAX_NUMBER:
        return "Nombre trop grand"

    # list to store resulted words
    words = []

    # case of a number higher than 100
    if nbr >= 100:
        # we iterate overs high_numbers in the decreasing order
        for key in reversed(high_numbers.keys()):
            if nbr >= key:
                # floor division is applied here to get the largest integer less than or equal to the division result
                # it represents the number of hundreds, thousands, ...
                floor_div_value = nbr // key
                # nbr is updates to the remainder of the division
                nbr %= key
                # to handle "cent" and  "mille" because we don't say "un cent" "un mille"
                if floor_div_value == 1 and key <= 1000:
                    words.append(high_numbers.get(key))
                else:
                    # Here a recursive call is done on the number of hundreds, thousands, ...
                    # the recursive call can add 's' so we use rec parameter
                    # "s" is added when the remainder is equal to 0 except for ”mille” since it never takes an “s”.
                    words.append(number_to_words(nbr=floor_div_value, rec=True) + "-" + high_numbers.get(key) + ("s" if key != 1000 and nbr == 0 and rec is False else ""))

    if nbr >= 20:
        # tens
        if nbr % 10 == 0:
            words.append(tens.get(nbr) + ("s" if nbr == 80 and rec is False else ""))
        # exceptions
        elif nbr in exception.keys():
            words.append(exception.get(nbr))
        else:
            # numbers >= 20 ending with 1: add "et"
            words.append(tens.get(nbr - nbr % 10) + "-" + ("et-" if nbr % 10 == 1 else '') + units.get(nbr % 10))
    # units are handled here including numbers between 11-16
    elif nbr in units.keys():
        words.append(units.get(nbr))
    # the Rest of numbers >=10
    elif nbr >= 10:
        words.append(tens.get(10) + (("-" + units.get(nbr - 10)) if nbr != 10 else ""))

    return "-".join(words).strip()

def convert_list_of_numbers(in_list: list):
    """
    this method takes a list of numbers (numerical) and returns a list of French numbers (words)
    :param in_list: list of numbers
    :return: a list of French numbers (words)
    """
    return [number_to_words(nbr) for nbr in in_list]

def parse_list_from_text(text: str):
    try:
        return ast.literal_eval(text)
    except (ValueError, SyntaxError):
        print("Error when parsing the list")
        return None

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', help='list of numbers to convert', type=str, required=True)
    args = parser.parse_args()
    list_numbers = parse_list_from_text(args.list)
    if list_numbers:
        print(convert_list_of_numbers(list_numbers))

