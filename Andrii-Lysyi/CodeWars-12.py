def filter_words(st):
    lr = st.lower()
    lr2 = lr.upper()[0]+lr[1:]
    lr3 = lr2.split()
    return " ".join(lr3)