import streamlit as st
import numpy as np


def levenshtein_distance(sc_wrds, targ_wrds):
    arr_nbr = np.zeros((len(sc_wrds) + 1, len(targ_wrds) + 1), dtype=int)

    for i in range(1, len(sc_wrds) + 1):
        arr_nbr[i][0] = i
    for j in range(1, len(targ_wrds) + 1):
        arr_nbr[0][j] = j

    for i in range(1, len(sc_wrds) + 1):
        for j in range(1, len(targ_wrds) + 1):
            if sc_wrds[i - 1] == targ_wrds[j - 1]:
                sub_cost = 0
            else:
                sub_cost = 1
            del_cost = arr_nbr[i - 1][j] + 1
            ins_cost = arr_nbr[i][j - 1] + 1
            sub_cost = arr_nbr[i - 1][j - 1] + sub_cost
            arr_nbr[i][j] = min(del_cost, ins_cost, sub_cost)

    return arr_nbr[-1][-1]


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words


vocabs = load_vocab(file_path='solution/vocab.txt')


def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word:')
    if st.button("Compute"):
        leven_distances = {vocab: levenshtein_distance(
            word, vocab) for vocab in vocabs}
        sorted_distances = dict(
            sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances.keys())[0]
        st.write('Correct word: ', correct_word)
        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)

        col2.write('Distances:')
        col2.write(sorted_distances)


if __name__ == "__main__":
    main()
