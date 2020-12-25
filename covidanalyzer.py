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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('country_name', help='Enter Country Name In Capwords',
                        choices=['North America', 'Europe', 'Asia',
                                 'South America', 'Oceania', 'Africa',
                                 'World', 'USA', 'Spain',
                                 'Italy', 'France', 'UK',
                                 'Germany', 'Turkey', 'Russia',
                                 'Iran', 'Brazil', 'Canada',
                                 'Belgium', 'Netherlands', 'India',
                                 'Peru', 'Switzerland', 'Portugal',
                                 'Ecuador', 'Saudi Arabia', 'Ireland',
                                 'Sweden', 'Mexico', 'Israel',
                                 'Austria', 'Singapore', 'Pakistan',
                                 'Chile', 'Japan', 'Poland',
                                 'Belarus', 'Qatar', 'Romania',
                                 'UAE', 'S. Korea', 'Indonesia',
                                 'Ukraine', 'Denmark', 'Serbia',
                                 'Philippines', 'Norway', 'Czechia',
                                 'Australia', 'Bangladesh', 'Dominican Republic',
                                 'Panama', 'Colombia', 'Malaysia',
                                 'Egypt', 'South Africa', 'Finland',
                                 'Morocco', 'Argentina', 'Luxembourg',
                                 'Algeria', 'Moldova', 'Kuwait',
                                 'Kazakhstan', 'Thailand', 'Bahrain',
                                 'Hungary', 'Greece', 'Oman',
                                 'Croatia', 'Uzbekistan', 'Iraq',
                                 'Armenia', 'Afghanistan', 'Cameroon',
                                 'Iceland', 'Azerbaijan', 'Ghana',
                                 'Estonia', 'Bosnia and Herzegovina', 'Nigeria',
                                 'New Zealand', 'Cuba', 'North Macedonia',
                                 'Slovenia', 'Bulgaria', 'Slovakia',
                                 'Lithuania', 'Guinea', 'Ivory Coast',
                                 'Djibouti', 'Bolivia', 'Hong Kong',
                                 'Tunisia', 'Cyprus', 'Latvia',
                                 'Senegal', 'Albania', 'Andorra',
                                 'Honduras', 'Kyrgyzstan', 'Lebanon',
                                 'Diamond Princess', 'Niger', 'Costa Rica',
                                 'Burkina Faso', 'Uruguay', 'Sri Lanka',
                                 'Guatemala', 'San Marino', 'Channel Islands',
                                 'Somalia', 'Georgia', 'DRC',
                                 'Mayotte', 'Malta', 'Jordan',
                                 'Taiwan', 'Mali', 'RÃ©union',
                                 'Jamaica', 'El Salvador', 'Kenya',
                                 'Palestine', 'Mauritius', 'Venezuela',
                                 'Montenegro', 'Sudan', 'Equatorial Guinea',
                                 'Isle of Man', 'Tanzania', 'Vietnam',
                                 'Maldives', 'Paraguay', 'Gabon',
                                 'Rwanda', 'Congo', 'Faeroe Islands',
                                 'Martinique', 'Myanmar', 'Guadeloupe',
                                 'Liberia', 'Gibraltar', 'Brunei',
                                 'Madagascar', 'Ethiopia', 'French Guiana',
                                 'Cambodia', 'Trinidad and Tobago', 'Cabo Verde',
                                 'Bermuda', 'Sierra Leone', 'Aruba',
                                 'Togo', 'Monaco', 'Zambia',
                                 'Liechtenstein', 'Bahamas', 'Barbados',
                                 'Uganda', 'Haiti', 'Mozambique',
                                 'Sint Maarten', 'Guyana', 'Guinea-Bissau',
                                 'Eswatini', 'Cayman Islands', 'Benin',
                                 'Libya', 'French Polynesia', 'Nepal',
                                 'Chad', 'CAR', 'Macao',
                                 'Syria', 'Eritrea', 'Saint Martin',
                                 'Mongolia', 'Malawi', 'South Sudan',
                                 'Zimbabwe', 'Angola', 'Antigua and Barbuda',
                                 'Timor-Leste', 'Botswana', 'Grenada',
                                 'Laos', 'Belize', 'Fiji',
                                 'New Caledonia', 'CuraÃ§ao', 'Dominica',
                                 'Namibia', 'Saint Kitts and Nevis', 'Saint Lucia',
                                 'St. Vincent Grenadines', 'Nicaragua', 'Falkland Islands',
                                 'Turks and Caicos', 'Burundi', 'Montserrat',
                                 'Greenland', 'Seychelles', 'Gambia',
                                 'Suriname', 'Vatican City', 'MS Zaandam',
                                 'Papua New Guinea', 'Sao Tome and Principe', 'Mauritania',
                                 'Bhutan', 'British Virgin Islands', 'St. Barth',
                                 'Western Sahara', 'Caribbean Netherlands', 'Anguilla',
                                 'Saint Pierre Miquelon', 'Yemen',
                                 'China',
                                 ])
    args = parser.parse_args()

    print(total_recovered_ratio(args.country_name))
