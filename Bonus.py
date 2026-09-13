# A nested dictionary to store weather data: {city: {date: {temperature, humidity, condition}}}
weather_data = {}

def add_weather_data():
    print("\n--- Add Weather Data ---")
    city = input("Enter city name: ").strip().capitalize()
    date = input("Enter date (YYYY-MM-DD): ").strip()
    temperature = input("Enter temperature: ").strip()
    humidity = input("Enter humidity: ").strip()
    condition = input("Enter weather condition: ").strip()
    
    # If the city is not in the dictionary, create an entry for it
    if city not in weather_data:
        weather_data[city] = {}
        
    # Store the weather details under the specific date
    weather_data[city][date] = {
        "temperature": temperature,
        "humidity": humidity,
        "condition": condition
    }
    print(f"Success! Weather data for {city} on {date} has been added.\n")

def query_weather_data():
    print("\n--- Query Weather Data ---")
    city = input("Enter the city name to see the weather details: ").strip().capitalize()
    
    if city in weather_data:
        print(f"\nWeather Details for {city}:")
        for date, details in weather_data[city].items():
            print(f"  Date: {date}")
            print(f"    - Temperature: {details['temperature']}")
            print(f"    - Humidity: {details['humidity']}")
            print(f"    - Condition: {details['condition']}")
        print()
    else:
        print(f"Sorry, no weather data found for '{city}'.\n")

# Main program loop
def main():
    while True:
        print("=== Weather Data Aggregation System ===")
        print("1. Add Weather Data")
        print("2. Query Weather Data")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ").strip()
        
        if choice == '1':
            add_weather_data()
        elif choice == '2':
            query_weather_data()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.\n")

if __name__ == "__main__":
    main()