"""
For very common words, such as malignant neoplasms, add paranthetical explination
"""
def clarify(cause):
    keywords = ["- Malignant neoplasms", "Malignant neoplasm "]
    additions = ["cancer", "cancer"]
    i = 0
    for keyword in keywords:
        if keyword in cause:
            cause = cause.split(keyword)
            addition = f"({additions[i]}) "
            cause = cause[0]+keyword+addition+cause[1]
        i += 1
    return cause

if __name__ == "__main__":
    list1 = ["Oesophagus, unspecified - Malignant neoplasms", "Malignant neoplasm of prostate"]
    for line in list1:
        print(clarify(line))




