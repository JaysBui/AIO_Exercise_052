#Bài 1:

def f1_score_classification(tp, fp, fn):
    metrics = {"tp": tp, "fp": fp, "fn": fn}
    for k, v in metrics.items():
        if not isinstance(v, int):
            print(f"{k} must be int")
            return None
        if v <= 0:
            print(f"{k} must be greater than or equal to Zero")
            return None
    precision= tp / (tp + fp)
    recall= tp / (tp + fn)
    f1_score = 2 * (precision * recall)/ (precision + recall)
    print(f'Precision is {precision}')
    print(f"Recall is {recall}")
    print(f'F1 score is {f1_score}')
    return precision, recall, f1_score

if __name__ == "__main__":
    f1_score_classification(tp=2, fp=3, fn=4)
    f1_score_classification(tp='a', fp=3, fn=4)
    f1_score_classification(tp=2, fp='a', fn=4)
    f1_score_classification(tp=2, fp=3, fn='a')
    f1_score_classification(tp=2, fp=0, fn=4)