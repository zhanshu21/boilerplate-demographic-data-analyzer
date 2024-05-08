import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    mask = df['sex'] == 'Male'
    average_age_men = round(df[mask]['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    mask = df['education'] == 'Bachelors'
    num_bachelors = df[mask].shape[0]
    num_sum = df.shape[0]
    percentage_bachelors = round(num_bachelors/num_sum*100, 1)
    

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # percentage with salary >50K
    mask = ((df['education'] == 'Bachelors') | (df['education'] == 'Masters')| (df['education'] == 'Doctorate')) 
    df_higher = df[mask]
    higher_education_rich = df_higher[df_higher['salary'] == '>50K'].shape[0] / df_higher.shape[0] * 100
    higher_education_rich = round(higher_education_rich, 1)

    df_lower = df.drop(df_higher.index)
    lower_education_rich = df_lower[df_lower['salary'] == '>50K'].shape[0] / df_lower.shape[0] * 100
    lower_education_rich = round(lower_education_rich, 1)


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    
    # min_work_hours_rich = df_l50k['hours-per-week'].min()
    mask = df['hours-per-week']==min_work_hours
    df_minwork = df[mask]
    num_min_workers = df_minwork.shape[0]
    
    rich_percentage = df_minwork[df_minwork['salary'] == '>50K'].shape[0]/num_min_workers*100
    rich_percentage = round(rich_percentage, 1)

    # What country has the highest percentage of people that earn >50K?
    df_l50k = df[df['salary'] == '>50K']
    highest_earning_country = df_l50k['native-country'].value_counts().idxmax()
    highest_earning_country_percentage = df_l50k['native-country'].value_counts().max()/num_sum*100

    # Identify the most popular occupation for those who earn >50K in India.
    mask = (df['salary'] == '>50K') & (df['native-country'] == 'India')

    top_IN_occupation = df[mask]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
