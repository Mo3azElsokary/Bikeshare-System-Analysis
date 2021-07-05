import time
import pandas as pd
import numpy as np

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
    print('please put all letters in lowercase.')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cityinput = input('Would you like to see data for chicago, new york city, or washington?\n').lower().strip()
    while cityinput not in ['chicago','new york city','washington'] :
        print ('please put a valid value')
        cityinput = input().lower().strip()
    if cityinput in ['chicago','new york city','washington'] :
        city = cityinput
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    mdinput = input('Would you like to filter the data by month, day, both, or non to analyse all months and days?\n').lower().strip()
    while mdinput not in ['both','month','day','non'] :
        print ('please put a valid value')
        mdinput = input().lower().strip()
    if mdinput == 'both':
        monthinput = input('Which month - january, february, march, april, may, or june?\n').lower().strip()
        while monthinput not in ['january','february','march','april','may','june'] :
            print ('please put a valid value')
            monthinput = input().lower().strip()
        if monthinput in ['january','february','march','april','may','june'] :
            month = monthinput
        dayinput = input('Which day - monday, tuesday, wednesday, thursday, friday, saturday, or sunday?\n').lower().strip()
        while dayinput not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] :
            print ('please put a valid value')
            dayinput = input().lower().strip()
        if dayinput in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] :
            day = dayinput
        print('-'*40)
        print('Just one moment ..... loading the data')
        return city, month, day
    elif mdinput == 'month':
        monthinput = input('Which month - january, february, march, april, may, or june?\n').lower().strip()
        while monthinput not in ['january','february','march','april','may','june'] :
            print ('please put a valid value')
            monthinput = input().lower().strip()
        if monthinput in ['january','february','march','april','may','june'] :
            month = monthinput
            day = 'all'
        print('-'*40)
        print('Just one moment ..... loading the data')
        return city, month, day
    elif mdinput == 'day':
        dayinput = input('Which day - monday, tuesday, wednesday, thursday, friday, saturday, or sunday?\n').lower().strip()
        while dayinput not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] :
            print ('please put a valid value')
            dayinput = input().lower().strip()
        if dayinput in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'] :
            day = dayinput
            month = 'all'
        print('-'*40)
        print('Just one moment ..... loading the data')
        return city, month, day
    else : 
        month , day = 'all' , 'all'
        print('-'*40)
        print('Just one moment ..... loading the data')
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
        # load data file into a dataframe
    DataFrame = pd.read_csv(CITY_DATA[city])
    df = DataFrame.copy()
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month.title()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df , DataFrame

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print ('the most common month :-')
    common_month = df['month'].mode()[0]
    print(common_month , '  with count of :-  ' , str(df[df['month'] == common_month].count()[0]))
    # TO DO: display the most common day of week
    print ('the most common day of the week :-')
    common_day = df['day_of_week'].mode()[0]
    print(common_day , '  with count of :-  ' , str(df[df['day_of_week'] == common_day].count()[0]))
    # TO DO: display the most common start hour
    print ('the most common start hour is :-')
    most_common_start_hour = df['Start Time'].dt.hour.mode()[0]
    print(most_common_start_hour , '  with count of :-  ' , str(df[df['Start Time'].dt.hour == most_common_start_hour].count()[0]))
    # TO DO: display the most common end hour
    print ('the most common end hour is :-')
    most_common_end_hour = df['End Time'].dt.hour.mode()[0]
    print(most_common_end_hour , '  with count of :-  ' , str(df[df['End Time'].dt.hour == most_common_end_hour].count()[0])) 
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print ('the most common start station :-')
    most_common_start_station = df['Start Station'].mode()[0]
    print(most_common_start_station , '  with count of :-  ' , str(df[df['Start Station'] == most_common_start_station].count()[0])) 
    # TO DO: display most commonly used end station
    print ('the most common end station :-')
    most_common_end_station = df['End Station'].mode()[0]
    print(most_common_end_station , '  with count of :-  ' , str(df[df['End Station'] == most_common_end_station].count()[0])) 
    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + '  >>>>  ' + df['End Station']
    print ('the most common trip :-')
    most_common_trip = df['Trip'].mode()[0]
    print(most_common_trip , '  with count of :-  ' , str(df[df['Trip'] == most_common_trip].count()[0])) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['travel_time'] = df['End Time'] - df['Start Time']
    print ('The total traveling time :-')
    print (df['travel_time'].sum())

    # TO DO: display mean travel time
    print ('The average time spent on each trip :-')
    print (df['travel_time'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print ('Display counts of user types :-')
    df['User Type'].value_counts()

    # TO DO: Display counts of gender
    print ('Display counts of gender :-')
    if 'Gender' not in df :
        print ('No gender data to share.')
    else :
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print ('The oldest, youngest, and most common year of birth, respectively :-')
    if 'Birth Year' not in df :
        print ('No birth year data to share.')
    else :
        birth = (df['Birth Year'].min() , df['Birth Year'].max() , df['Birth Year'].mode()[0])
        print (birth)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(DataFrame):
    while True :
        display_data = input('Would you like to view individual trip data? type yes or no \n').lower().strip()
        while display_data not in ['yes','no'] :
            print ('please put a valid value')
            display_data = input().lower().strip()
        if display_data in ['yes','no'] :
            if display_data == 'yes' :
                n=0
                while n <= 5 :
                    d = DataFrame.iloc[np.random.choice(299999)].to_dict()
                    for k, v in d.items():
                        print (k, ' : ', v)
                    print ('___________________')
                    n += 1
            if  display_data == 'no' :
                print ('Thank you')
                break

def main():
    while True:

        city, month, day = get_filters()
        df , DataFrame = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(DataFrame)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower().strip() != 'yes':
            break


if __name__ == "__main__":
    main()