from datetime import datetime, timedelta

def generate_time_conversion_table(start_hour=0, end_hour=23, london_offset=0, denver_offset=-7):
    london_time = datetime(2024, 4, 28, start_hour)  # Starting time in London
    denver_time = london_time + timedelta(hours=denver_offset - london_offset)  # Corresponding Denver time
    
    print("London Time\tDenver Time")
    for hour in range(start_hour, end_hour + 1):
        london_time_str = london_time.strftime("%H:%M")
        denver_time_str = denver_time.strftime("%H:%M")
        print(f"{london_time_str}\t\t{denver_time_str}")
        
        london_time += timedelta(hours=1)
        denver_time += timedelta(hours=1)

generate_time_conversion_table()