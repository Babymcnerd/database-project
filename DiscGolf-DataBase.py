#!/usr/bin/python

import psycopg2

loggedInUsername = ""
loggedIn = False

conn = psycopg2.connect(
    host="localhost",
    dbname="disks-db",
    user="postgres",
    password="password",
    port="5432",
)
cur = conn.cursor()

commands = {
    "signup": "signup username password",
    "login": "login username password",
    "addBag": "addBag bagname",
    "addDisc": "addDisc discname bagname",
    "showPlayer": "showPlayer playername",
    "showDiscs": "",
    "showPros": "",
    "showBag": "showBag bagname",
    "help": "help",
    "quit": "",
}


def init():
    # STUFF DONE HERE

    cur.execute(
        """CREATE TABLE IF NOT EXISTS bag (
        bagid VARCHAR(255) PRIMARY KEY,
        numberofdiscs INT,
        bagname VARCHAR(255),
        owner VARCHAR(255) 
    );
    """
    )

    cur.execute(
        """CREATE TABLE IF NOT EXISTS discsinbag (
        b1 VARCHAR(255),
        b2 VARCHAR(255),
        b3 VARCHAR(255),
        b4 VARCHAR(255),
        b5 VARCHAR(255),
        b6 VARCHAR(255),
        b7 VARCHAR(255)
    );
    """
    )

    cur.execute(
        """CREATE TABLE IF NOT EXISTS person (
        name VARCHAR(255),
        username VARCHAR(255) PRIMARY KEY,
        password VARCHAR(255)
    );
    """
    )

    cur.execute(
        """CREATE TABLE IF NOT EXISTS company (
        name VARCHAR(255) PRIMARY KEY,
        hqlocation VARCHAR(255)
    );
    """
    )

    cur.execute(
        """CREATE TABLE IF NOT EXISTS proplayer (
        playerid VARCHAR(255) PRIMARY KEY,
        ranking INT,
        name VARCHAR(255),
        bagid VARCHAR(255),
        companyname VARCHAR(255)
    );
    """
    )

    cur.execute(
        """CREATE TABLE IF NOT EXISTS disc (
        speed INT,
        glide INT,
        turn INT,
        fade INT,
        material VARCHAR(255),
        name VARCHAR(255),
        discid VARCHAR(255) PRIMARY KEY 
    );
    """
    )

    cur.execute(
        """INSERT INTO disc (speed, glide, turn, fade, material, name, discid) VALUES
    (14, 4, -1, 3, 'ST', 'FIRESTORM', 'D1'),
    (12, 2, -2, 3, 'GS', 'CORVETTE', 'D2'),
    (5, 3, -3, 3, 'GS', 'KRAIT', 'D3'),
    (9, 1, -4, 3, 'GS', 'COLUSSUS', 'D4'),
    (12, 5, -2, 3, 'ES', 'APE', 'D5'),
    (11, 2, -5, 3, 'XT', 'BOSS', 'D6'),
    (14, 1, -1, 3, 'PR', 'SHRYKE', 'D7'),
    (7, 1, -1, 3, 'RP', 'ORC', 'D8'),
    (7, 1, -1, 3, 'DX', 'HAWKEYE', 'D9'),
    (6, 2, -1, 3, 'DX', 'TL', 'D10'),
    (9, 2, -1, 3, 'DX', 'LEOPARD', 'D11'),
    (10, 3, -2, 3, 'DX', 'VIPER', 'D12'),
    (2, 4, -2, 3, 'MF', 'BANSHEE', 'D13'),
    (14, 1, -3, 3, 'ST', 'LEOPARD3', 'D14'),
    (10, 0, -3, 3, 'ES', 'ARCHANGEL', 'D15'),
    (9, 2, -4, 3, 'ST', 'SPIDER', 'D16'),
    (11, 3, -2, 3, 'ST', 'RAT', 'D17'),
    (10, 3, -1, 3, 'ST', 'COLT', 'D18');
    """
    )

    cur.execute(
        """INSERT INTO proplayer (playerid, ranking, name, bagid, companyname) VALUES
    ('P1', 1, 'Paul McBerth', 'b1', 'INNOVA'),
    ('P2', 6, 'Chad Mcborwick', 'b3', 'GATEWAY'),
    ('P3', 4, 'Andrew Tits', 'b4', 'INNOVA'),
    ('P4', 3, 'Chicken McChicken', 'b7', 'DISCRAFT'),
    ('P5', 2, 'Eagle McMan', 'b6', 'INNOVA'),
    ('P6', 7, 'Simon Lazerzet', 'b2', 'DYNAMICDISCS'),
    ('P7', 5, 'Hannah McBerth', 'b5', 'INNOVA');
    """
    )

    cur.execute(
        """INSERT INTO bag (bagid, numberofdiscs, bagname, owner) VALUES
    ('b1', 4, 'Paul McBerth bag', 'Paul'),
    ('b2', 3, 'Simon Lazerzet bag', 'Simmon'),
    ('b3', 4, 'Chad Mcborwick bag', 'Chad'),
    ('b4', 2, 'Andrew Tits bag', 'Andrew'),
    ('b5', 4, 'Hannah McBerth bag', 'Hannah'),
    ('b6', 4, 'Eagle McMan bag', 'Eagle'),
    ('b7', 3, 'Chicken McChicken bag', 'Chicken');
    """
    )

    cur.execute(
        """INSERT INTO discsinbag (b1, b2, b3, b4, b5, b6, b7) VALUES
    ('D1','D2' ,'D1' ,'D6' ,'D9' ,'D3' ,'D4' ),
    ('D4','D6' ,'D7' ,'D6' ,'D12' ,'D2' ,'D8' ),
    ('D9','D4' ,'D5' , NULL,'D3' ,'D7' ,'D1' ),
    ('D10',NULL ,'D3' ,NULL ,'D3' ,'D1' , NULL);
    """
    )

    cur.execute(
        """INSERT INTO person (name, username, password) VALUES
    ('Paul McBerth', 'Paul McBerth',''),
    ('Chad Mcborwick', 'Chad Mcborwick',''),
    ('Andrew Tits', 'Andrew Tits',''),
    ('Chicken McChicken', 'Chicken McChicken',''),
    ('Eagle McMan', 'Eagle McMan',''),
    ('Simon Lazerzet', 'Simon Lazerzet',''),
    ('Hannah McBerth', 'Hannah McBerth','');
    """
    )

    cur.execute(
        """INSERT INTO company (name, hqlocation) VALUES
    ('INNOVA', 'ST LOUIS MISSOURI'),
    ('GATEWAY', 'AUTIN TEXAS'),
    ('DISCRAFT', 'WACO TEXAS'),
    ('DYNAMICSDISCS', 'NEY YORK NEY YORK');
    """
    )

    conn.commit()
    # STUFF DONE HERE


