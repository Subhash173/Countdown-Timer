
# Import the time module to handle time-related functions
import time  

# Loop until seconds reach zero
def countdown_timer(seconds):
    
    while seconds > 0:
        # Calculate minutes and seconds from total seconds
        mins, secs = divmod(seconds, 60)
        
        # Format the time as MM:SS
        time_format = f'{mins:02}:{secs:02}'
        
        # Print the current time left on the same line and flush the output
        print(time_format, end='\r')
        
        # Pause the program for 1 second
        time.sleep(1)
        
        # Decrease the total time by 1 second
        seconds -= 1
    
    # Print "Time's up!" when the countdown reaches zero
    print("Time's up!")

# Example usage
seconds_input = int(input("Enter the countdown time in seconds: "))  # Get user input
countdown_timer(seconds_input)  # Start the countdown
