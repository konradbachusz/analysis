


sql = {'sql_test' : """
		SELECT * FROM rw.blue_move
		limit 10 
		""",

		# --------------------		

		
		'sql_trips':"""

		  WITH fleet_team_id AS
	  (SELECT member_id
	   FROM ana.members
	   WHERE ROLE != 'customer' )
	SELECT t.booking_start_date,
	       t.trip_start_date,
	       date(t.booking_start_date) AS book_start_day,
	       date(t.trip_start_date) AS trip_start_day,
	       t.vin,
	       t.member_id,
	       sz.name AS start_zone_name,
	       ez.name AS end_zone_name,
	       t.start_lat,
	       t.start_lon,
	       t.end_lat,
	       t.end_lon,
	       t.distance,
	       t.trip_duration
	FROM prc.trips t
	LEFT JOIN rw.quartiers sz ON st_contains(sz.geom, t.start_pos_gis)
	LEFT JOIN rw.quartiers ez ON st_contains(ez.geom, t.end_pos_gis)
	WHERE member_id IN
	    (SELECT *
	     FROM fleet_team_id)
	  AND trip_duration > 0
	  AND date(t.trip_start_date) >= '2018-01-01'

	   """}





