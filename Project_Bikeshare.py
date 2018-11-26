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
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    cities = ['chicago','new york city','washington']
    while True:
        city = input('Please Enter name of city\n')
        city = city.lower()
        if city in cities:
            break;
    # Get user input for month (all, january, february, ... , june)
    months=['all','january','february','march','april','may','june','july','august','september','october','november','december']
    while True:
        month = input('Please Enter month of the year\n')
        month = month.lower()
        if month in months:
            break;
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        day = input('Please Enter day of the week\n')
        day = day.lower()
        if day in days:
            break;

    print('-'*40)
    print('City, Month,Day',city, month,day)
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

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour

   # Display the most common month
    common_month = df['month'].mode()[0]
    print('\nMost Popular Start Month:', common_month)


  # Display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('\nMost Popular Start Day:', common_day)

    # Display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('\nMost Popular Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    Popular_start_station = df['Start Station'].mode()[0]
    print('\nMost Popular Start Station:', Popular_start_station)

    # Display most commonly used end station
    Popular_end_station = df['End Station'].mode()[0]
    print('\nMost Popular End Station:', Popular_end_station)


    # Display most frequent combination of start station and end station trip
    df['round_trip'] = 'From' + df['Start Station'] +'To'+ df['End Station']
    common_round_trip_station = df['round_trip'].mode()[0]
    print('\nMost Popular Round trip Station:', common_round_trip_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_trip_time = df['Trip Duration'].sum()
    print('\nThe total travel time in seconds:', total_trip_time)

    # Display mean travel time
    mean_trip_time = df['Trip Duration'].mean()
    print('\nThe mean of travel time in seconds:', mean_trip_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print('\n The count of User Type is :',user_type)

    # Display counts of
    try :
        if city in ['chicago','new york city']:
           gender = df['Gender'].value_counts()
           print('\nCounts of Gender',gender)
    except:
          print('\n Gender is not present in Washington ')


    # Display earliest, most recent, and most common year of birth
    try :
           if city in ['chicago','new york city']:
               birth_year = df['Birth Year'].min()
               print('\nThe earliest birth year is',(int)(birth_year))
    except:
              print('\n Birth year is not present in Washington ')
    try :
           if city in ['chicago','new york city']:
               birth_year = df['Birth Year'].max()
               print('\nThe most recent birth year is',(int)(birth_year))
    except:
           print('\n Birth year is not present in Washington ')
    try :
           if city in ['chicago','new york city']:
               birth_year = df['Birth Year'].mode()
               print('\nThe most common birth year is',(int)(birth_year))
    except:
          print('\n Birth year is not present in Washington ')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_input_data(df):
    user_input = input('Would you like to see a Raw Data? \'yes\'.\n')
    while True:
        if user_input != 'yes':
            break
        else:
            return(print(df.sample(5)))
           # return( df.sample(5)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_input_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
