"""
author: adel.beghdadi@edu.esiee.fr
"""
# vos imports ici
import csv

FILENAME = "ex08-zip-data-meteo-france-synop.2015110112.csv"

def read_data_to_dicts(filename):
    """puts structured csv data in a list of dicts

    Args:
        filename (str): csv data filename

    Returns:
        list: csv data in dicts

    >>> data = read_data_to_dicts(FILENAME)
    >>> isinstance(data, list)
    True
    >>> isinstance(data[0], dict)
    True
    >>> len(data)
    51
    >>> data[11]['numer_sta']
    '07168'
    >>> data[11]['date']
    '20151101120000'
    >>> data[11]['pmer']
    '102940'
    >>> data[11]['t']
    '290.050000'
    >>> data[11]['td']
    '283.850000'
    >>> data[11]['tminsol']
    '275.850000'
    >>> data[21]['numer_sta']
    '07335'
    >>> data[21]['date']
    '20151101120000'
    >>> data[21]['pmer']
    '102720'
    >>> data[21]['t']
    '293.450000'
    >>> data[21]['td']
    '279.050000'
    >>> data[21]['tminsol']
    '273.950000'
    >>> data[31]['numer_sta']
    '07607'
    >>> data[31]['date']
    '20151101120000'
    >>> data[31]['pmer']
    '102400'
    >>> data[31]['t']
    '292.950000'
    >>> data[31]['td']
    '284.950000'
    >>> data[31]['tminsol']
    'mq'
    >>> data[41]['numer_sta']
    '07790'
    >>> data[41]['date']
    '20151101120000'
    >>> data[41]['pmer']
    '102830'
    >>> data[41]['t']
    '291.850000'
    >>> data[41]['td']
    '282.850000'
    >>> data[41]['tminsol']
    '284.750000'
    """
    l = []
    header = []
    with open(filename,'r',encoding='utf-8') as f:
        reader = csv.reader(f,delimiter=";")
        header = next(reader)
    with open(filename,'r',newline='\n',encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile,fieldnames=header,delimiter=";")
        for i,row in enumerate(reader):
            if i != 0:
                l.append(row)
    return l

def filter_data(d):
    """Filter full data dict

    Args:
        d (dict): full meteo data

    Returns:
        dict: filtered meteo data (numer_sta, date, t)

    >>> d = {'numer_sta': '07005', 'date': '20151101120000', \
    'pmer': '102910', 'tend': '-80', 'cod_tend': '8', \
        'dd': '150', 'ff': '2.600000', 't': '287.750000', \
        'td': '283.950000', 'u': '78', 'vv': '8000', \
        'ww': '0', 'w1': '0', 'w2': '0', 'n': '0', 'nbas': '0', \
        'hbas': 'mq', 'cl': '30', 'cm': '20', \
        'ch': '10', 'pres': '102040', 'niv_bar': 'mq', 'geop': 'mq',\
         'tend24': '590', 'tn12': 'mq', \
        'tn24': 'mq', 'tx12': 'mq', 'tx24': 'mq', 'tminsol': '278.950000',\
         'sw': 'mq', 'tw': 'mq', \
        'raf10': '3.500000', 'rafper': '4.600000', 'per': '-10', \
        'etat_sol': '0', 'ht_neige': '0.000000', \
        'ssfrai': '0.000000', 'perssfrai': 'mq', 'rr1': '0.000000',\
         'rr3': '0.000000', 'rr6': '0.200000', \
        'rr12': '0.400000', 'rr24': '0.400000', 'phenspe1': 'mq', \
        'phenspe2': 'mq', 'phenspe3': 'mq', \
        'phenspe4': 'mq', 'nnuage1': 'mq', 'ctype1': 'mq', 'hnuage1': 'mq', \
        'nnuage2': 'mq', 'ctype2': 'mq', \
        'hnuage2': 'mq', 'nnuage3': 'mq', 'ctype3': 'mq', 'hnuage3': 'mq', \
        'nnuage4': 'mq', 'ctype4': 'mq', 'hnuage4': 'mq', '': ''}

    >>> fd = filter_data(d)
    >>> isinstance(fd, dict)
    True
    >>> len(fd)
    3
    >>> fd['numer_sta']
    '07005'
    >>> fd['date']
    '20151101120000'
    >>> fd['t']
    '287.750000'
    >>> fd.get('ww')
    
    """
    fields = ['numer_sta','date','t']
    fd = {key:value for key, value in d.items() if key in fields}
    return fd

def main():
    """
    Fonction principale

    Args: Aucun

    Returns: Rien
    """
    data = read_data_to_dicts(FILENAME)
    print(data)
    print(data[41])
    print(data[41]['td'])
    print(filter_data(data[9]))

if __name__ == "__main__":
    main()
