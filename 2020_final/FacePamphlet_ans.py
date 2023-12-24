class FacePamphlet:
    # Your code starts here
    def __init__(self, username):
        self.__username = username
        self.friends = []
        self.status_history = {}
    
    def add_friend(self, friend):
        self.friends.append(friend)
        print(self.__username, 'added:', friend.get_username())
    
    def post(self, status):
        index = len(self.status_history) + 1
        self.status_history[index] = status
        print(self.__username + ' posted \\' + status + '\\')
    
    def set_username(self, new_name):
        print('Name changed from "' + str(self.__username) + '" to"' + new_name + '"')
        self.__username = new_name
    
    def get_username(self):
        return self.__username
    
    def get_status_history(self):
        return self.status_history
    
    def get_friend_list(self):
        friends_str = '['
        for friend in self.friends:
            friends_str += friend.get_username()
            friends_str += ', '
        friends_str = friends_str[0:len(friends_str) - 2]
        friends_str += ']'
        return friends_str


def main():
    jerry = FacePamphlet('Jerry Liao')
    jerry.post('sleeping')
    jerry.set_username('stanCode Jerry')
    nienti = FacePamphlet('Nienti')
    jerry.add_friend(nienti)
    print(jerry.get_username())
    jerry.post('coding life')
    status_dict = jerry.get_status_history()
    print(status_dict)
    sally = FacePamphlet('Sally Huang')
    jerry.add_friend(sally)
    print(jerry.get_friend_list())


if __name__ == '__main__':
    main()
