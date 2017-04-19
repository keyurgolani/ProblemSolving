def answer(intervals):
    ''' Produce the total time that is covered by at least one interval
        in a list of intervals.
        
        The intervals are (start, end) pairs where start < end.
    '''
    # sorting the list uncovers redundancy
    # reversed sort facilitates efficient popping of earliest-starting interval
    intervals.sort(reverse=True)
    
    unique_intervals = []
    while intervals:
        # take the earliest remaining interval, then guarantee uniqueness
        unique_interval = intervals.pop()
        unique_intervals.append(unique_interval)
        
        # scan the remaining intervals for overlap
        # since we already have the earliest start, anything with an
        # earler stop is redundant
        redundant_intervals = [i for i, interval in enumerate(intervals)
                                 if interval[1] <= unique_interval[1]]
        
        # remove redundant intervals from the end or things get out of order
        for i in sorted(redundant_intervals, reverse=True):
            intervals.pop(i)
    
    merged_intervals = []
    while unique_intervals:
        # since unique_intervals is reverse-sorted by construction, 
        # pop to get the latest ending interval 
        merged_interval = unique_intervals.pop()
        
        # merge any unique intervals that overlap with it, starting with
        # the next-latest ending interval
        for start, stop in reversed(unique_intervals):
            # having a stop time after the latest-ending interval start time
            # defines overlap, meaning we should merge the intervals
            if stop >= merged_interval[0]:
                merged_interval[0] = start # merge by rewriting stop time
                unique_intervals.pop() # and discarding the overlapper
            else:
                break # further iteration is unnecessary because of sorting
        
        merged_intervals.append(merged_interval)
        
    return sum(end-start for start, end in merged_intervals)
    
def better_answer(intervals):
    ''' if the interval numbers are not too big, this solution is awesomer
    '''
    
    monitored_times = set()
    
    for interval in intervals:
        monitored_times.update(range(*interval))
        
    return len(monitored_times)