import psycopg
import etl

if __name__ == '__main__':
    extracted_data = etl.extract_from_dmi("2018-02-12T01:00:00Z/2018-02-12T01:00:00Z", 100, 0)
    transformed_data = etl.transform(extracted_data)
    etl.load_humidity(transformed_data)
    etl.load_temp_dry(transformed_data)
    etl.load_pressure(transformed_data)
    extracted_data_S_API=etl.extract_from_specialisterne_API("2026-10-28 14:48:29.281465 UTC/2026-10-28 14:48:36.483821 UTC",100,0)
    transormed_data_S_API=etl.transform_S_API_Data(extracted_data_S_API)
    etl.load_humidity(transormed_data_S_API)
    etl.load_temp_dry(transormed_data_S_API)
    etl.load_pressure(transormed_data_S_API)