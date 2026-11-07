import string

txt = """

"""
def word_count(txt):
    wrds = []
    for w in txt.replace("  ", " ").replace("\n", " ").strip().split(" "):
        if not (w == "") and (any(c in list(w) for c in list(string.ascii_lowercase)+list(string.ascii_uppercase)+[str(i) for i in [0,1,2,3,4,5,6,7,8,9]])):
            wrds.append(w)
    return wrds

if __name__ == "__main__":
    wrds = word_count(txt)
    print(wrds)
    print(len(wrds))
