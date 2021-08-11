import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv


# function removes the Comma from string number#
def comma_removal(num_str):  # takes string @ '1,999.000'
    num_str = num_str.replace(',', '')
    return num_str  # '1999.000'


# function changes the point to comma and comma to point#
def point_to_comma_vice_versa(num_str):  # takes string @ '1,999.000'
    num_str = num_str.replace(',', 'COMMA')
    num_str = num_str.replace('.', ',')
    num_str = num_str.replace('COMMA', '.')
    return num_str  # '1.999,000'


def number_formatter(num_string):  # Removes Special Character and Alphabets from number
    new_numstring = ''.join(char for char in num_string if char.isnumeric())
    return new_numstring


class Crawler:
    def __init__(self, link):
        self.link = link
        self.soup = None
        self.progress = 00
        self.property_zip = None
        self.property_address = None
        self.info_mainclass = None
        self.price = None
        self.area = None
        self.rooms = None
        self.agent_address = None
        self.agent_phone = None
        self.agent_mobile = None

    # makes soup of Link Provided#
    def make_soup(self):

        html_content = requests.get(self.link).content
        # print(html_content)
        self.soup = BeautifulSoup(html_content, 'html.parser')

    # finding property address#
    def find_property_address(self):
        try:
            location = self.soup.find(
                class_='btn_02 black no_m no_l w_auto_s margin_none_s ng-star-inserted').get_text()

            i = 0
            self.property_address = ''
            while i < len(location.split()):
                if i == 0:
                    self.property_zip = location.split()[i]
                else:
                    self.property_address += location.split()[i]
                i += 1
            self.progress += 10
        except:
            self.property_zip = 'Not Available'
            self.property_address = 'Not Available'
            self.progress += 00

    # Function gets the main class for Rooms, Price#
    def find_mainclass_for_price_area_rooms(self):
        try:
            self.info_mainclass = self.soup.find(class_='hardfacts clear')
        except:
            self.info_mainclass = ' Could Not Find Price, Rooms & Living Area.'

    # finding property price#
    def find_property_price(self):
        try:
            self.price = self.info_mainclass.find('strong', class_='ng-star-inserted').text  # price = 1111 €
            self.price = float(comma_removal(point_to_comma_vice_versa(self.price.split()[
                                                                           0])))  # typecasting str to float(removing the comma from string(reversing the comma into point and vice versa(( first index str datatype))))
            self.progress += 10
        except:
            self.progress = 00
            self.price = -1

    # finding living space#
    def find_living_area(self):
        try:
            self.area = self.info_mainclass.find('span', class_='ng-star-inserted').text  # price = 2222 m²
            self.area = float(comma_removal(point_to_comma_vice_versa(self.area.split()[
                                                                          0])))  # typecasting str to float(removing the comma from string(reversing the comma into point and vice versa(( first index str datatype))))
            self.progress += 10
        except:
            self.progress += 00
            self.area = -1

    # finding number of rooms#
    def find_rooms(self):
        try:
            self.rooms = self.info_mainclass.find(class_='hardfact rooms ng-star-inserted').text
            self.rooms = self.rooms.split()[0]
            self.progress += 10
        except:
            self.progress += 00
            self.rooms = 'Not Available'

    # finding agent address#
    def find_agent_address(self):
        try:
            self.agent_address = self.soup.find(
                class_='grid_06o12_l grid_06o12_m grid_12o12_s order_2_s padding_bottom_none')
            self.agent_address = self.agent_address.find('p', class_='ng-star-inserted').text
            self.progress += 10
        except:
            self.progress += 00
            self.agent_address = 'Private Agent'

    def find_agent_phone(self):
        try:
            script = (self.soup.find_all('script')[14])
            script = str(script)
            try:
                pos_phone = script.index('phone') + 10
                phone = script.strip()[pos_phone:pos_phone + 32]
                pos_mobile = script.index('mobile') + 10
                mobile = script.strip()[pos_mobile:pos_mobile + 32]
                self.agent_phone = number_formatter(phone)
                self.agent_mobile = number_formatter(mobile)
                self.progress += 20
            except:
                try:
                    pos_phone = script.index('phone') + 10
                    phone = script.strip()[pos_phone:pos_phone + 32]
                    self.agent_phone = number_formatter(phone)
                    self.agent_mobile = 'Phone'
                    self.progress += 10
                except:
                    try:
                        pos_mobile = script.index('mobile') + 10
                        mobile = script.strip()[pos_mobile:pos_mobile + 32]
                        self.agent_mobile = number_formatter(mobile)
                        self.agent_phone = 'Mobile'
                        self.progress += 10
                    except:
                        self.agent_mobile = 'Not Available'
                        self.agent_phone = 'Not Available'
        except:
            self.progress += 00
            print('Unable to Find Number')  # if script [14] is not found


# opening notepad file which contains URLs
file = open('D:\\urls.txt', 'r')

file1 = open('sixless.csv', 'a', newline='')
file2 = open('sixplus.csv', 'a', newline='')
file3 = open('defective links.csv', 'a', newline='')
writerless = csv.writer(file1)
writerplus = csv.writer(file2)
writerdefective = csv.writer(file3)
header_row = ['Date(D/M/Y)', 'Time(H:M:S)', 'Link', 'Progress (%)', 'Property Zip Code', 'Property Address', 'Property Price',
              'Property Area',
              'Price/Area', 'Rooms', 'Agent Address', 'Agent Phone', 'Agent Mobile']
header_defect_row = ['Date(D/M/Y)', 'Time(H:M:S)', 'Link', 'Progress', 'Comments/Issue']
writerless.writerow(header_row)
writerplus.writerow(header_defect_row)
writerdefective.writerow(header_row)

# iterating URLs through for Request
for link in file:
    now = datetime.now()
    Date = now.strftime("%d/%m/%Y")
    Time = now.strftime("%H:%M:%S")

    obj = Crawler(link)
    obj.make_soup()

    # --> Start Function Calling Here--#
    obj.find_property_address()
    if obj.progress == 00:  # check for identifing improper urls or property has been removed from link
        print('Something is wrong with Property/ Link.')
        list2 = [Date, Time, link, 'Progress 0%', 'Something is wrong with Property/ Link.Perform Manual Inspection']
        writerdefective.writerow(list2)
        print('-------')
        continue

    obj.find_mainclass_for_price_area_rooms()

    obj.find_property_price()
    obj.find_living_area()
    obj.find_rooms()
    obj.find_agent_address()
    obj.find_agent_phone()
    # --> Function Calling Ends Here--#

    list = [Date, Time, link, 'Progress ' + str(obj.progress) + '%', obj.property_zip, obj.property_address, obj.price,
            obj.area,
            float(obj.price / obj.area), obj.rooms,
            obj.agent_address, 'Phone : ' + obj.agent_phone, 'Mobile: ' + obj.agent_mobile]

    if int(obj.rooms) < 6:
        writerless.writerow(list)
    else:
        writerplus.writerow(list)
    print(list)
    print('-------')
# Hello I am Zinda
