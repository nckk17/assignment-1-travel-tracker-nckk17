"""
Replace the contents of this module docstring with your own details
Name:Nay chi Ko Ko
Date started:8/9/2020
GitHub URL:
"""
import csv
from operator import itemgetter


def main():
    print("Travel Tracker 1.0 - by <Your Name>")
    my_files = open("places.csv", "r")
    info = my_files.readlines()
    blah = read_file(info)  # formart 4

    my_files.close()
    print("{}  places loaded from places.csv".format(len(blah)))

    while True:
        blah.sort(key=itemgetter(2)) #For sort list in order of priority
        menu()
        menus = str(input(">>>")).upper()

        if menus == "L":
            display_list(blah)

        elif menus == "A":
            new_place = add_place()
            blah.append(add_place())
        elif menus == "M":
            display_list(blah)
            mark_place(blah)
        elif menus == "Q":
            for_save_place(blah)
            break
        else:
            print("Invald")


def menu():
    """For display menu"""
    print("Menu:")
    print("L - List places")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")


def read_file(info):  # for read file
    """For list place"""

    place_list = []

    for a in info:
        place_list.append(a.strip().split(","))  # place data append to the place_list

    for priority in place_list:  # priority string convert into int
        priority[2] = int(priority[2])

    for n in place_list:  #
        if n[3] == "v":  # v means visited place and marking with blank
            n[3] = " "
        elif n[3] == "n":  # n means unvisited place and marking with start
            n[3] = "*"

    return place_list


def display_list(blah):
    for places, p in enumerate(blah):
        print("{} {}. {:30} - {:15} ({})".format(p[3], places, p[0], p[1], p[2]))  # Prints list in table format
    # blah is the place list
    all_places = 0
    unvisted = 0
    for p in blah:
        all_places = len(blah)
        count = p.count("*")
        unvisted = unvisted + count
    visited = all_places - unvisted

    if unvisted == 0:
        print("No places left to visit.")
    else:
        print(visited, "places. You still want to visited", unvisted, "place")




def mark_place(blah): #for mark a place as visited
    print("Enter the number of a place to mark as visited")
    while True:
        try:
            numberOfPlace = int(input(">>> "))#for the user input
            count_place = len(blah)

            if numberOfPlace > count_place:
                print("Invalid place number")

            elif numberOfPlace < 0:
                print("Number must be >= 0")

            else:
                for p in blah[numberOfPlace:numberOfPlace + 1]:
                    if p[3] == " ":
                        print("No unvisited places", p[0])
                    else:
                        p[3] = " "
                        print(p[0], "by", p[1], "visited")
                break

        except ValueError:
            print("Invalid input; enter a valid number")


def add_place():  # for add the new place
    place_list = []
    while True:
        try:
            name = input("Name: ")  # ask for name
            if not name:
                print("Input can not be blank")
            else:
                break
        except ValueError:
            print("Invalid input, enter a valid name")

    while True:
        try:
            country = input("Country: ")  # ask for the country
            if not country:
                print("Input can not be blank")
            else:
                break
        except ValueError:
            print("Invalid input,enter a valid name")
    while True:
        try:
            priority = int(input(' priority: '))  # Ask user priority number
            if priority < 0:
                print(" priority must be >= 0")
            else:
                break

        except ValueError:
            print("Invalid input; enter a valid  priority")

        # For append input to list
    place_list.append(name)
    place_list.append(country)
    place_list.append(priority)
    place_list.append("*")
    # Uluru in Australia (priority 2) added to Travel Tracker
    print(name, "in", country, "(", priority, ")", "added to Travel Tracker")
    return place_list

def for_save_place(blah):  # for save the placec and write
    my_files = open("places.csv", "w")
    for p in blah:
        if p[3] == "*":
            p[3] = "n"
        elif p[3] == " ":
            p[3] = "v"
    for i in blah:
        print(i[0] + ",", i[1], ",", i[2], ",", i[3], file=my_files)  # Removes white spaces from list

    my_files.close()
    all_places = len(blah)

    print(all_places, "place saved to places.csv")
    print("Have a nice day :)")


if __name__ == '__main__':
    main()
