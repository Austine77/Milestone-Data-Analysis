# Set the correct file path to your CSV file
file_path = "/storage/emulated/0/Download/life-expectancy.csv"  # Common path for Downloads on Android

min_life_expectancy = float('inf')
max_life_expectancy = float('-inf')
min_year_country = ("", "")
max_year_country = ("", "")
total_life_expectancy = {}
count_life_expectancy = {}

try:
    with open(file_path, 'r') as file:
        next(file)  # Skip the header line
        for line in file:
            parts = line.strip().split(",")
            country = parts[0]
            year = int(parts[1])
            life_expectancy = float(parts[2])  # Assuming life expectancy is in the third column

            if life_expectancy < min_life_expectancy:
                min_life_expectancy = life_expectancy
                min_year_country = (year, country)

            if life_expectancy > max_life_expectancy:
                max_life_expectancy = life_expectancy
                max_year_country = (year, country)

            if year not in total_life_expectancy:
                total_life_expectancy[year] = 0
                count_life_expectancy[year] = 0
            total_life_expectancy[year] += life_expectancy
            count_life_expectancy[year] += 1

    print(f"The lowest life expectancy is: {min_life_expectancy} from {min_year_country[1]} in {min_year_country[0]}")
    print(f"The highest life expectancy is: {max_life_expectancy} from {max_year_country[1]} in {max_year_country[0]}")

    year_of_interest = int(input("Enter the year of interest: "))
    if year_of_interest in total_life_expectancy:
        average_life_expectancy = total_life_expectancy[year_of_interest] / count_life_expectancy[year_of_interest]

        year_min = float('inf')
        year_max = float('-inf')
        min_country = ""
        max_country = ""

        with open(file_path, 'r') as file:
            next(file)  # Skip the header line
            for line in file:
                parts = line.strip().split(",")
                country = parts[0]
                year = int(parts[1])
                life_expectancy = float(parts[2])

                if year == year_of_interest:
                    if life_expectancy < year_min:
                        year_min = life_expectancy
                        min_country = country
                    if life_expectancy > year_max:
                        year_max = life_expectancy
                        max_country = country

        print(f"\nFor the year {year_of_interest}:")
        print(f"The average life expectancy across all countries was {average_life_expectancy:.2f}")
        print(f"The max life expectancy was in {max_country} with {year_max:.2f}")
        print(f"The min life expectancy was in {min_country} with {year_min:.2f}")
    else:
        print(f"No data available for the year {year_of_interest}.")

except FileNotFoundError:
    print(f"Error: The file at '{file_path}' was not found. Please check the path and try again.")
except Exception as e:
    print(f"An error occurred: {e}")