"""
CP1404 Practical
Silver Service Taxi Class (Derived from Taxi Class)
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent silver service taxi"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise Silver Service Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string representation"""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(),
                                                    self.flagfall)

    def get_fare(self):
        """Get current fare."""
        return self.flagfall + super().get_fare()
