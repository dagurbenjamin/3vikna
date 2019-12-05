from UILayer.UIMAIN import UIMAIN

class DestinationInfoMenuUI():

    def __init__(self):
        pass
    #taka inn destination ut fra inputti fra fyrri sidu
    def print_all_destination_info_menu(self,id, destination_dict):
        print('****************************************************************')
        print('                                                                ')
        print('		        NaN Air                "q" - quitAndSave           ')
        print('                                                                ')
        print('****************************************************************')
        print('                                                                ')
        print('           ----------------------------------------             ')
        print('                 Destination: {}-{}                          '.format(destination_dict[id]['country'],destination_dict[id]['destination']))
        print('           ----------------------------------------             ')
        print('                                                                ')
        print('   Airport                Country              Distance         ')
        print(' -----------            ----------            ----------        ')
        print('   {} airport           {}            {} km           '.format(destination_dict[id]['destination'],destination_dict[id]['country'],destination_dict[id]['distance']))
        print('                                                                ')
        print('  Contact name         Emergency Number       Flight Time       ')
        print(' --------------       ------------------      ------------      ')
        print('   {}             {}             {}               '.format(destination_dict[id]['contactname'],destination_dict[id]['emergencynumber'],destination_dict[id]['flighttime']))
        print('                                                                ')
        print(' Destination number                                             ')
        print(' -------------------                                            ')
        print('        {}                                                      '.format(destination_dict[id]['destinationnumber']))
        print('                                                                ')
        print('                                                                ')
        print('Back to main menu............"mm"                               ')
        print('Back to sub menu............."sm"                               ')
        print('Back one page................"bp"                               ')
        input_command = input('Enter input command: ')
        if input_command == 'mm':
            pass
            
            


