import csv
import argparse
import sys

ratio = None


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


def average_death_rate(safety_measure):
    count = 0
    countries_list = []
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

    result = sum(countries_death_rate) / count
    result = "{:.4f}".format(result)
    return f'{result}% death average found in {count} countries.'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', help='Enter country Name', nargs='+')
    parser.add_argument('-b', help='Enter Safety Measure', nargs='+')
    parser.add_argument('c', action='store_true')

    args = parser.parse_args()

    if args.a:
        arg_str = ' '.join(args.a)
        print(total_recovered_ratio(arg_str.title()))

    elif args.b:
        arg_str = ' '.join(args.b)
        print(average_death_rate(arg_str.capitalize()))
