spam = ['apples','bananas','tofu','cats']
blank = []


def list_concat(your_list):
    new_string = str()
    your_index = 0
    for x in your_list:
        if your_index < len(your_list) - 1:
            new_string = new_string + str(x) + ', '
            your_index += 1
        else:
            new_string = new_string + str(x)
            break
    print(new_string)


list_concat(spam)
list_concat(blank)
