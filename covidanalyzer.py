import csv
import argparse
import sys
from tkinter import *
ratio = None
countries_list = []


def total_recovered_ratio(country):
    global ratio

    with open('covid_cases_stats.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            if line[0] == country:

                total_cases = int(line[1])
                total_recovered = int(line[5])

                try:
                    ratio = total_recovered / total_cases

                except ZeroDivisionError:
                    print("Can't divide by zero!")
                    sys.exit(1)

                return f'Recovered/total ratio: {ratio}'

    return 'You have entered the wrong country name!'


def average_death_rate(safety_measure, check):
    global countries_list
    count = 0
    total_cases = None
    total_deaths = None
    countries_death_rate = []
    result = None

    with open('covid_safety_measures.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            if line[7] == safety_measure:
                with open('covid_cases_stats.csv', 'r', encoding='utf-8') as csv_new_file:
                    csv_new_reader = csv.reader(csv_new_file)

                    for new_line in csv_new_reader:
                        if new_line[0] == line[1]:
                            if new_line[0] not in countries_list:
                                countries_list.append(new_line[0])
                                total_deaths = int(new_line[3].strip() or 0)
                                total_cases = int(new_line[1])
                                countries_death_rate.append((total_deaths / total_cases) * 100)
                                count += 1
    if check == 1:
        return countries_list
    else:
        result = sum(countries_death_rate) / count
        result = '{:.4f}'.format(result)
        countries_list.clear()
        return f'{result}% death average found in {count} countries.'


def calculate_efficiency(safety_items):
    global countries_list
    total_recovered = 0
    total_cases = 0
    efficiency = 0
    countries_name = []
    safety_measures_efficiencies = []

    for i in range(5):
        countries_name = average_death_rate(safety_items[i], 1)
        with open('covid_cases_stats.csv', 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                if line[0] in countries_name:
                    total_cases += int(line[1])
                    total_recovered += int(line[5].strip() or 0)

        efficiency = total_recovered / total_cases
        efficiency = '{:.4f}'.format(efficiency)
        safety_measures_efficiencies.append(efficiency)
    root = Tk()
    x = Label(root, text='Efficiencies of 5 mostly adopted Safety Measures. ')
    x.pack()
    for i in range(5):
        x = Label(root, text=f'{safety_items[i]}: {safety_measures_efficiencies[i]}')
        x.pack()
    root.mainloop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help='Enter country Name', nargs='+')
    parser.add_argument('-b', help='Enter Safety Measure', nargs='+')
    parser.add_argument('-c', action='store_true')

    args = parser.parse_args()
    list_items = ['Economic measures', 'Limit public gatherings',
                  'Introduction of quarantine policies', 'Strengthening the public health system',
                  'International flights suspension'
                  ]
    if args.a:
        arg_str = ' '.join(args.a)
        print(total_recovered_ratio(arg_str.title()))

    elif args.b:
        arg_str = ' '.join(args.b)
        print(average_death_rate(arg_str.capitalize(), 0))

    elif args.c:
        calculate_efficiency(list_items)
    else:
        print('You have enter wrong command, Kindly Choose command from -a, -b, -c')
