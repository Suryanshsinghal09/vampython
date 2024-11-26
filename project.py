class Flight:
    def _init_(self, flight_id, origin, destination, price, seats_available):
        self.flight_id = flight_id
        self.origin = origin
        self.destination = destination
        self.price = price
        self.seats_available = seats_available

    def book_seat(self):
        if self.seats_available > 0:
            self.seats_available -= 1
            return True
        return False

    def _str_(self):
        return f"Flight ID: {self.flight_id} | {self.origin} -> {self.destination} | Price: ${self.price} | Seats Available: {self.seats_available}"


class FlightBookingSystem:
    def _init_(self):
        self.flights = [
            Flight(101, "New York", "London", 500, 50),
            Flight(102, "Los Angeles", "Tokyo", 700, 30),
            Flight(103, "San Francisco", "Paris", 600, 40),
            Flight(104, "Chicago", "Dubai", 800, 20),
            Flight(105, "Miami", "Berlin", 550, 60)]

    def display_flights(self):
        print("Available Flights:")
        for flight in self.flights:
            print(flight)

    def search_flights(self, origin, destination):
        available_flights = [flight for flight in self.flights if flight.origin.lower() == origin.lower() and flight.destination.lower() == destination.lower()]
        return available_flights

    def book_flight(self, flight_id):
        for flight in self.flights:
            if flight.flight_id == flight_id:
                if flight.book_seat():
                    print(f"Booking successful for {flight.origin} -> {flight.destination}.")
                    return True
                else:
                    print("Sorry, no seats available on this flight.")
                    return False
        print("Flight not found.")
        return False


def main():
    system = FlightBookingSystem()

    while True:
        print("\nFlight Booking System")
        print("1. Display Available Flights")
        print("2. Search Flights by Origin and Destination")
        print("3. Book a Flight")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            system.display_flights()
        elif choice == '2':
            origin = input("Enter origin city: ")
            destination = input("Enter destination city: ")
            available_flights = system.search_flights(origin, destination)
            if available_flights:
                print("Available Flights:")
                for flight in available_flights:
                    print(flight)
            else:
                print(f"No flights found from {origin} to {destination}.")
        elif choice == '3':
            flight_id = int(input("Enter Flight ID to book: "))
            system.book_flight(flight_id)
        elif choice == '4':
            print("Thank you for using the Flight Booking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "_main_":
    main()