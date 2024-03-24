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


def part04():
    app = True
    numberRange = [0, 20, 40, 60, 80, 100, 120]
    studentId = ""
    passCredits = 0
    deferCredits = 0
    failCredits = 0
    studentMarkTotal = 0

    progressCount = 0
    moduleTrailerCount = 0
    moduleRetrieverCount = 0
    excludeCount = 0
    studentsResults = {}

    while app:
        studentId = input("Enter unique student Id: ")
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
            studentsResults[studentId] = f"Progress - {passCredits}, {deferCredits}, {failCredits}"
            progressCount = progressCount + 1
        elif passCredits == 100:
            print("Progress (module trailer)")
            studentsResults[studentId] = f"Progress (module trailer) - {passCredits}, {deferCredits}, {failCredits}"
            moduleTrailerCount = moduleTrailerCount + 1
        elif passCredits + deferCredits >= 60:
            print("Do not Progress-module retriever")
            studentsResults[studentId] = f"Module retriever - {passCredits}, {deferCredits}, {failCredits}"
            moduleRetrieverCount = moduleRetrieverCount + 1
        elif failCredits >= 80:
            print("Exclude")
            studentsResults[studentId] = f"Exclude - {passCredits}, {deferCredits}, {failCredits}"
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
    # Print key and value of each item in the dictionary
    for id, record in studentsResults.items():
        print(f"{id} : {record}")

part04()