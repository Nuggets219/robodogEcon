import io
econArchive = open("econarchive.txt", "r", encoding="utf-8") #opening in read mode so its harder to accidentally erase the whole chat's history.
users = {}
for i in econArchive:
    if len(i) > 0:
        currentUser = i.split("?")
        users[currentUser[0]] = int(currentUser[1])

def formatNumber(num:int) -> str:
    return f'{num:,}'

def sayPoints(user):
    if user.lower() in users:
        print(f"{user} has {formatNumber(users[user.lower()])} points!")

def setPoints(user : str,points : int):
    global users
    users[user.lower()] = points

def changePoints(user : str,diff : int):
    global users
    users[user.lower()] += diff

def saveAndQuit():
    global users,econArchive
    econArchive.close()
    econArchive = io.open('econarchive.txt','w')
    for name in users:
        econArchive.writelines(f'{name}?{users[name]}\n')
    econArchive.close()
    
while True:
    exec(input()) #Here for testing purposes

"""
broadcaster?10032
user1?1234
user2?1337

"""