def close():
    conn.commit()
    cur.close()
    conn.close()


def HandleUserInput():
    global commands
    global loggedIn
    userinput = input()
    userinput = userinput.split()
    if not userinput:
        return
    command = userinput[0]
    userinput.remove(command)
    if command == "login" and int(len(userinput)) == 2:
        login(userinput[0], userinput[1])
        return
    elif command == "help":
        StartPrint()
        return
    elif command == "quit":
        close()
        exit()
    elif command == "signup" and int(len(userinput)) == 2:
        signup(userinput[0], userinput[1])
        return
    elif command == "addBag" and loggedIn and int(len(userinput)) == 1:
        addBag(userinput[0])
        return
    elif command == "addDisc" and int(len(userinput)) == 2:
        addDisc(userinput[0], userinput[1])
        return
    elif command == "showPlayer" and int(len(userinput)) == 1:
        showPlayer(userinput[0])
        return
    elif command == "showBag" and int(len(userinput)) == 1:
        showBag(userinput[0])
        return
    elif command == "showBag" and not userinput:
        printUserBag()
        return
    elif command == "showDiscs" and not userinput:
        showDiscs()
        return
    elif command == "showPros" and not userinput:
        showPros()
        return
    if command in commands:
        print(f"command {command} contains input fields please try again")
    else:
        print(
            f'command {command} is not a command please try again or use the command "help" for a list of command you can use'
        )


def printUserBag():
    if not loggedIn:
        print(
            "You must be logged in to use this command. Please login with 'login username password'."
        )
        return
    query = f"SELECT bagname FROM bag WHERE owner='{loggedInUsername}'"
    cur.execute(query)
    response = cur.fetchall()
    if len(response) != 0:
        print(f"bags: \n{response}")
    else:
        print(f'you have no bags to make a bag use the "addBag" command')


def login(usernameinput, passwordinput) -> bool:
    global loggedIn
    global loggedInUsername
    checkinput = f"SELECT username FROM person WHERE username='{usernameinput}' and password='{passwordinput}';"
    cur.execute(checkinput)
    checkinputreturn = cur.fetchone()
    NoneType = type(None)
    if not isinstance(checkinputreturn, NoneType):
        loggedIn = True
        print(f"User {usernameinput} succesfully logged in")
        loggedInUsername = checkinputreturn[0]
    else:
        print(
            f"User {usernameinput} is not a user to signup use the command: signup username password"
        )


def signup(usernameinput, passwordinput):
    cur.execute(f"""SELECT username FROM person WHERE username='{usernameinput}'""")
    response = cur.fetchall()
    if not response:
        cur.execute(
            f"""INSERT INTO person (username, password) VALUES ('{usernameinput}', '{passwordinput}');"""
        )
        conn.commit()


