**Assumptions**

# First priority is to give cheapest available space for a vehicle
# Second priority is to keep consecutive spaces available for buses
# Third priority is to give space near the entry
# Fourth priority is to give every vehicle something to park
# For handicapped people, if space other than handicapped space is assigned, he/she is charged according to the rate of the type of space.
# For handicapped people, first priority is handicapped space. If not available, larger space is priority over cheaper space
# Smaller cars do not have a parking at 1st floor. Hence, there's going to be compromise with the 'near to the entrance' preferance rather than to the 'cheaper place available' preference
# Assuming that rounding the parking time upto the nearest MINIMUM_PARKING_INTERVAL_SECONDS means that anything less than MINIMUM_PARKING_INTERVAL_SECONDS gets bumped up to MINIMUM_PARKING_INTERVAL_SECONDS rather than pushed down to 0 and each chargable time interval is rounded up to higher multiple of MINIMUM_PARKING_INTERVAL_SECONDS
# Assuming that rounding off the amount charged to the nearest penny follows the mechanism of 'round' method in mathematics and python.
# Assuming that giving handicapped people large car space if handicapped space is not available has more priority than saving consecutive block of large car spaces for buses.
