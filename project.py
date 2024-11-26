class Flight:
    def __init__(self, flight_id, airline, source, destination, date, total_seats):
        self.flight_id = flight_id
        self.airline = airline
        self.source = source
        self.destination = destination
        self.date = date
        self.total_seats = total_seats
        self.booked_seats = 0
    
    def is_available(self):
        return self.total_seats - self.booked_seats > 0
    
    def book_seat(self):
        if self.is_available():
            self.booked_seats += 1
            print(f"Seat booked successfully on Flight {self.flight_id}.")
        else:
            print(f"Sorry, no available seats on Flight {self.flight_id}.")

    def __str__(self):
        return f"Flight {self.flight_id} - {self.airline}\nFrom: {self.source} to {self.destination}\nDate: {self.date}\nSeats Available: {self.total_seats - self.booked_seats}"


class FlightBookingSystem:
    def __init__(self):
        self.flights = []
    
    def add_flight(self, flight):
        self.flights.append(flight)
    
    def search_flights(self, source, destination, date):
        available_flights = []
        for flight in self.flights:
            if flight.source == source and flight.destination == destination and flight.date == date:
                available_flights.append(flight)
        return available_flights
    
    def book_flight(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                flight.book_seat()
                return
        print("Flight not found.")
    
    def show_flights(self, available_flights):
        if not available_flights:
            print("No available flights found.")
            return
        for flight in available_flights:
            print(flight)
            print("-" * 50)


def main():
    # Initialize the flight booking system
    system = FlightBookingSystem()
    
    # Add some sample flights to the system
    flight1 = Flight("AI101", "Air India", "New York", "London", "2024-12-25", 100)
    flight2 = Flight("BA202", "British Airways", "New York", "London", "2024-12-25", 50)
    flight3 = Flight("UA303", "United Airlines", "New York", "Paris", "2024-12-25", 70)
    
    system.add_flight(flight1)
    system.add_flight(flight2)
    system.add_flight(flight3)
    
    print("Welcome to the Flight Booking System!")
    
    # Search for available flights
    source = input("Enter source city: ")
    destination = input("Enter destination city: ")
    date = input("Enter date of travel (YYYY-MM-DD): ")

    available_flights = system.search_flights(source, destination, date)
    system.show_flights(available_flights)
    
    # Book a flight if available
    if available_flights:
        flight_id = input("Enter the flight ID to book a seat: ")
        system.book_flight(flight_id)
        
        # Show updated flight details
        system.show_flights(system.search_flights(source, destination, date))


if __name__ == "__main__":
    main()