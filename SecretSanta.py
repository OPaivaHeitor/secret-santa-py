import random
PARTICIPANT_NAMES = []


def pickrandom(participants, NUMBER_OF_PARTICIPANTS):
    i = 0
    while i < NUMBER_OF_PARTICIPANTS:
        j = 0
        flag = 0
        pick = random.randint(0, NUMBER_OF_PARTICIPANTS-1)
        if participants[i]["ID"] == pick:
            flag = 1
        while j < NUMBER_OF_PARTICIPANTS:
            if participants[j]["SECRET SANTA ID"] == pick:
                flag = 1
            j += 1
        if flag == 0:
            participants[i]["SECRET SANTA ID"] = pick
            participants[i]["SECRET SANTA NAME"] = participants[pick]["NAME"]
            i += 1


def printresults(participants, NUMBER_OF_PARTICIPANTS):
    i = 0
    print("PARTICIPANT-SANTA")
    while i < NUMBER_OF_PARTICIPANTS:
        print(participants[i]["NAME"] + "-" +
              participants[i]["SECRET SANTA NAME"])
        i += 1


def main():
    i = 0
    number = int(input("Digite o numero de participantes \n"))
    if i <= 0:
        return
    print("Digite os nomes dos participantes: ")
    while i < number:
        participant_name = input("")
        PARTICIPANT_NAMES.append(participant_name)
        i += 1
    i = 0
    NUMBER_OF_PARTICIPANTS = len(PARTICIPANT_NAMES)

    participants = []
    while i < NUMBER_OF_PARTICIPANTS:
        participants.append({
            "ID": i,
            "NAME": PARTICIPANT_NAMES[i],
            "SECRET SANTA ID": 99999,
            "SECRET SANTA NAME": "",
        })
        i += 1
    print("\n\n")
    pickrandom(participants, NUMBER_OF_PARTICIPANTS)
    printresults(participants, NUMBER_OF_PARTICIPANTS)


main()
