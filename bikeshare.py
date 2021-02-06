#https://stackoverflow.com/questions/38067704/how-to-change-the-datetime-format-in-pandas
#https://stackoverflow.com/questions/32041840/python-error-typeerror-input-expected-at-most-1-arguments-got-3
#errortype
#https://pandas.pydata.org/pandas-docs/version/0.21.1/generated/pandas.DataFrame.mode.html
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['all','january', 'february', 'march', 'april', 'may', 'june']
DAY_DATA = ['all','sunday','monday','tuesday','wednesday','friday','saturday']

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
    while True:
        city = input("enter city name:\n").lower()
        if city in CITY_DATA:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter the month:\n"%MONTH_DATA).lower()
        if month in MONTH_DATA:
            break
            print("wrong")
            
       

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("Enter the day:"%DAY_DATA).lower()
        if day in DAY_DATA:
            break          

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
    df = pd.read_csv(CITY_DATA[city])
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
    print("the most common month")
    print(list(df['month'].mode()))


    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_dweek = df['day_of_week'].mode()[0]
    print(" most common day of week\n"+common_dweek)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("most common start hour: \n"+str(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\n most commonly used start station: \n')
    print(df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('\n most commonly used end station: \n')
    print(df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    print("most frequent combination of start station and end station trip")
    print((df['Start Station']+df['End Station']).mode()[0])
    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time")
    print(sum(df['Trip Duration']))

    # TO DO: display mean travel time
    print("average travel time")
    print(df['Trip Duration'].mean())

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if city == 'new york city' or city == 'chicago':
        print(df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
        print("\n the earliest year of birth")
        print(max(df['Birth Year']))
        print("\n the most recentt year of birth")
        print(min(df['Birth Year']))
        print("\n the most common year of birth")
        print(df['Birth Year'].mode())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        while True:
            display_data(df)
            break
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        display_data(df)
        break
       


if __name__ == "__main__":
	main()
