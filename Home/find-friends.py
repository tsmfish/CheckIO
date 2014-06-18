__author__ = 'Pavel.Malko'

def check_connection(network, first, second):
    friends = {}

    def unionList(firstList, secondList):
        for friend in friends[secondList]:
            friends[firstList].append(friend)
        friends.pop(secondList)

    def findFriendList(who):
        if len(friends) == 0: return None
        for listName, list in friends.items():
            if who in list: return listName
        return None

    def pushFriends(who, whitch):
        whoList, whitchList = findFriendList(who), findFriendList(whitch)
        if whoList and whitchList: unionList(whoList, whitchList)
        elif whoList: friends[whoList].append(whitch)
        elif whitchList: friends[whitchList].append(who)
        else: friends[who] = [who,whitch]

    for friendsCupl in network:
        left, rigth = friendsCupl.split('-')
        pushFriends(left, rigth)

    print(friends)
    return findFriendList(first) == findFriendList(second)

print(check_connection(("nikola-robin","batman-nwing","mr99-batman","mr99-robin","dr101-out00","out00-nwing",),"dr101","mr99"))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
