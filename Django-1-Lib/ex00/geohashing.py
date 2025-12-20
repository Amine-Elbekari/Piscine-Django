import antigravity
import sys

def calculate_geohashing():
    if len(sys.argv) != 4:
        raise Exception('Usage: python3 geohashing.py <latitude> <longitude> <datedow>')
    try:    
        latitude = float(sys.argv[1])
        longtitude = float(sys.argv[2])
    except ValueError:
        raise Exception('Error: Latitude and Longtitude must be numbers!')
    datedow = sys.argv[3].encode('utf-8')
    antigravity.geohash(latitude, longtitude, datedow)

if __name__ == "__main__":
    try:
        calculate_geohashing()
    except Exception as e:
        print(e)