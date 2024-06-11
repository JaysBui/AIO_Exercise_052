# Bài 3:

def count_wrds(file_name):
    with open(file_name, "r") as data:
        wrd_dict = {}
        for aline in data:
            lst_words = aline.split(" ")
            for wrd in lst_words:
                wrd = wrd.lower().strip()
                if wrd not in wrd_dict:
                    wrd_dict[wrd] = 0
                wrd_dict[wrd] += 1
    wrd_lst = list(wrd_dict.keys())
    wrd_lst.sort()
    sorted_wrd_dict = {i: wrd_dict[i] for i in wrd_lst}
    print(sorted_wrd_dict)
    return sorted_wrd_dict


if __name__ == "__main__":
    count_wrds("P1_data.txt")
