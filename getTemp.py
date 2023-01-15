import pymysql

class temp:
    def Temprature():
        conn=pymysql.connect(host="localhost", #connect Database 
                                        user="raspi_user",
                                        passwd="password",
                                        db="raspi_db")

        sql = "SELECT value1,value2 FROM collect_data ORDER BY collect_time DESC LIMIT 1" #DB에 저장된 센서 값 중 가장 최신 값 불러옴
        with conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                result = cur.fetchall()
                sensorData = result[0]
        temp = sensorData[0] 
        hum = sensorData[1]
        return f'온도: {temp}*c 습도: {hum}%'
