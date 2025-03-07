from menu import print_menu, handle_user_input, print_message



if __name__ == "__main__":
    while True:
        option: str = print_menu()
        try:
            handle_user_input(option)
        except ValueError as e:
            print_message(str(e),"INFORMATION", "yellow")
            continue
