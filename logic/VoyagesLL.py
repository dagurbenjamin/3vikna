
from iolayer.VoyagesIO import VoyagesIO
import datetime
import time
from logic.AirplanesLL import AirplanesLL
from iolayer.CrewIO import CrewIO
from logic.EmployeesLL import EmployeesLL


class VoyagesLL():
    def __init__(self, a_str=''):
        self.a_str = a_str

    def create_voyage(self, new_voyage_list):
        new_voyage_str = ','.join(new_voyage_list)
        VoyagesIO().write_in_voyages_flights(new_voyage_str)

    def update_one_voyage(self, number_voyage_to_change, replacement_value, index_to_replace):
        one_voyage = VoyagesIO().load_voyages_from_file(number_voyage_to_change)
        if index_to_replace == 4 or index_to_replace == 5:
            if VoyagesLL().check_if_pilot_has_licence_for_plane(replacement_value, one_voyage):
                employees_working_same_day = EmployeesLL().employees_working(one_voyage.get_date())
                if replacement_value in employees_working_same_day:
                    return print('cant add employee, hes working this day')
                else:
                    list_voyage[index_to_replace] = replacement_value
                    VoyagesLL().change_the_big_voyage_list(number_voyage_to_change, list_voyage)
            else:
                return False

    def change_the_big_voyage_list(self, number_voyage_to_change, new_list_voyage, input_value='0'):
        all_voyages = VoyagesIO().load_voyages_from_file(input_value)
        all_voyages_list = []
        for voyage in all_voyages:
            str_voyage = str(voyage)
            list_voyage = str_voyage.split(',')
            if list_voyage[0] == number_voyage_to_change:
                list_voyage = new_list_voyage
            all_voyages_list.append(list_voyage)
        header = ['voyageID', 'planeInsignia', 'date', 'destination', 'captain',
                  'copilot', 'FlightServiceManager', 'flightAttendant']
        all_voyages_list.insert(0, header)
        VoyagesIO().overwrite_voyage_file(all_voyages_list)

    def is_voyage_fully_staffed(self, voyageID):
        voyages = VoyagesIO().load_voyages_from_file(voyageID)
        for line in voyages:
            str_voyage = str(line)
            list_voyage = str_voyage.split(',')
            if list_voyage[4] == 'x' or list_voyage[5] == 'x' or list_voyage[6] == 'x' or list_voyage[7] == 'x':
                return print('Voyage is not fully staffed!')
            else:
                return print('Voyage is fully staffed!')

    def get_voyages(self):
        all_voyages = VoyagesIO().load_voyages_from_file('0')
        a_list = []
        for voyage in all_voyages:
            str_voyage = str(voyage)
            list_voyage = str_voyage.split(',')
            list_of_voyages = list_voyage
            a_list.append(list_of_voyages)
        return a_list

    def get_one_voyage(self, voyageID):
        one_voyage = VoyagesIO().load_voyages_from_file(voyageID)
        return one_voyage

    def list_voyages_by_day(date, the_input='0'):
        all_voyages = VoyagesIO().load_voyages_from_file(the_input)
        for line in all_voyages:
            str_voyage = str(line)
            list_voyage = str_voyage.split(',')
            if list_voyage[2] == date:
                str_voyage = str(line)
                list_voyage = str_voyage.split(',')
                print(line)
                if list_voyage[4] == 'x' or list_voyage[5] == 'x' or list_voyage[6] == 'x' or list_voyage[7] == 'x':
                    print('Voyage is not fully staffed!')
                else:
                    print('Voyage is fully staffed!')

    def list_voyages_by_week(self, weeknumber, the_input='0'):
        WEEK = weeknumber - 2  # as it starts with 0 and you want week to start from sunday
        startdate = time.asctime(time.strptime('2019 %d 0' % WEEK, '%Y %W %w'))
        startdate = datetime.datetime.strptime(
            startdate, '%a %b %d %H:%M:%S %Y')
        dates = [startdate.strftime('%Y-%m-%d')]
        for i in range(1, 7):
            day = startdate + datetime.timedelta(days=i)
            dates.append(day.strftime('%Y-%m-%d'))
        all_voyages = VoyagesIO().load_voyages_from_file(the_input)
        all_voyages_in_that_week = []
        for line in all_voyages:
            str_voyage = str(line)
            list_voyage = str_voyage.split(',')
            if list_voyage[2] in dates:
                all_voyages_in_that_week.append(list_voyage)
        return all_voyages_in_that_week

    def check_if_pilot_has_licence_for_plane(self, pilot_ssn, one_voyage):
        all_airplanes = AirplanesLL().get_all_airplanes()
        plane_insignia = one_voyage.get_planeInsignia()
        for line in all_airplanes:
            for val in line:
                if val == plane_insignia:
                    planeTypeID = line[1]
        all_pilots = CrewIO().load_pilot_or_cabincrew('Pilot')
        for pilot in all_pilots:
            if pilot.get_social() == pilot_ssn:
                my_pilot = pilot
        if my_pilot.get_license() == planeTypeID:
            return True
        else:
            return False
