import requests
import datetime
end_date = datetime.date.today().strftime("%Y-%m-%d")
url = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=FIPS:27&datatypeid=TMAX&startdate=2016-05-01&enddate=2016-05-01'
url_2 = 'http://www.ncdc.noaa.gov/cdo-web/api/v2/locations?locationcategoryid=CITY&sortfield=name&sortorder=desc&limit=52'
headers = {'token': 'oZAkdjVeaJXhsSDLcchbcqWUyXlJDdOX'}
response = requests.get(url, headers=headers)
print (response.text)
