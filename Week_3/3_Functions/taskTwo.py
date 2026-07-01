# Mini Project 16: Movie Ticket Booking

# Requirement
# Create functions to:
    # Select movie
    # Choose seats
    # Calculate ticket price
    # Confirm booking

# Function to select a movie
def select_movie(movie_name):
    print("Select Movie", movie_name)
    return movie_name

# Function to choose seats
def choose_seats(number_of_seats):
    print("Seats Booked", number_of_seats)
    return number_of_seats

# Function to calculate total price
def calculate_ticket_price(number_of_seats):
    ticket_price = 200
    total = number_of_seats * ticket_price
    return total

# Function to confirm booking
def confirm_booking(movie_name, seats, total_price):
    print("\nBooking Confirmed")
    print("Movie :", movie_name)
    print("Seats :", seats)
    print("Total Price :", total_price)

# Function Calls
movie = select_movie("Rocket Tree")
seats = choose_seats(3)
price = calculate_ticket_price(seats)

confirm_booking(movie, seats, price)