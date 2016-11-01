import requests
import datetime
from token import get_token

end_date = datetime.date.today().strftime("%Y-%m-%d")
url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&datatypeid=TAVG&locationid=FIPS:27&startdate=2016-01-01&enddate=2016-01-31&units=standard'
url_2 = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CITY&sortfield=name&sortorder=desc&limit=52'
url_3 = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/datatypes/TMAX'
token = get_token()
headers = {'token': token}
response = requests.get(url, headers=headers)
print (response.text)
