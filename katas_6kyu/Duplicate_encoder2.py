

def duplicate_encode(word):
    final_word = ""
    for letter in word:
        if word.count(letter) == 1:
            final_word = final_word + "("
        elif word.count(letter) > 1:
            final_word = final_word + ")"
    return final_word


if __name__ == "__main__":
    

    # CASE TEST #


    assert(duplicate_encode("din"))
    assert(duplicate_encode("recede"))