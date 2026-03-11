from pathlib import Path
def readmyfilesandfolders():
    path = Path('')
    items = list(path.rglob('*'))
    for i,item in enumerate(items):
        print(f"{i+1} : {item}")

def create_file():
    try: 
        readmyfilesandfolders()
        name = input("Enter your file name: ")
        p = Path(name)
        if not p.exists(): 
            with open(p , "a") as fs:
                data = input("Write what you want to write in the file: ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY")
        else:
            print("The file is already created")
    except Exception as error:
        print("An error occurred as",error)

def read_files():
    try:
        readmyfilesandfolders()
        read_name = input("Enter the name of the file you want to read: ")
        p1 = Path(read_name)
        if p1.exists() and p1.is_file():
            with open(p1 , 'r') as fs:
                data = fs.read()
                print(data)
            print("FILE READED SUCCESSFULLY")
        else:
            print("FILE DOESN'T EXISISTS")
    except Exception as error:
        print(f"An error has been occured as {error}")

def update_file():
    try:
        readmyfilesandfolders()
        print("Press 1 if you wanna to append the file")
        print("Press 2 if you wanna to edit the file's name ")
        print("Press 3 if you wanna overwrite the file")
        choice_update = int(input("Enter your choice: "))
        if choice_update == 1 : 
            name_update = input("Enter the file name you wanna append: ")
            p2 = Path(name_update)
            if p2.exists() and p2.is_file():
                with open(p2 , 'a') as fs:
                    data = input("Enter what you wanna append: ")
                    fs.write(data)
                print("You have successfully appended the file")
            else:
                print("NAME OF THE FILE IS NOT IN THIS REPO")
        elif choice_update == 2:
            name_update_rename = input("Enter the name of the file you wanna edit: ")
            p3 = Path(name_update_rename)
            if p3.exists() and p3.is_file():
                rename_file = input("Enter the new name of the file: ")
                p3_1 = Path(rename_file)
                p3.rename(p3_1)
                print("FILE NAME SUCCESSFULLY CHANGED ")
            else:
                print("NO FILE FOUNDED!!!")
        elif choice_update == 3:
            name_of_file = input("Enter the name of the file you want to overwrite: ")
            p4 = Path(name_of_file)
            if p4.exists() and p4.is_file():
                with open(p4 ,'w') as fr:
                    data = input("Enter the thing you wanna overwrite: ")
                    fr.write(data)
            else:
                print("NO FILE FOUNDED")
    except Exception as error: 
        print(f"AN ERROR OCCURRED AS {error}")

def delete_file():
    try:
        readmyfilesandfolders()
        name_delete = input("Enter the name of the file you want to delete")
        p5 = Path(name_delete)
        if p5.exists() and p5.is_file():
            p5.unlink()
            print("FILE HAS BEEN DELETED SUCCESSFULLY")
        else:
            print("FILE NOT FOUND")
    except Exception as error:
        print(f"AN ERROR HAS OCCURRED AS {error}")

while True:
    print("Press 1 to CREATING a file")
    print("Press 2 for READING a file")
    print("Press 3 for UPDATING a file")
    print("Press 4 for DELETING a file")
    print("Press 5 for EXIT")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_file()
        elif choice == 2:
            read_files()
        elif choice == 3: 
            update_file()
        elif choice == 4: 
            delete_file()
        elif choice == 5:
            print("THANK YOU FOR USING MY PROGRAM")
            break
    except Exception as error:
        print(f"AN ERROR HAS OCCURRED AS {error}")
