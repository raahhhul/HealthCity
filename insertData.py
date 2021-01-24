#patientNo,Disease,Height,Weight,Symptoms,CheckupDate,Gender,Area,City,State,BloodGroup,Age
#   1, D1, 5.2, 70, S1, 12/dec, M, Amaraiwadi, Abad, Guj, B+, 20
#   2, D2, 5.2, 70, S2, 12/dec, F, Area2, Abad, Guj, AB+, 21
# personMobileDictionary = {'jay':'vivo', 'deep':'samsung','rititka':'oppo'}
#json file is file with key-value pair
#csv-comma seperated values
import numpy as np
import pandas as pd
import json
import random
from datetime import date
#numpy = numerical python
#pandas = dataframe
def getcityAreaList():
    files = [open('/city_areas/ahmedabad.txt'),
    open('/city_areas/amreli.txt'),
    open('/city_areas/anand.txt'),
    open('/city_areas/banaskantha.txt'),
    open('/city_areas/bharuch.txt'),
    open('/city_areas/dahod.txt'),
    open('/city_areas/gandhinagar.txt')]
    initDict = {}
    for file in files:
        array = file.read().split('\n') #[Amraiwadi S.O	Ahmedabad	380026,Anandnagar S.O (Ahmedabad)	Ahmedabad	380007,...]
        area = []
        for arr in array:
            a = arr.split('\t')# [Amraiwadi S.O Ahmedabad, 380026]
            area.append(a[0].split(' ')[0]) #[Amraiwadi, S.O, Ahmedabdd]
        # area = ['Area1','Area2','Area3'.....]
        initDict.update({file.name.split('\\')[-1].split('.')[0].capitalize(): area})
    return initDict

def getRandomDate(startDay,startMonth,startYear,endDay,endMonth,endYear):
    start_dt = date.today().replace(day=startDay, month=startMonth, year=startYear).toordinal()
    end_dt = date.today().replace(day=endDay, month=endMonth, year=endYear).toordinal()
    dt = date.fromordinal(random.randint(start_dt, end_dt))
    dt = date.__format__(dt, '%d-%m-%Y')
    return dt


cities_list = ['Ahmedabad', 'Vadodara', 'Anand',
               'Dahod', 'Kheda', 'Panchmahal', 'Gandhinagar',
               'Banaskantha', 'Mehsana', 'Patan',
                'Sabarkantha', 'Rajkot','Amreli', 'Bhavnagar',
                'Jamnagar', 'Junagadh','Porbandar',
                'Surendranagar','Kachchh','Surat','Bharuch',
                'Dang','Narmada','Navsari','Valsad']

#state
state = 'Gujarat'

#height list
height_list=[5,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,6]

#weight list
weight_list=np.arange(41,82)

#blood groups list
blood_groups= ['A+','B+','AB+','O+','A-','B-','AB-','O-']


openfile = open('sex_age_diagnosis.json')
jsondata = json.load(openfile)
sexAgeDiag = pd.DataFrame(jsondata)
print(sexAgeDiag)

areas = np.array([])
patientNos = np.array([])
diseases = np.array([])
heights = np.array([])
weights = np.array([])
symptoms = np.array([])
checkupDates = np.array([])
genders = np.array([])
cities = np.array([])
blood_groups = np.array([])
ages_list = np.array([])

