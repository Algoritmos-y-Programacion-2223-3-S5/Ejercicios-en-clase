from employees import Writer, Boss
from section import Section

def read_newspaper():
    pass

def add_writer(writter_list):
    writter_list.append(
        Writer(
            input("Please enter the writer name: "),
            input("Please enter the writer dni: ")
        )
    )
    print("Writer added successfully!!")

def add_boss(boss_list):
    boss_list.append(
        Boss(
            input("Please enter the boss name: "),
            input("Please enter the boss dni: ")
        )
    )
    print("Boss added successfully!!")

def create_section(section_list,writers, boss_list):
    section_list.append(
        Section(
            input("Please enter Section name: " ),
            select_boss(boss_list),
            select_writers(writers)
        )
    )
    print("Boss added successfully!!")

def select_boss(boss_list):
    for index, boss in enumerate(boss_list):
        print(f"{index + 1} - {boss.name}")
    boss_selected = int(input("Please enter the boss that you want: "))
    return boss_list[boss_selected - 1]

def select_writers(writer_list):
    writer_list_new = []
    for index, writer in enumerate(writer_list):
        print(f"{index + 1} - {writer.name}")
    while True:
        writer_selected = int(input("Please enter the writer that you want: "))
        writer_list_new.append(writer_list[writer_selected - 1])
        option = input("Do you want to add another writer? (Y-yes / N-No)\n->")
        if option == "N" or option == "n":
            break
    return writer_list_new

def main():
    writter_list = []
    boss_list = []
    section_list = []
    while True:
        option = input("Please enter option \n1-Read Newspaper\n2-Add Writer\n3-Add Boss\n4-Create Section\n5-Create Article\n6-Create Commercial Anouncement\n7 Create Classified Anouncement\n8-Exit\n->")
        if option == "1":
            read_newspaper()
        elif option == "2":
            add_writer(writter_list)
        elif option == "3":
            add_boss(boss_list)
        elif option == "4":
            create_section(section_list, writter_list, boss_list)
        elif option == "5":
            pass
        elif option == "6":
            pass
        elif option == "7":
            pass
        elif option == "8":
            break
        else:
            print("Invalid option")

main()