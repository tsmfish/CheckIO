__author__ = 'Pavel.Malko'

def check_connection(network, first, second):
    friends = {}

    def unionList(firstList, secondList):
        if firstList == secondList: return
        tempList = friends.pop(secondList)
        for friend in tempList:
            friends[firstList].append(friend)

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
print(check_connection(("scout1-scout3","plane1-robin","scout3-sscout","scout1-base","pingin-scout1","sscout-base","scout3-plane1","scout3-robin","plane1-nikola","plane1-pingin","base-scout3","plane1-sobhia","base-pingin","scout3-sobhia","robin-stevan","robin-base","nikola-robin","sobhia-sscout","stevan-sscout","robin-sobhia","robin-sscout","pingin-sscout","scout3-nikola","nikola-base","plane1-scout1","plane1-base","sscout-plane1","sobhia-scout1","sscout-scout1","robin-pingin","pingin-stevan","pingin-sobhia","scout3-pingin","nikola-sscout","nikola-pingin","stevan-base","stevan-scout1","scout1-nikola","nikola-sobhia","stevan-sobhia","stevan-scout3","scout1-robin","nikola-stevan","sobhia-base","stevan-plane1",),"pingin","sobhia"))

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
