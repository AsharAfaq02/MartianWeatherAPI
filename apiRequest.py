import requests 
import json
api_key = "CKU9QxpxvX5tTczB93AT7IHEcAc4HkIw3pFgEDwK"
feedtype = "json"
ver = "1.0"
NASA_REQ = requests.get('https://api.nasa.gov/insight_weather/?api_key='+api_key+'&feedtype='+feedtype+'&ver='+ver+'')
Mars_weather = json.loads(NASA_REQ.text)
sol_day = 0
solList = Mars_weather["sol_keys"]
lenSol = len(solList)
SZNarr = []
MNTarr = []
PAarr = []
TMParr = []
while sol_day < lenSol:
	sol = str(solList[sol_day])
	season = str(Mars_weather[sol]["Season"])
	month = str(json.dumps(Mars_weather[sol]["Month_ordinal"]))
	pressure = str(json.dumps(Mars_weather[sol]["PRE"]["av"]))
	Temp = "" #temp is not avail on NASA API currently

	SZNarr.insert(sol_day, season)
	MNTarr.insert(sol_day, month)
	PAarr.insert(sol_day, pressure)
	TMParr.insert(sol_day, Temp)


	sol_day = sol_day + 1


	data = {}

	data["solList"] = (solList)
	data["Season"] = (SZNarr)
	data["Month"] = (MNTarr)
	data["PressureAvg"] = (PAarr)
	data["Tempurature"] = (TMParr)

	f = open("./templates/mars.json", "w")
	f.write(json.dumps(data))

	f.close()

print("Status: working")