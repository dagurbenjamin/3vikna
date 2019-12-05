from UIMAIN import UIMAIN


class AlldestinationsmenuUI():

    def __init__(self):
        pass
    #taka inn destination ut fra inputti fra fyrri sidu
    def print_all_destination_info_menu(self, destination_dict):
        print('****************************************************************')
        print('                                                                ')
        print('		        NaN Air                "q" - quitAndSave           ')
        print('                                                                ')
        print('****************************************************************')
        print('                                                                ')
        print('           ----------------------------------------             ')
        print('                     Destination: {}-{}                          '.format())
        print('           ----------------------------------------             ')
        print('                                                                ')
        print('   Airport                Country              Distance         ')
        print(' -----------            ----------            ----------        ')
        print('   {} airport           {}                      {} km           ')
        print('                                                                ')
        print('  Contact name         Emergency Number       Flight Time       ')
        print(' --------------       ------------------      ------------      ')
        print('                                                                ')
        print(' Destination number                                             ')
        print(' -------------------                                            ')
        print('        {}                                                      ')
        print('                                                                ')
        print('                                                                ')
        print('                                                                ')
        print('Back to main menu............"mm"                               ')
        print('Back to sub menu............."sm"                               ')
        print('Back one page................"bp"                               ')


a = UIMAIN().get_all_destinations()
print(a['GOH']['country'])
b = AlldestinationsmenuUI()


