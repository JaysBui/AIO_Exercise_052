# Bài 01

def check_intput(lst, k):
    if isinstance(lst, list) == False or k < 1 or isinstance(k, int) == False:
        return False
    else:
        return True


def max_sliding_window(lst, k):
    if check_intput(lst, k) == False:
        print("Check input variables! First input must be List. Second input must be Integer and Its value must be larger or equal to Zero")
        return None
    else:
        len_lst = len(lst)
        max_sliding_window = []
        for idx in range(len_lst):
            window_idx = idx
            ceiling_idx = k + window_idx
            window = []
            if ceiling_idx <= len(lst):
                while window_idx < ceiling_idx:
                    window.append(lst[window_idx])
                    window_idx += 1
                window_max = max(window)
                max_sliding_window.append(window_max)
        print(max_sliding_window)
        return max_sliding_window


num_lst = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]

if __name__ == "__main__":
    max_sliding_window(num_lst, k=3)
