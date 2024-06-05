
def main():
    file_contents=None
    words_count_output=None
    count_unique_caracters_output=None
    count_unique_sorted=None

    print("--- Begin report of books/frankenstein.txt ---")

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words_count_output = count_words(file_contents)
    count_unique_caracters_output = count_unique_caracters(file_contents)

    def value_getter(item):
        return item[1]

    count_unique_sorted=sorted(count_unique_caracters_output.items(), key=value_getter , reverse=True )

    print(f"{words_count_output} words found in the document")
    print("")

    #print(count_unique_sorted)

    for i in range(0, len(count_unique_sorted)):
        if count_unique_sorted[i][0].isalpha():
            print(f"The '{count_unique_sorted[i][0]}' character was found '{count_unique_sorted[i][1]}' times")

    print("--- End report ---")




def count_unique_caracters(texto_input):
    dir_caracteres={}

    for i in range(0, len(texto_input)):

        if texto_input[i].lower() not in dir_caracteres:
            dir_caracteres[texto_input[i].lower()]=1
        else:
            dir_caracteres[texto_input[i].lower()] += 1

    return(dir_caracteres)




def count_words(texto_input):
    count_words_retorno=None

    count_words_retorno=len(texto_input.split())
    return(count_words_retorno)


main()






