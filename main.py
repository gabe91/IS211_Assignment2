import argparse
import requests
import datetime
import logging


def downloadData(url):
    response = requests.get(url)
    # return response as text
    return response.text


def processData(file_content):
    person_dict = {}
    for data_line in file_content.split("\n"):
        if len(data_line) == 0:
            continue
        identifier, name, birthday = data_line.split(",")
        if identifier == "id":
            continue
        id_int = int(identifier)
        try:
            real_birthday = datetime.datetime.strptime(birthday, "%d/%m/%Y")
            person_dict[id_int] = (name, real_birthday)
        except ValueError:
            print(f"error parsing {birthday}")
    return person_dict


def displayPerson(id, persoData):
    try:
        print("Person #" + str(idnum) + " is " + persoData[idnum][0] + "with a birthday of " + persoData[idnum][
            1].strftime(
            '%d/%m/%Y'))

    except:
        print("No user ID found ")


if __name__ == "__main__":
    url = "https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv"
    response = downloadData(url)
    results_dict = processData(response)
    idnum = int(input("ID "))
    displayPerson(idnum, results_dict)
    # print(response)
    # print(results_dict[1])
