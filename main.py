import random


class Gen:
    def __init__(self):
        self.var = {}

    def fit(self, text):
        x = zip(text, text[1:])
        for p, c in x:
            if p not in self.var.keys():
                self.var[p] = set()
            self.var[p].append(c)

    def gen(self, leng) -> str:
        c = '.'
        res = []
        while True:
            nw = list(self.var[c])
            c = random.choice(nw)
            res.append(c)
            if c == '.':
                if len(res) > leng:
                    return " ".join(res)


def read() -> list:
    text = []
    with open("twilight.txt", encoding="windows-1251") as doc:
        lines = doc.readlines()
        for i in lines:
            for w in i.strip().split():
                nw = ''
                for let in w:
                    if let.isalnum():
                        nw += let.lower()
                text.append(nw)
                if w[-1] == '.':
                    text.append('.')
    return text


a = Gen()
a.fit(read())
final = a.gen(500)
print(final)
