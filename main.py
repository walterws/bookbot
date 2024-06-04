
def main():
    file_contents=None
    words_count_output=None
    count_unique_caracters_output=None

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words_count_output = count_words(file_contents)

    count_unique_caracters_output = count_unique_caracters(file_contents)

    #print(file_contents)
    #print(words_count_output)
    print(count_unique_caracters_output)

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






