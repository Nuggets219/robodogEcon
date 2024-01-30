from config import *
import time
import io
econArchive = io.open("econarchive.txt", "r",encoding="utf-8")  # opening in read mode so its harder to accidentally erase the whole chat's history.
users = {} #initialize user list

def attendance(targUser) -> bool: #users must use the !attendance command to add themselves to the users list, and then they can get points from the routine checks.
    for i in econArchive:
        if targUser in i:
            currentUser = i.split("?")
            users[currentUser[0]] = int(currentUser[1])
            return True
    return False

def pointCountdownGiver(points : int):
    for person in users:
        users[person] += points

def pointCountdownInitiator(mins : int):
    global timerEnd, users
    users = users.sorted()
    timerInital = time.time()
    timerEnd = timerInital + mins * 60
def checkPointCountdown() -> object:
    if time.time() >= timerEnd:
        pointCountdownGiver(pointTimerAmount)


def formatNumber(num: int) -> str: #quick formatting for points numbers
    return f'{num:,}'

def register(targUser):
    if targUser not in users:
        users[targUser] = startingPointAmount
        return True
    else:
        return False

def transferBal(targUserOld,targUserNew):
    try:
        attendance(targUserNew) #make sure both users are loaded into the Users list
        attendance(targUserOld)
        users[targUserNew] = users[targUserOld] #transfer balance
        del users[targUserOld] #remove the entry for the old
        printToChat('Balance Transfer Successful!')
    except:
        printToChat('Balance Transfer Failed!')
def sayPoints(targUser):
    if targUser.lower() in users:
        print(f"{targUser} has {formatNumber(users[targUser.lower()])} points!")
        printToChat(f"{targUser} has {formatNumber(users[targUser.lower()])} points!")
    else:
        return False

def giftPoints(sourceUser,targUser,amount):
    if 0 < amount <= users[sourceUser]:
        users[sourceUser] -= amount
        users[targUser] += amount

def setPoints(targUser: str, points: int):
    global users
    users[targUser.lower()] = points


def changePoints(targUser: str, diff: int):
    global users
    users[targUser.lower()] += diff


def saveEconState():
    global users, econArchive

    #overwrite the backup with the archive state at the beginning of the stream
    econArchive = io.open("econarchive.txt", "r",encoding="utf-8")
    econBackup = io.open('econbackup.txt','w',encoding='utf-8')
    for line in econArchive:
        if len(line) > 0:
            econBackup.write(line)
    econBackup.close()
    econArchive.close()
    #overwrite the archive with the current user list
    econArchive = io.open('econarchive.txt','w',encoding='utf-8')
    for name in users:
        econArchive.writelines(f'{name}?{users[name]}\n')
    econArchive.close()



"""
broadcaster?10032
user1?1234
user2?1337

"""