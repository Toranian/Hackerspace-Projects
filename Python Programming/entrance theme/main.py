while True:
    select_file = input("file name: ")

    try:
        with open("{}.txt".format(select_file)) as file:
            data = file.read()
            print(data)
    except:
        print("failed")
