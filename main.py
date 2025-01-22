path_to_file = "./books/frankenstein.txt"

def func(text):
    return len(text.split())

def word_count(text):
    dic = {}
    for i in text:
        i = i.lower()
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return dic

def sort_on(dict):
    return dict["num"]

with open(path_to_file) as f:
    file_contents = f.read()
    word_dict = word_count(file_contents)

    word_list = []
    for i in word_dict:
        word_list.append({"char": i, "num": word_dict[i]})
    word_list.sort(reverse= True, key = sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{func(file_contents)} words found in document")
    print()
    for i in word_list:
        if i["char"].isalpha():
            print(f"The '{i["char"]}' character was found {i["num"]} times")
    print("--- End report ---")
    

