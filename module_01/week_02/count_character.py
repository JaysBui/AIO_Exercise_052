# Bài 2:

def count_str(text):
    text_dict = {}
    text = text.lower()
    for char in text:
        if char not in text_dict:
            text_dict[char] = 0
        text_dict[char] += 1
    print(text_dict)
    return text_dict


if __name__ == "__main__":
    count_str("Happiness")
    count_str("smiles")
