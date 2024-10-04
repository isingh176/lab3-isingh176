#!/usr/bin/env python3

# Author ID: isingh176

import subprocess

# Function to get free disk space on the root directory
def free_space():
    # Run the 'df' command with appropriate flags and pipes
    result = subprocess.run("df -h | grep '/$' | awk '{print $4}'", shell=True, stdout=subprocess.PIPE, text=True)
    
    # Return the result as a UTF-8 string, stripped of newline characters
    return result.stdout.strip()

if __name__ == '__main__':
    # Print the free space when the script is run directly
    print(free_space())
