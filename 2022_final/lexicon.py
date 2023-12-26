class Lexicon:
    def __init__(self):
        self.words = []
    
    def add_word(self, new_w):
        if new_w not in self.words:
            self.words.append(new_w)
        else:
            print(f"{new_w} had been added.")
    
    def search(self, search_w):
        if search_w in self.words:
            return True
        for w in self.words:
            if len(search_w) == len(w):
                for i in range(len(w)):
                    if search_w[i] != w[i] and search_w[i] != '.':
                        return False
                return True
        return False


def main():
    lexicon = Lexicon()
    lexicon.add_word('apple')
    lexicon.add_word('beef')
    print(lexicon.words)
    print(lexicon.search('apple'))
    print(lexicon.search('app'))
    print(lexicon.search('app..'))
    print(lexicon.search('.....'))
    print(lexicon.search('...'))
    print(lexicon.search('.p.l.'))


if __name__ == '__main__':
    main()