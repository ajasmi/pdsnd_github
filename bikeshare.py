'''References used for the completion of this project
w3schools.com >> for loops
https://www.tutorialspoint.com/python/python_dictionary.htm>> for using get
https://www.tutorialspoint.com/python/dictionary_get.htm
udacity nanodegree practice problems
https://stackoverflow.com/questions/50882377/how-do-you-convert-a-numpy-float64-to-python-native-string-type-for-writing-to-a>> convert to string
https://www.studytonight.com/python-howtos/how-to-get-month-name-from-month-number-in-python>> converting month number to name
https://pandas.pydata.org/
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.head.html#pandas.Series.head
https://pythonbasics.org/try-except/
https://github.com/Aritra96/bikeshare-project/blob/master/bikeshare.py'''


import time
import pandas as pd
import numpy as np
import datetime as dt


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        city= input("Please enter a city you want to explore:\n").lower()

        if city not in CITY_DATA.keys():
            print("Please enter chicago, new york city or washington")


    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ["all", "january", "february","march", "april", "may", "june"]
    month = ''
    while month not in month_list:
        month= input("Please enter the month you want to explore.\n You can enter all, january, february, march, april, may, june\n").lower()

        if month not in month_list:
            print("The month you entered does not match.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ["all", "sunday", "monday","tuesday", "wednesday", "thursday", "friday", "saturday"]
    day = ''
    while day not in day_list:
        day= input("Please enter the day you want to explore.\n You can enter all, sunday, monday, tuesday, wednesday, thursday, friday, saturday\n").lower()

        if day not in day_list:
            print("The day you entered does not match.")

    print("You want to view tha data for {} for month {} for day {}".format(city.upper(),month.upper(),day.upper()))
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    for key in city:
        filename = CITY_DATA.get(city)
    #print (filename)
    df = pd.read_csv(filename)

    # load data file into a dataframe
    #df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    month_num = df['Month'].mode()[0]

    #Converting month number to name
    dt_object = dt.datetime.strptime(str(month_num), "%m")
    popular_month = dt_object.strftime("%b")
    print('Most Popular Month:', popular_month)

    # TO DO: display the most common day of week

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Day'] = df['Start Time'].dt.weekday_name
    popular_day = df['Day'].mode()[0]
    print('Most Popular Day:', popular_day)


    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print('Most commonly used Start Station:', common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['Start Station'].mode()[0]

    print('Most commonly used end Station:', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['combo_station'] = df['Start Station'] + ' to ' +df ['End Station']
    frequent_combo_station = df['combo_station'].mode()[0]

    print('Most frequent combination of the trip:', frequent_combo_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time =sum(df['Trip Duration'])
    print ("The total travel time is {}.".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print ("The mean travel time is {}.".format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    '''Use of try, except, finally to handle exception for the data of washington as it does not have gender and birth data'''
    try:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

    # TO DO: Display counts of user types
        user_types = df['User Type'].value_counts()
        print("The count of user types:\n{}".format(user_types))

    # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count based on gender is:\n{}".format(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
        early_birth_year = df['Birth Year'].min()
        print("The earliest year of birth is:\n{}".format(int(early_birth_year)))

        recent_birth_year = df['Birth Year'].max()
        print("The most recent year of birth is:\n{}".format(int(recent_birth_year)))

        common_birth_year = df['Birth Year'].mode()[0]
        print("The most common year of birth is:\n{}".format(int(common_birth_year)))

    except:
        print("\nThere is no data to calulate the statistics")

    finally:
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def raw_data(df):
    '''Displays the raw data 5 rows at a time'''

    data_count = 0
    valid_input = ['yes','no']
    data = input ("\nDo you want to view the raw data (5 rows at a time)?\n Please type yes or no\n").lower()
    while data in valid_input:
        if data == "yes":
            print(df[data_count:data_count+5])
            data_count += 5
            data = input("Do you want to view more of the raw data?\n Please type yes or no\n").lower()

        elif data == "no":
            break

    if data not in valid_input:
        print("Sorry your answer is not recognised. Restart the program and make sure you answer with the word Yes or the word No.")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
