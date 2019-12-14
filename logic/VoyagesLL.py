from logic.LLAPI import LLAPI
#from iolayer.VoyagesIO import VoyagesIO
import datetime
import time
from logic.AirplanesLL import AirplanesLL
from iolayer.CrewIO import CrewIO


class VoyagesLL():
    def __init__(self, a_str=''):
        self.a_str = a_str
    
    def is_airplane_available(self, date, plane_insignia):
        all_voyages = VoyagesLL().get_voyages()
        for voyage in all_voyages:
            if voyage[1] == plane_insignia and voyage[2] == date:
                return False
        else:
            return True

    def create_voyage(self, new_voyage_list):
        new_voyage_str = ','.join(new_voyage_list)
        LLAPI().write_in_voyages_flights(new_voyage_str)

    def update_one_voyage(self, number_voyage_to_change, replacement_value, index_to_replace):
        one_voyage = LLAPI().load_voyages_from_file(number_voyage_to_change)
        employees_working_same_day, destinations_list = VoyagesLL(
        ).employees_working(one_voyage.get_date())
        for voyage in employees_working_same_day:
            for employee in voyage:
                if employee == replacement_value:
                    return 'False'
                else:
                    str_voyage = str(one_voyage)
                    list_voyage = str_voyage.split(',')
                    list_voyage[index_to_replace] = replacement_value
                    VoyagesLL().change_the_big_voyage_list(number_voyage_to_change, list_voyage)

    def change_the_big_voyage_list(self, number_voyage_to_change, new_list_voyage, input_value='0'):
        all_voyages = LLAPI().load_voyages_from_file(input_value)
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
        LLAPI().overwrite_voyage_file(all_voyages_list)

    def is_voyage_fully_staffed(self, voyageID):
        voyages = LLAPI().load_voyages_from_file(voyageID)
        for line in voyages:
            str_voyage = str(line)
            list_voyage = str_voyage.split(',')
            if list_voyage[4] == 'x' or list_voyage[5] == 'x' or list_voyage[6] == 'x' or list_voyage[7] == 'x':
                return print('Voyage is not fully staffed!')
            else:
                return print('Voyage is fully staffed!')

    def get_voyages(self):
        all_voyages = LLAPI().load_voyages_from_file('0')
        a_list = []
        for voyage in all_voyages:
            str_voyage = str(voyage)
            list_voyage = str_voyage.split(',')
            list_of_voyages = list_voyage
            a_list.append(list_of_voyages)
        return a_list

    def get_one_voyage(self, voyageID):
        one_voyage = LLAPI().load_voyages_from_file(voyageID)
        return one_voyage

    def list_voyages_by_day(date, the_input='0'):
        all_voyages = LLAPI().load_voyages_from_file('0')
        voyages_that_day = []
        staffed = []
        for line in all_voyages:
            str_voyage = str(line)
            list_voyage = str_voyage.split(',')
            if list_voyage[2] == the_input:
                str_voyage = str(line)
                list_voyage = str_voyage.split(',')
                voyages_that_day.append(list_voyage)
                if list_voyage[4] == 'x' or list_voyage[5] == 'x' or list_voyage[6] == 'x' or list_voyage[7] == 'x':
                    staffed.append('Voyage is not fully staffed!')
                else:
                    staffed.append('Voyage is fully staffed!')
        return voyages_that_day, staffed

    def list_voyages_by_week(self, weeknumber, the_input='0'):
        staffed = []
        WEEK = weeknumber - 2  # as it starts with 0 and you want week to start from sunday
        startdate = time.asctime(time.strptime('2019 %d 0' % WEEK, '%Y %W %w'))
        startdate = datetime.datetime.strptime(
            startdate, '%a %b %d %H:%M:%S %Y')
        dates = [startdate.strftime('%Y-%m-%d')]
        for i in range(1, 7):
            day = startdate + datetime.timedelta(days=i)
            dates.append(day.strftime('%Y-%m-%d'))
        all_voyages = LLAPI().load_voyages_from_file(the_input)
        all_voyages_in_that_week = []
        for line in all_voyages:
            str_voyage = str(line)
            list_voyage = str_voyage.split(',')
            if list_voyage[2] in dates:
                all_voyages_in_that_week.append(list_voyage)
                if list_voyage[4] == 'x' or list_voyage[5] == 'x' or list_voyage[6] == 'x' or list_voyage[7] == 'x':
                    staffed.append('Voyage is not fully staffed!')
                else:
                    staffed.append('Voyage is fully staffed!')
        return all_voyages_in_that_week, staffed

    def employees_working(self, date_inputt, voyageID='0'):
        all_voyages = LLAPI().load_voyages_from_file(voyageID)
        employees_working_list = []
        destinations_list = []
        for line in all_voyages:
            if line.date == date_inputt:
                employees_list = []
                if line.captain != 'x':
                    employees_list.append(line.captain)
                if line.copilot != 'x':
                    employees_list.append(line.copilot)
                if line.flightAttendant != 'x':
                    employees_list.append(line.flightAttendant)
                if line.FlightServiceManager != 'x':
                    employees_list.append(line.FlightServiceManager)
                employees_working_list.append(employees_list)
                destinations_list.append(line.destination)
        return employees_working_list, destinations_list
    
    
