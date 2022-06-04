"""
For very common words, such as malignant neoplasms, add paranthetical explination
"""
def clarify(cause):
    keywords = [", unspecified - Malignant neoplasms"," - Malignant neoplasms", "Malignant neoplasm "]
    additions = ["cancer", "cancer","cancer"]
    i = 0
    for keyword in keywords:
        if keyword in cause:
            cause = cause.split(keyword)
            addition = f" {additions[i]} "
            cause = cause[0]+addition+cause[1]
        i += 1
    return cause