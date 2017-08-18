import math

class Calculator:
    """Simple class implementing a calculator with basic operations."""

    @staticmethod
    def add(arg1,arg2):
        """Return the sum of arg1 and arg2"""
        return(arg1+arg2)
    @staticmethod
    def sub(arg1,arg2):
        """Return the difference between arg1 and arg2"""
        return(arg1-arg2)
    @staticmethod
    def mul(arg1,arg2):
        """Return the product of arg1 and arg2"""
        return (arg1*arg2)
    @staticmethod
    def div(arg1,arg2):
        """Return the division between arg1 and arg2"""
        return (arg1/arg2)
    @staticmethod
    def sqrt(arg1):
        """Return the square root of arg1"""
        return math.sqrt(arg1)
