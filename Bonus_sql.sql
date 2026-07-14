/*
Wingz Django Assessment
Bonus SQL Query (PostgreSQL)


Function:
Return each ride together with:
- Rider information
- Driver information
- Latest ride event
- Trip duration in minutes
*/

WITH latest_events AS (
    SELECT
        id_ride_id,
        MAX(created_at) AS latest_event_time
    FROM rides_rideevent
    GROUP BY id_ride_id
)

SELECT
    r.id_ride,
    rider.username AS rider_username,
    driver.username AS driver_username,
    r.status,
    r.pickup_time,
    le.latest_event_time,

    ROUND(
        EXTRACT(
            EPOCH FROM (
                le.latest_event_time - r.pickup_time
            )
        ) / 60,
        2
    ) AS trip_duration_minutes

FROM rides_ride r

JOIN rides_user rider
    ON rider.id = r.id_rider_id

JOIN rides_user driver
    ON driver.id = r.id_driver_id

LEFT JOIN latest_events le
    ON le.id_ride_id = r.id_ride

ORDER BY
    r.pickup_time DESC;