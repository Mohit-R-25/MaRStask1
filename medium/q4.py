import statistics

# Grab the raw data from the log file
with open("log.txt", "r") as f:
    data = f.read()

# Convert the string content into a list of floats so we can actually do math
values = list(map(float, data.split()))

def sanchiko(values, window_size):
    
    #Applies a median filter to smooth out outliers or 'spikes' in the data:
    
    filtered_results = []

    # Slide the window across the list
    for i in range(len(values) - window_size + 1):
        window = values[i : i + window_size]
        # Using median here helps ignore extreme noise 
        filtered_results.append(statistics.median(window))

    return filtered_results

def muchiko(values, window_size):
    """
    Applies a moving average to smooth the overall trend.
    """
    filtered_results = []
    
    for i in range(len(values) - window_size + 1):
        window = values[i : i + window_size]
        # Taking the mean gives us that classic 'rolling average' feel
        filtered_results.append(statistics.mean(window))
        
    return filtered_results

# Get the user's preference for how aggressive the smoothing should be
x = int(input("Enter the window size: "))

# First pass: clean up the spikes with the median filter
s_values = sanchiko(values, x)

# Second pass: smooth the remaining data using a slightly smaller window
# Note: x-2 is used here to tighten the moving average relative to the median pass
m_values = muchiko(s_values, x - 2)

# Output the final processed dataset
print(m_values)
