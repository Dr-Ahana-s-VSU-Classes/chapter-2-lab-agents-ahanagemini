def ReflexVacuumAgent(percept):
    """
    Implementation of the algorithm in Figure 2.8.
    Input: percept - A tuple (location, status)
    Output: action - 'Suck', 'Left', or 'Right'
    """
    location, status = percept

    if status == 'Dirty':
        return 'Suck'
    elif location == 'A':
        return 'Right'
    elif location == 'B':
        return 'Left'

    return None
