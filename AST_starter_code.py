# Imports - importing "csv" is not necessary!
from typing import Dict

# Constants
## Languages
ENG = "E"
ANI = "A" # Anishinaabemowin

## CSV location
CSV_LOC = "csv/ani_eng_phrases.csv"

def main() -> None:
    """
    The main loop of the English-Anishinaabemowin translator program.
    """
    # Loop infinitely
    while True:
        translation_dict = {}
        lang = ""

        # Repeatedly ask the user for an English or Anishinaabemowin language option upon an incorrect input
        while lang != ENG and lang != ANI:
            lang = input("What language do you want to find a translation for (English [E] or Anishinaabemowin [A])?\n")

        phrase_to_find = input("Enter the phrase you wish to find a translation for:\n")

        print("")
        
        # English option selected
        if lang == ENG:
            print(f"Listing English phrases containing \"{phrase_to_find}\" and their Anishinaabemowin translations:")
            translation_dict = find_phrase(phrase_to_find, "")
        
        # Anishinaabemowin option selected
        elif lang == ANI:
            print(f"Listing Anishinaabemowin phrases containing \"{phrase_to_find}\" and their English translations:")
            translation_dict = find_phrase("", phrase_to_find)
        
        print_results(translation_dict, lang == ENG)

def print_results(translation_dict: Dict[str, str], eng_translation: bool) -> None:
    """
    Prints the results of the user searching for an inputted phrase, depending
    on if they're wanting an English phrase translation or a Anishinaabemowin phrase translation

    Args:
        translation_dict (Dict[str, str]): A dictionary containing English phrases (keys)
        and their Anishinaabemowin translations (value)
        eng_translation (bool): True if the user searches for English phrase translations.
        False otherwise.
    """
    count = 1
    if eng_translation:
        for key, value in translation_dict.items():
            print(f"{count}. English: {key} => Anishinaabemowin: {value}")
            count += 1
    else:
        for key, value in translation_dict.items():
            print(f"{count}. Anishinaabemowin: {value} => English: {key}")
            count += 1
            
    print("End of results.", end="\n\n")

############################################# TASK 1 #############################################

def find_phrase(eng_search: str, ani_search: str) -> Dict[str, str]:
    """
    Finds the English phrase <eng_phrase> or the Anishinaabemowin phrase <ani_phrase> in the file
    <CSV_LOC>.

    Args:
        eng_search (str): The English phrase to search for. Is an empty string if the user is
        not searching for an English phrase's translation
        ani_search (str): The Anishinaabemowin phrase to search for. Is an empty string if the
        user is not searching for an Anishinaabemowin phrase's translation

    Returns:
        Dict[str, str]: A dictionary containing English phrases (keys) and their
        Anishinaabemowin translations (value)
    """
    translation_dict = {}

    # We ensure the characters of all of our phrases are lower case to ensure our program
    # is case-insensitive.
    eng_search, ani_search = eng_search.lower(), ani_search.lower()
    
    # TODO: What should replace "None" in the "with" statement?
    with open(CSV_LOC, None, encoding="utf8") as next_line:
        next_line.readline() # Skip the header

        # TODO: What should we do if we want to read the first line of the csv, after the header?
        line = None

        ## Processing line by line
        while line:
            # TODO: How do we separate an Anishinaabemowin and English phrase from each other?
            # Hint: Are there any interesting properties that you can exploit?
            phrases = None
            
            # TODO: How should we assign these variables?
            line_ani, line_eng = None, None
                
            # Finding an English or Anishinaabemowin syllabic phrase
            if (((eng_search != "") and (eng_search in line_eng.lower())) or
                ((ani_search != "") and (ani_search in line_ani.lower()))):
                translation_dict[line_eng] = line_ani
                
            # TODO: How do we read the next line of the file?
            line = None # TODO

    return translation_dict

############################################# TASK 2 #############################################

def write_results(translation_dict: Dict[str, str], eng_translation: bool, phrase_to_find: str) -> None:
    """
    Write the results of the user searching for an inputted phrase, depending
    on if they want an English phrase translation or an Anishinaabemowin phrase translation.
    
    If <eng_translation> is True, then the written file's name should be:
    "eng_to_ani_<phrase_to_find>".
    Otherwise, the written file's name should be:
    "ani_to_eng_<phrase_to_find>".
    
    For instance, if the English option is chosen, then the written file's file name should be:
    "eng_to_ani_well"
    
    Note: The written results should be exactly the same as what is printed by print_results,
    with the exception of the "End of results." line.

    Args:
        translation_dict (Dict[str, str]): A dictionary containing English phrases (keys)
        and their Anishinaabemowin translations (value)
        eng_translation (bool): True if the user searches for English phrase translations.
        False otherwise.
        phrase_to_find (str): The user's inputted phrase

    """
    count = 1
    string_to_write = ""
    
    if eng_translation:
        file_nme = "eng_to_ani_" + phrase_to_find + ".txt"
        string_to_write = f"Listing English phrases containing \"{phrase_to_find}\" and their Anishinaabemowin translations:\n"
        for key, value in translation_dict.items():
            string_to_write += f"{count}. English: {key} => Anishinaabemowin: {value}\n"
            count += 1
        
    else:
        file_nme = "ani_to_eng_" + phrase_to_find + ".txt"
        string_to_write = f"Listing Anishinaabemowin phrases containing \"{phrase_to_find}\" and their English translations:\n"
        for key, value in translation_dict.items():
            string_to_write += f"{count}. Anishinaabemowin: {value} => Anishinaabemowin: {key}\n"
            count += 1

    if string_to_write != "":
        # TODO: What should replace "None" in the "with" statement?
        with open(file_nme, None, encoding="utf8") as file:
            
            # TODO: What should we do to write all of our results to a new file?
            pass

if __name__ == "__main__":
    main() # Run main loop infinitely