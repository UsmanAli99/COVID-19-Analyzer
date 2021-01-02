import csv
import argparse
import sys

ratio = None


def total_recovered_ratio(country):
    global ratio

    with open('covid_cases_stats.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            if line[0] == country.title():

                total_cases = int(line[1])
                total_recovered = int(line[5])

                try:
                    ratio = total_recovered / total_cases

                except ZeroDivisionError:
                    print("Can't divide by zero!")
                    sys.exit(1)

                return f'Recovered/total ratio: {ratio}'

    return 'You have entered the wrong country name!'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('task', help='Enter a, b or c to run task 1, 2 or 3 respectively!')
    parser.add_argument('second_argument', help='Enter Country Name or Safety Measure', nargs='+')

    args = parser.parse_args()
    arg_str = ' '.join(args.second_argument)

    if args.task == 'a':
        if args.second_argument:
            print(total_recovered_ratio(arg_str))
    elif args.task == 'b':
        print()
    elif args.task == 'c':
        print()
    else:
        print('You have to Enter a, b or c as your first argument to run task 1, 2 or 3 respectively!')