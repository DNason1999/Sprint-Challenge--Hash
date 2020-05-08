def has_negatives(a):
    neg = {k:k*-1 for k in a}
    result = []
    for k in neg:
        if neg[k] in neg:
            if k > 0:
                result.append(k)

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
