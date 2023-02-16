def study_schedule(permanence_period, target_time):
    count = 0
    try:
        for start, end in permanence_period:
            if target_time >= start and target_time <= end:
                count += 1
        return count
    except TypeError:
        return None
