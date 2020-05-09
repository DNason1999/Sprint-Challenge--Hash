def intersection(arrays):
    # total = [j for i in arrays for j in arrays]

    # result = []

    # for x in arrays[0]:
    #     if total.count(x) == len(arrays):
    #         result.append(x)

    # return result

    int_counts = {}
    for arr in arrays:
        for x in arr:
            if x not in int_counts:
                int_counts[x] = 0
            
            int_counts[x] += 1

    result = []

    for key,value in int_counts.items():
        if value == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
