import RPi.GPIO as GPIO
import sys
import time
import Adafruit_DHT as dht
import pymysql

def runTempSensor():
        sensor = dht.DHT11 #센서
        conn=pymysql.connect(host="localhost",
                                        user="raspi_user",
                                        passwd="password",
                                        db="raspi_db")
#host=서버주소, user=사용자, passwd=서버암호, db=데이터베이스, 스키마 이름, charset=문자세트(utf8)
        pin = 4  #온습도센서 GPIO 핀번호
        try:
                with conn.cursor() as cur : #커서객체 생성, 커서 객체에 DB작업을 위한 함수들이 포함되어 있기 때문에 생성
                        sql="insert into collect_data(sensor, collect_time, value1, value2) values(%s, %s, %s, %s)"
                        while True:
                                humidity, temperature = dht.read_retry(sensor, pin)
                                if humidity is not None and temperature is not None:
                                        cur.execute(sql,
                                                        ('DHT11',time.strftime("%Y-%m-%d %H:%M",time.localtime()), temperature, humidity))
                                #cur.execute('sql실행문')
                                #time.strftime('포맷',시간객체):날짜/시간 객체를 문자열로
                                #time.localtime()=time에서 반환한 값을 날짜와 시간 형태로 변환
                                        conn.commit() #입력한 데이터 저장
                                else:
                                        print("Failed to get reading.")
                                time.sleep(10)
        except KeyboardInterrupt :
                exit()
        finally:
                conn.close() #연결 종료
