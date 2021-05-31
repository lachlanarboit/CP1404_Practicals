"""
CP1404 Practical
Silver Service Taxi Class Tests
"""

from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 1)
    taxi.drive(123)
    print(taxi)
    print(taxi.get_fare())


main()
