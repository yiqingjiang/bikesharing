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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid = True
    while valid:
        city = input('Please input the city you want to explore (chicago, new york city, washington): ').lower()
        if city not in ('chicago','new york city', 'washington' ):
            print("Sorry, the input is invalid. Enter again:")
        else: 
            valid = False 
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please input the month you want to explore (all or specific month in lower case): ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please input the weekday you want to explore (all or specific day in lower case): ').lower()

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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df, print_dict):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print_dict['Most Common Month'] = popular_month
    print_dict['Most Common Day'] = popular_day
    print_dict['Most Common Hour'] = popular_hour                 
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return print_dict

def station_stats(df, print_dict):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    popular_com_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
    
    print_dict['Most Commonly used Start Station'] = popular_start_station
    print_dict['Most Commonly used End Station'] = popular_end_station
    print_dict['Most frequent combination of start station and end station trip'] = popular_com_station

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    return print_dict

def trip_duration_stats(df, print_dict):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    print_dict["Total travel time in seconds"] = total_time          
    print_dict["Mean travel time in seconds"] = mean_time
    return print_dict               
                    
def user_stats(df, print_dict):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_types = df['User Type'].value_counts()
    
    # TO DO: Display counts of gender
    count_genders = df['Gender'].value_counts()
    

    # TO DO: Display earliest, most recent, and most common year of birth
    popular_birthyear = df['Birth Year'].mode()
    most_recent = df['Birth Year'].max()
    earliest = df['Birth Year'].min()
    print_dict["Counts of user types"] = count_user_types
    print_dict["Counts of genders"] = count_genders
    print_dict["The earliest birth"] = int(earliest)
    print_dict["The most recent birth"] = int(most_recent)
    print_dict["The most common year of birth"] = int(popular_birthyear)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    return print_dict

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)             
        print_dict = {}        
        
        time_stats(df, print_dict)
        station_stats(df, print_dict)
        trip_duration_stats(df, print_dict)
        user_stats(df, print_dict)
        
        for k, (key, value) in enumerate(print_dict.items()):
            if k > 0 and k % 5 == 0:
                more_data = input('\nWould you like to continue? Enter yes or no.\n')
                if more_data.lower() != 'yes':
                    break
            print ("{}: {}".format(key, value))


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
