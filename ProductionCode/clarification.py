"""
For very common words, such as malignant neoplasms, add paranthetical explination
"""
def clarify(cause):
    keywords = ["malignant neoplasms"]
    additions = ["cancer"]
    i = 0
    for keyword in keywords:
        if keyword in cause:
            cause = cause.split(keyword)
            addition = f" ({additions[i]})"
            cause = cause[0]+keyword+addition+cause[1]
        i += 1
    return cause





