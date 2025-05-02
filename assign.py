from datetime import datetime

def difference(date1: str, date2: str) -> int:
    """
    Calculates the difference in days between two dates.
    
    Parameters:
    - date1 (str): The first date in 'YYYY-MM-DD' format.
    - date2 (str): The second date in 'YYYY-MM-DD' format.
    
    Returns:
    - int: Number of days between date1 and date2.
    
    Raises:
    - ValueError: If input dates are not in the correct format.
    
    Example:
    >>> days_between_dates('2025-01-01', '2025-01-10')
    9
    """
    try:
        d1 = datetime.strptime(date1, "%Y-%m-%d")
        d2 = datetime.strptime(date2, "%Y-%m-%d")
        return abs((d2 - d1).days)
    except ValueError:
        raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")
    
    #call function with two dates
print(difference("2025-11-23", "2025-11-25"))
