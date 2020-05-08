def finder(files, queries):
    query_path = {}
    for f in files:
        key = f.rsplit('/', 1)[1]
        value = f
        if key not in query_path:
            query_path[key] = []

        query_path[key].append(f)

    result = []

    for x in queries:
        if x in query_path:
            result += query_path[x]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
