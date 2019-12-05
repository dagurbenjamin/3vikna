from UIMAIN import UIMAIN
from DestinationInfoMenuUI import DestinationInfoMenuUI

class AllDestinationsMenuUI():

    def __init__(self):
        pass
    
    def print_all_destinations_menu(self):
        print('****************************************************************')
        print('                                                                ')
        print('		        NaN Air                "q" - quitAndSave           ')
        print('                                                                ')
        print('****************************************************************')
        print('                                                                ')
        print('           ----------------------------------------             ')
        print('                     All Destinatinons                          ')
        print('           ----------------------------------------             ')
        print('                                                                ')
        print('            City/Country		Input Command                      ')
        print('            -------------	      -----------------            ')
        print('                                                                ')
        print('            Nuuk/Greenland.................."1"                 ')
        print('                                                                ')
        print('            Kulusuk/Greenland..............."2"                 ')
        print('                                                                ')
        print('            Torshavn/Faroe islands.........."3"                 ')
        print('                                                                ')
        print('            Tingwall/Shetland..............."4"                 ')
        print('                                                                ')
        print('            Longyearbyen/Svalbard..........."5"                 ')
        print('                                                                ')
        print('                                                                ')
        print('                                                                ')
        print('Back to main menu............"mm"                               ')
        print('Back to sub menu............."sm"                               ')
        print('Back one page................"bp"                               ')
        destination_choice = input("Enter input command: ")
        print('                                                                ')
        print('                                                                ')
        print('                                                                ')
        print('                                                                ')
        all_destinations = UIMAIN().get_all_destinations()
        if destination_choice == '1':
            destination_choice = 'GOH'
        elif destination_choice == '2':
            destination_choice = 'KUS'
        elif destination_choice == '3':
            destination_choice = 'FAE'
        elif destination_choice == '4':
            destination_choice = 'LWK'
        elif destination_choice == '5':
            destination_choice = 'LYR'
        a = DestinationInfoMenuUI().print_all_destination_info_menu(destination_choice,all_destinations)


