Globe
=====

Utilities for manipulation of latitude and longitude


Checking if a Latitude or Longitude is Valid
--------------------------------------------

A latitude is valid if it is a float or integer and is in the range
[-90, 90]. A longitude is valid if it is a float or integer and is in
the range [-180, 180]. These two methods simply return a boolean
indicating whether or not the latitude or longitude meets these criteria.

.. code :: python

    lat = 45.2
    globe.is_lat_valid(lat)  # Returns True

    lon = -190
    globe.is_lon_valid(lon)  # Returns False


Distances from a Pair of Latitude and Longitudes
------------------------------------------------

The ``globe.distance`` method uses the Vincenty formula to calculate the distance between two
points on Earth. Earth is assumed spherical and the distance is in meters.

.. code :: python

    distance = globe.distance(lat1, lon1, lat2, lon2)


Teleporting
-----------

The ``globe.teleport`` method returns a random latitude and longitude given some intial latitude and longitude and a typical distance (in meters). The actual distance is randomly calculated from a Gaussian distribution with a width equal to the typical distance. The angle between the initial and final points is selected randomly.

.. code :: python

    (newlat, newlon) = globe.teleport(lat, lon, 1000)


Other Utilities
---------------

The ``globe.latlon2sc`` method converts a latitude and longitude to
spherical coordinates on the unit sphere:

.. code :: python

    (theta, phi) = globe.latlon2sc(0, 30)

