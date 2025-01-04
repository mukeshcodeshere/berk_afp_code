# # PSUEDOCODE

# - First, it takes the number of dice and the number of sides on each die as input from the user.
# - Then, it calculates the expected value for rolling just one die (this is simply the average of all the numbers on the die).
# - For more than one die, the program calculates the expected value by considering how the dice values change as you add more dice. It uses the expected value from the previous dice to filter out values that are lower than the previous result, and then calculates the new expected value.
# - It continues this process for all the dice from 1 up to the total number of dice the user specified.


def calculate_expected_value(candidates):
    return sum(candidates) / len(candidates) if candidates else 0

def filter_candidates(candidates, ev_prev):
    return [x for x in candidates if x > ev_prev]

def calculate_ev_for_multiple_dice(candidates, num_dice):
    # Base case: Expected value for 1 die is the average of all candidates
    avg_candidates = calculate_expected_value(candidates)
    expected_values = [avg_candidates]

    for i in range(2, num_dice + 1):
        # Calculate the expected value for the ith die
        ev_prev = expected_values[-1]  # Previous EV (for i-1 dice)
        avg_filtered = calculate_expected_value(filter_candidates(candidates, ev_prev))
        ev_current = (i - 1) / i * ev_prev + 1 / i * avg_filtered 
        expected_values.append(ev_current)
    
    return expected_values

def print_expected_values(expected_values):
    for i, ev in enumerate(expected_values, start=1):
        print(f"Expected Value for {i} Die{'s' if i > 1 else ''}: {ev:.5f}")
        
try:
    # User inputs for the number of dice and number of sides per die
    num_dice = int(input("Enter the number of rolls / trials: "))
    num_sides = int(input("Enter the number of sides on each die: "))
    
    if num_dice < 1 or num_sides < 1:
        print("Please enter positive integers for the number of dice and the number of sides.")
    else:
        # Generate the list of candidates (numbers on each die: 1 to num_sides)
        all_candidates = list(range(1, num_sides + 1))
        expected_values = calculate_ev_for_multiple_dice(all_candidates, num_dice)
        print_expected_values(expected_values)

except ValueError:
    print("Invalid input. Please enter integers")
