# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1953600 # Date: 12/12/2022


def printHistogram(progress, moduleTrailer, moduleRetriever, exclude):
    # Histogram
    print("---------------------------------------------------------------")
    print("Histogram")

    print("Progress ", progress, " : ", end=" ")
    for result in range(progress):
        print("*", end="")
    print("")

    print("Trailer ", moduleTrailer, "  : ", end=" ")
    for result in range(moduleTrailer):
        print("*", end="")
    print("")

    print("Retriever ", moduleRetriever, ": ", end=" ")
    for result in range(moduleRetriever):
        print("*", end="")
    print("")

    print("Excluded ", exclude, " : ", end=" ")
    for result in range(exclude):
        print("*", end="")
    print("")

    print("")
    print(progress + moduleRetriever + moduleTrailer + exclude, "outcomes in total.")
    print("---------------------------------------------------------------")


def part01():
    app = True
    numberRange = [0, 20, 40, 60, 80, 100, 120]
    passCredits = 0
    deferCredits = 0
    failCredits = 0
    studentMarkTotal = 0

    progressCount = 0
    moduleTrailerCount = 0
    moduleRetrieverCount = 0
    excludeCount = 0

    while app:
        while studentMarkTotal != 120:
            while True:
                try:
                    passCredits = int(input("Enter your total PASS credits: "))
                    if passCredits in numberRange:
                        studentMarkTotal = studentMarkTotal + passCredits
                        break
                    else:
                        print("Out of Range")
                except ValueError:
                    print("Integer Required")

            while True:
                try:
                    deferCredits = int(input("Enter your total DEFER credits: "))
                    if deferCredits in numberRange:
                        studentMarkTotal = studentMarkTotal + deferCredits
                        break
                    else:
                        print("Out of Range")
                except ValueError:
                    print("Integer Required")

            while True:
                try:
                    failCredits = int(input("Enter your total FAIL credits: "))
                    if failCredits in numberRange:
                        studentMarkTotal = studentMarkTotal + failCredits
                        break
                    else:
                        print("Out of Range")
                except ValueError:
                    print("Integer Required")

            if studentMarkTotal != 120:
                studentMarkTotal = 0
                print("Total Incorrect")
            else:
                break

        if passCredits == 120:
            print("Progress")
            progressCount = progressCount + 1
        elif passCredits == 100:
            print("Progress (module trailer)")
            moduleTrailerCount = moduleTrailerCount + 1
        elif passCredits + deferCredits >= 60:
            print("Do not Progress-module retriever")
            moduleRetrieverCount = moduleRetrieverCount + 1
        elif failCredits >= 80:
            print("Exclude")
            excludeCount = excludeCount + 1
        print("")
        decision = input(
            "Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
        if decision == "y":
            studentMarkTotal = 0
        elif decision == "q":
            app = False
            break
        else:
            print("Enter either \"q\" or \"y\" ")
        print("")
    printHistogram(progressCount, moduleTrailerCount, moduleRetrieverCount, excludeCount)


def part02():
    app = True
    numberRange = [0, 20, 40, 60, 80, 100, 120]
    studentsResults = []
    passCredits = 0
    deferCredits = 0
    failCredits = 0
    studentMarkTotal = 0

    progressCount = 0
    moduleTrailerCount = 0
    moduleRetrieverCount = 0
    excludeCount = 0

    while app:
        while studentMarkTotal != 120:
            while True:
                try:
                    passCredits = int(input("Enter your total PASS credits: "))
                    if passCredits in numberRange:
                        studentMarkTotal = studentMarkTotal + passCredits
                        break
                    else:
                        print("Out of Range")
                except ValueError:
                    print("Integer Required")

            while True:
                try:
                    deferCredits = int(input("Enter your total DEFER credits: "))
                    if deferCredits in numberRange:
                        studentMarkTotal = studentMarkTotal + deferCredits
                        break
                    else:
                        print("Out of Range")
                except ValueError:
                    print("Integer Required")

            while True:
                try:
                    failCredits = int(input("Enter your total FAIL credits: "))
                    if failCredits in numberRange:
                        studentMarkTotal = studentMarkTotal + failCredits
                        break
                    else:
                        print("Out of Range")
                except ValueError:
                    print("Integer Required")

            if studentMarkTotal != 120:
                studentMarkTotal = 0
                print("Total Incorrect")
            else:
                break

        if passCredits == 120:
            print("Progress")
            studentsResults.append(["Progress", passCredits, deferCredits, failCredits])
            progressCount = progressCount + 1
        elif passCredits == 100:
            print("Progress (module trailer)")
            studentsResults.append(["Progress (module trailer)", passCredits, deferCredits, failCredits])
            moduleTrailerCount = moduleTrailerCount + 1
        elif passCredits + deferCredits >= 60:
            print("Do not Progress-module retriever")
            studentsResults.append(["Module retriever", passCredits, deferCredits, failCredits])
            moduleRetrieverCount = moduleRetrieverCount + 1
        elif failCredits >= 80:
            print("Exclude")
            studentsResults.append(["Exclude", passCredits, deferCredits, failCredits])
            excludeCount = excludeCount + 1
        print("")
        decision = input(
            "Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
        if decision == "y":
            studentMarkTotal = 0
        elif decision == "q":
            app = False
            break
        else:
            print("Enter either \"q\" or \"y\" ")
        print("")
    printHistogram(progressCount, moduleTrailerCount, moduleRetrieverCount, excludeCount)

    for studentResult in studentsResults:
        print(f"{studentResult[0]} - {studentResult[1]}, {studentResult[2]}, {studentResult[3]}")


def part03():
    app = True
    numberRange = [0, 20, 40, 60, 80, 100, 120]
    passCredits = 0
    deferCredits = 0
    failCredits = 0
    studentMarkTotal = 0

    progressCount = 0
    moduleTrailerCount = 0
    moduleRetrieverCount = 0
    excludeCount = 0
    studentsResults = []

    while app:
        while studentMarkTotal != 120:
            while True:
                try:
                    passCredits = int(input("Enter your total PASS credits: "))
                    if passCredits in numberRange:
                        studentMarkTotal = studentMarkTotal + passCredits
                        break
                    else:
                        print("Out of Range")
                except ValueError:
                    print("Integer Required")

            while True:
                try:
                    deferCredits = int(input("Enter your total DEFER credits: "))
                    if deferCredits in numberRange:
                        studentMarkTotal = studentMarkTotal + deferCredits
                        break
                    else:
                        print("Out of Range")
                except ValueError:
                    print("Integer Required")

            while True:
                try:
                    failCredits = int(input("Enter your total FAIL credits: "))
                    if failCredits in numberRange:
                        studentMarkTotal = studentMarkTotal + failCredits
                        break
                    else:
                        print("Out of Range")
                except ValueError:
                    print("Integer Required")

            if studentMarkTotal != 120:
                studentMarkTotal = 0
                print("Total Incorrect")
            else:
                break

        if passCredits == 120:
            print("Progress")
            studentsResults.append(f"Progress - {passCredits}, {deferCredits}, {failCredits} \n")
            progressCount = progressCount + 1
        elif passCredits == 100:
            print("Progress (module trailer)")
            studentsResults.append(f"Progress (module trailer) - {passCredits}, {deferCredits}, {failCredits} \n")
            moduleTrailerCount = moduleTrailerCount + 1
        elif passCredits + deferCredits >= 60:
            print("Do not Progress-module retriever")
            studentsResults.append(f"Module retriever - {passCredits}, {deferCredits}, {failCredits} \n")
            moduleRetrieverCount = moduleRetrieverCount + 1
        elif failCredits >= 80:
            print("Exclude")
            studentsResults.append(f"Exclude - {passCredits}, {deferCredits}, {failCredits} \n")
            excludeCount = excludeCount + 1
        print("")
        decision = input(
            "Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ")
        if decision == "y":
            studentMarkTotal = 0
        elif decision == "q":
            app = False
            break
        else:
            print("Enter either \"q\" or \"y\" ")
        print("")
    printHistogram(progressCount, moduleTrailerCount, moduleRetrieverCount, excludeCount)
    # Write student marks to text file
    dataFile = open("studentsData.txt", 'w')
    dataFile.writelines(studentsResults)
    dataFile.close()
    # Read student marks from text file
    dataFile = open("studentsData.txt", 'r')
    data = dataFile.readlines()
    dataFile.close()

    for record in data:
        print(record, end="")

programVersion = int(input("Enter version number to run (1, 2, 3): "))
if programVersion == 1:
    print("\nVersion 01")
    part01()
elif programVersion == 2:
    print("\nVersion 02 (List)")
    part02()
elif programVersion == 3:
    print("\nVersion 03 (Text File)")
    part03()
else:
    print("Invalid program version")
