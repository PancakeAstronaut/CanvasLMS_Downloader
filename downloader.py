# Stephen Hengeli
# November 20, 2019
# *****************************************#
# Canvas API File Download CLI Application #
# *****************************************#
# ###########<Package Imports>############*#
# *****************************************#
from configuration import canvasGlobals    #
import subprocess                          #
#                                          #
# *****************************************#
# TODO List for CLIcanvasAPI
# ********************************************************************************************
# Change the course menu to accept a dynamic number of classes like the files display        *
# Change the way courses are found in canvasGlobals                                          *
# Add a Dashboard file that connects different functionalities together                      *
# Write a submitter script                                                                   *
# Write a setup File                                                                         *
# Write a SISNUM getting script                                                              *
# Write instructions HTML about how to get keys and urls.                                    *
# ********************************************************************************************


def file_downloader(classObject, id, name):
    print("--------------------------------------------------")
    print("Are you sure you want to download '{}'?".format(name))
    print("--------------------------------------------------")
    x = input("usr input>")
    if x == "Yes" or x == "yes":
        file = classObject.get_file(id)
        file.download('LMS_downloads/{}'.format(name))
        print("Successfully downloaded '{}'".format(name))
        subprocess.call('./moveto_WebTransfer.sh')
        course_lobby(classObject=classObject)
    else:
        print("File Download Cancelled")
        file_viewer(classObject=classObject)


def file_viewer(classObject):
    file_list = classObject.get_files()
    idlist = []
    idx = 0
    namelist = []
    for id in file_list:
        idlist.append(file_list[idx].id)
        namelist.append(file_list[idx].display_name)
        idx += 1

    print("--------------------------------------------------")
    print("Files Available for {}".format(classObject.name))
    print("--------------------------------------------------")
    idx = 0
    while idx < len(namelist):
        print("{}.) {}".format(str(idx), namelist[idx]))
        idx += 1
    print("--------------------------------------------------")
    print("Choose the number next to the file name to download the file")
    print("--------------------------------------------------")
    x = input("usr input>")
    if int(x) < len(idlist) >= 0:
        file_downloader(classObject=classObject, id=idlist[int(x)], name=namelist[int(x)])
    else:
        print("Input Invalid")
        file_viewer(classObject=classObject)


def course_lobby(classObject):
    print("***** {} *****".format(classObject.name))
    print("--------------------------------------------------")
    print("What would you like to do?.......")
    print("--------------------------------------------------")
    print("1.) Download a File")
    print("2.) Go Back")
    print("--------------------------------------------------")
    x = input("usr input>")
    if x == str(1):
        file_viewer(classObject=classObject)
    elif x == str(2):
        print("******************************************")
        print("*************** Going Back ***************")
        print("******************************************")
        course_menu()
    else:
        print("Accepted input is 1 or 2")
        course_lobby(classObject=classObject)


def fetch_course(choice):
    # Getting Course information from custom Canvas API package
    MGMT418 = canvasGlobals.CANVAS.get_course(canvasGlobals.MGMT418)
    IST440 = canvasGlobals.CANVAS.get_course(canvasGlobals.IST440)
    IST421 = canvasGlobals.CANVAS.get_course(canvasGlobals.IST421)

    if choice == "mgmt418":
        course = MGMT418
    elif choice == "ist440":
        course = IST440
    elif choice == "ist421":
        course = IST421
    elif choice == "Yd2631VV":
        course_names = [MGMT418.name, IST440.name, IST421.name]
        return course_names
    else:
        course = "Error 404: COURSE OBJECT NOT FOUND"

    return course


def course_menu():
    sys_access_key = "Yd2631VV"
    course_name_list = fetch_course(sys_access_key)
    print("--------------------------------------------------")
    print("\t\tChoose a Course to view its files\t\t")
    print("--------------------------------------------------")
    print("1.) {}".format(course_name_list[0]))
    print("2.) {}".format(course_name_list[1]))
    print("3.) {}".format(course_name_list[2]))
    print("--------------------------------------------------")
    selection = "err.404_niner_niner"
    choice = input("usr input>")
    if choice == str(1):
        selection = fetch_course("mgmt418")
    elif choice == str(2):
        selection = fetch_course("ist440")
    elif choice == str(3):
        selection = fetch_course("ist421")
    else:
        print("Accepted input is 1 through 4")
        course_menu()

    course_lobby(classObject=selection)


def about():
    print("******************************************")
    print("*********** About the Author *************")
    print("******************************************")
    print("** Email: stephenCodeProjects@gmail.com **")
    print("** GitHub: https://github.com/PancakeAstronaut **")
    print("****** Uses the 'canvasapi' package ******")
    print("******************************************")
    input("Press any key to return to menu")
    main()


def exit_conf():
    print("******************************************")
    print("***** Are you sure you want to exit? *****")
    print("******************************************")
    print("************* [Y]es or [N]o **************")
    x = input("usr input>")
    if x == "Y" or x == "y" or x == "yes" or x == "Yes":
        print("******************************************")
        print("****** Disconnected from Canvas LMS ******")
        exit("******************************************")
    elif x == "N" or x == "n" or x == "No" or x == "no":
        print("****** Continuing Operation ******")
        pass


def main():

    print("--------------------------------------------------")
    print("\t\tCanvas API Backend File Retriever")
    print("--------------------------------------------------")
    print("What would you like to do?.......")
    print("--------------------------------------------------")
    print("1.) Choose a Course")
    print("2.) About Program")
    print("3.) Exit")
    print("--------------------------------------------------")
    option = input("usr input>")
    if option == str(1):
        course_menu()
    elif option == str(2):
        about()
    elif option == str(3):
        exit_conf()
    else:
        print("Accepted input is 1 or 2")
        main()


if __name__ == '__main__':
    main()
