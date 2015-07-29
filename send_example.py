
import pandas as pd
import json
import psycopg2

def send_example_json():
        conn_dict = {'dbname':'con_dist', 'user':'zeintawil', 'password': '', 'host':'/tmp'}
        conn = psycopg2.connect(dbname=conn_dict['dbname'], user=conn_dict['user'], host='/tmp')
        cur = conn.cursor()

        map_query = """
        				SELECT
                        DISTINCT
                        ST_asGEOJSON(wkb_geometry) geometry
                        , startcong
                        , statename
                        , district
                        , c.color
                        FROM district_shapes d
                        JOIN unique_colors c
                                ON cast(d.district as int) = c.dist_num
                        WHERE 113 BETWEEN CAST(startcong as INT) AND CAST(endcong as INT) and Statename='Texas' """ 

        df = pd.read_sql(map_query, conn)


        def add_properties_geo(row):
        	statename = row['statename']
        	district = row['district']
        	startcong = row['startcong']
        	hexcolor = row['color']
        	geo_json = {"type": "Feature", "geometry": json.loads(row['geometry']),  "properties": {'statename': statename , 'district': district, 'hexcolor':hexcolor}}
        	return geo_json

        list_to_export = []	
        for idx, row in df.iterrows():
        	list_to_export.append((add_properties_geo(row)))
        return list_to_export