def showDiscs():
    query = f"SELECT name FROM disc"
    cur.execute(query)
    response = cur.fetchall()
    print(
        f"these are the disks currently in the database that can be added to your bag: \n{response}"
    )


def addBag(bagName):
    if not loggedIn:
        print(
            "You must be logged in to use this command. Please login with 'login username password'."
        )
        return
    getNumOfBags = f"SELECT * FROM bag"
    cur.execute(getNumOfBags)
    getNumOfBagsreturn = int(len(cur.fetchall()))
    bagid = "b" + str(getNumOfBagsreturn + 1)
    print(f"bagid is at {bagid}")
    query1 = f"INSERT INTO bag (bagid,numberofdiscs,bagname,owner) VALUES ('{bagid}', '{0}', '{bagName}', '{loggedInUsername}');"
    cur.execute(query1)
    conn.commit()
    query2 = f"ALTER TABLE discsinbag ADD {bagid} VARCHAR(255)"
    cur.execute(query2)
    conn.commit()


def addDisc(discname, bagname):
    NoneType = type(None)
    if not loggedIn:
        print(
            "You must be logged in to use this command. Please login with 'login username password'."
        )
        return
    discid = getDiscId(discname)
    if isinstance(discid, NoneType):
        print(f"disc {discname} does not exist")
        return
    checkinput = f"SELECT bagid FROM bag WHERE bagname ='{bagname}' and owner ='{loggedInUsername}';"
    cur.execute(checkinput)
    bagid = cur.fetchone()[0]
    if not isinstance(checkinput, NoneType):
        q3 = f"SELECT numberofdiscs FROM bag WHERE bagname='{bagname}';"
        cur.execute(q3)
        numInBag = cur.fetchone()[0]
        query1 = f"INSERT INTO discsinbag ({bagid}) VALUES ('{discid[0]}');"
        cur.execute(query1)
        conn.commit()
        query2 = f"UPDATE bag SET numberofdiscs={numInBag + 1};"
        cur.execute(query2)
        conn.commit()
        print(f"added disc {discname} into bag {bagname}")
    else:
        print(f"bag {bagname} not exist.")


def showBag(bagname):
    global loggedInUsername
    global loggedIn
    NoneType = type(None)
    if not loggedIn:
        print(
            "You must be logged in to use this command. Please login with 'login username password'."
        )
        return
    query = f"SELECT bagid FROM bag WHERE owner='{loggedInUsername}' and bagname='{bagname}'"
    cur.execute(query)
    bag = cur.fetchone()
    query = f"SELECT {bag[0]} FROM discsinbag"
    cur.execute(query)
    response = cur.fetchall()
    # print(response[0][0])
    for disc in response:
        if disc[0] != None:
            print(f"disc : {getDiscName(disc[0])[0]}")


def showPlayer(proName):
    NoneType = type(None)
    query = f"SELECT bagid FROM bag WHERE owner='{proName}'"
    cur.execute(query)
    bag = cur.fetchone()
    if bag[0] == None:
        print(
            f"either pro {proName} is not in the database or does not have a registered bag"
        )
    query = f"SELECT {bag[0]} FROM discsinbag"
    cur.execute(query)
    response = cur.fetchall()
    # print(response[0][0])
    print(f"the pro player {proName} has the following discs in his bag: ")
    for disc in response:
        if disc[0] != None:
            print(f"disc : {getDiscName(disc[0])[0]}")


def showPros():
    query = f"SELECT name FROM proplayer"
    cur.execute(query)
    response = cur.fetchall()
    print(f"These are pros that have been added to the system: \n{response}")


def getDiscId(discname):
    checkinput = f"SELECT discid FROM disc WHERE name ='{discname}';"
    cur.execute(checkinput)
    discid = cur.fetchone()
    return discid


def getDiscName(discid):
    checkinput = f"SELECT discname FROM disc WHERE name ='{discid}';"
    cur.execute(checkinput)
    discid = cur.fetchone()
    return discid


def getDiscName(discId):
    checkinput = f"SELECT name FROM disc WHERE discid ='{discId}';"
    cur.execute(checkinput)
    discname = cur.fetchone()
    return discname


def StartPrint():
    global commands

    print("\nCOMMANDS:")
    for cmd, usage in commands.items():
        print(f"\t{cmd.ljust(12)}{usage}")

    print("\nEXAMPLE USAGE:")
    print("To signup, use the following command:")
    print("\tsignup johndoe password123\n")
    print("=" * 40)


def main():
    print("=" * 40)
    print("DISC GOLF DATABASE".center(40))
    print("=" * 40)
    # init()
    StartPrint()
    while True:
        HandleUserInput()


if __name__ == "__main__":
    main()
