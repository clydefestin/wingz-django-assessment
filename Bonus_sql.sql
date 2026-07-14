/*
Wingz Django Assessment
Bonus SQL (PostgreSQL)

Purpose:
Return the number of trips whose duration from
Pickup to Dropoff exceeded one hour,
grouped by Month and Driver.

Trip duration is calculated using RideEvent timestamps.

Pickup Event:
    'Status changed to pickup'

Dropoff Event:
    'Status changed to dropoff'
*/

WITH trip_events AS (

    SELECT

        r.id_ride,

        d.username AS driver,

        DATE_TRUNC('month', pickup.created_at) AS trip_month,

        pickup.created_at AS pickup_time,

        dropoff.created_at AS dropoff_time,

        EXTRACT(
            EPOCH FROM (
                dropoff.created_at - pickup.created_at
            )
        ) / 3600 AS duration_hours

    FROM rides_ride r

    INNER JOIN rides_user d
        ON d.id = r.id_driver_id

    INNER JOIN rides_rideevent pickup
        ON pickup.id_ride_id = r.id_ride
       AND pickup.description = 'Status changed to pickup'

    INNER JOIN rides_rideevent dropoff
        ON dropoff.id_ride_id = r.id_ride
       AND dropoff.description = 'Status changed to dropoff'

)

SELECT

    TO_CHAR(trip_month, 'YYYY-MM') AS month,

    driver,

    COUNT(*) AS trips_over_1_hour

FROM trip_events

WHERE duration_hours > 1

GROUP BY

    trip_month,
    driver

ORDER BY

    trip_month,
    driver;