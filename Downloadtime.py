import sys
import random

def calculate_download_time(size_gb, download_speed_mbps):
    # Convert download speed to megabytes per second
    download_speed_mbps = download_speed_mbps / 8  # 1 byte = 8 bits
    # Calculate download time in seconds
    download_time_seconds = (size_gb * 1024) / download_speed_mbps
    # Convert download time to hours, minutes, and seconds
    download_time_hours = int(download_time_seconds // 3600)
    download_time_seconds %= 3600
    download_time_minutes = int(download_time_seconds // 60)
    download_time_seconds %= 60

    return download_time_hours, download_time_minutes, download_time_seconds

def main():
    print("Welcome to the Game Download Time Calculator")

    fluctuation_enabled = input("Do you want to consider internet speed fluctuations? (yes/no): ").strip().lower()

    try:
        # Input game size in gigabytes
        game_size_gb = float(input("Enter the game size in gigabytes: "))
        if game_size_gb <= 0:
            raise ValueError("Game size must be a positive number.")

        if fluctuation_enabled == "yes":
            # Input lowest and highest download speed in megabits per second
            lowest_speed_mbps = float(input("Enter the lowest download speed in megabits per second: "))
            highest_speed_mbps = float(input("Enter the highest download speed in megabits per second: "))
            if lowest_speed_mbps <= 0 or highest_speed_mbps <= 0 or lowest_speed_mbps > highest_speed_mbps:
                raise ValueError("Invalid speed range. Both speeds must be positive, and lowest speed must be less than or equal to highest speed.")

            # Simulate internet speed fluctuations within the specified range
            download_speed_mbps = random.uniform(lowest_speed_mbps, highest_speed_mbps)
        else:
            # Input download speed in megabits per second
            download_speed_mbps = float(input("Enter the download speed in megabits per second: "))
            if download_speed_mbps <= 0:
                raise ValueError("Download speed must be a positive number.")

        # Calculate download time
        download_time_hours, download_time_minutes, download_time_seconds = calculate_download_time(game_size_gb, download_speed_mbps)

        # Display the download time
        print(f"Download time: {download_time_hours} hours, {download_time_minutes} minutes, {download_time_seconds} seconds. Made by Monstie")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
