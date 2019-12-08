from ui.MainMenuUI import Mainmenu

class UIMAIN():
    def __init__(self):
        pass
    def get_all_destinations(self):
        all_destinations_dict = LLAPI().get_all_destinations()
        return all_destinations_dict
    def main_menu(self):
        menu = Mainmenu()
        b = menu.print_main_menu
        input_command = ""
        while input_command != "q":
            #if input_command == "1":



