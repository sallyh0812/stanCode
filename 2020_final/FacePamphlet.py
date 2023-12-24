class FacePamphlet:
    def __init__(self, username):
        self.__n = username
        self.__friends = []
        self.__history = {}
        self.__history_i = 0
    
    def post(self, message):
        """
        Input:
                  message (str): Add message to the dictionary that stores history of status.
                         Print out the username followed by ”posted \message\”
        """
        self.__history_i += 1
        self.__history[self.__history_i] = message
        print(f"{self.__n} posted \\{message}\\")
    
    def set_username(self, new_name):
        """
        Input:
                  new_name (str): Changes the old user name to new_name
        """
        old_name = self.__n
        self.__n = new_name
        print(f"Name changed from \"{old_name}\" to \"{new_name}\"")
    
    def add_friend(self, profile):
        """
        Input:
                  profile (FacePamphlet): A FacePamphlet instance that needs to be added
                             as a friend with
        """
        self.__friends.append(profile)
        print(f"{self.__n} added: {profile.get_username()}")
    
    def get_username(self):
        """
        Returns:
                 One of the instance variables that stores the user name
        """
        return self.__n
    
    def get_status_history(self):
        """
        Returns:
                 A dictionary containing keys of type int, values of type str. Keys indicate
                 the order of posts; values hold each status. Let’s say an instance had
                 called post(‘sleeping’), post(‘coding’), post(‘lifting weights’),
                 get_status_history( ) should return a dict looks like:
                 {1: ‘sleeping’, 2: ‘coding’, 3: ‘lifting weights’}
        """
        return self.__history
    
    def get_friend_list(self):
        """
        Returns:
                 A string of friends that is separated by commas. For example,
                 if an instance had friends in a list, [‘Tom’, ‘Jerry’, ‘Bob’], get_friend_list( )
                 returns a string of ‘[Tom, Jerry, Bob]’
        """
        friend_list = "["
        for friend in self.__friends:
            friend_list += friend.get_username()
            if friend != self.__friends[-1]:
                friend_list += ', '
        friend_list += ']'
        return friend_list


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
