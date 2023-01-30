from geopy.distance import geodesic


potential_client_one = (51.5074, 0.1278)
potential_client_two = (40.7128, 74.0060)
print('The two clients are {} miles apart'.format(
    geodesic(potential_client_one, potential_client_two).miles))