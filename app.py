#!/usr/bin/env python

from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
import urllib.request, urllib.parse, urllib.error
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

'''
import apiai
CLIENT_ACCESS_TOKEN = '9964b46aafa34cfd8b1a414b31abc819'
PAGE_ACCESS_TOKEN = 'EAAODZBYcpPmkBAGtnxJ5FbERHR5hnBfbAvBeXTKGIefcNAzILPRz0cM8EACKnZCk4KEmxX5UnHP4WuC7CAFovMq8Fmosjl5PzsHHxCZCHTcSB134FuDWybuA9o4P7ZAIBo5RTHszaxn9gZC66O6adAtqgZAR18W8PGL8Gni9bOFAZDZD'
VERIFY_TOKEN = '9964b46aafa34cfd8b1a414b31abc819'
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

access_token = 'EAAODZBYcpPmkBAEj9EVraapZA3US5ZCo9A084X8AT8hqOiPRcUpecq7SLzEyvJKbibIjn8nLTtvUwCBmLOJQu7j8nIUEVGYX9D94PkDJ50ZCT5k0wUguYNQx3zgvs9ZATHmxOwFXn5snFR10rnwdxKXsyHdGV7bUXkYgrzWecMgZDZD'


@app.route('/', methods=['GET'])
def handle_verification():
    if (request.args.get('hub.verify_token', '') == VERIFY_TOKEN):
        print("Verified")
        return request.args.get('hub.challenge', '')
    else:
        print("Wrong token")
        return "Error, wrong validation token"

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

  @app.route('/', methods=['POST'])
def handle_message():
   
  #  Handle messages sent by facebook messenger to the applicaiton
    
    data = request.get_json()

    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):

                    sender_id = messaging_event["sender"]["id"]        
                    recipient_id = messaging_event["recipient"]["id"]  
                    message_text = messaging_event["message"]["text"]  
                    send_message_response(sender_id, parse_natural_text(message_text))


    return "ok"

def send_message(sender_id, message_text):
    
  #  Sending response back to the user using facebook graph API
    
    r = requests.post("https://graph.facebook.com/v2.6/me/messages",

        params={"access_token": PAGE_ACCESS_TOKEN},

        headers={"Content-Type": "application/json"},

        data=json.dumps({
        "recipient": {"id": sender_id},
        "message": {"text": message_text}
    }))
	
	def parse_user_text(user_text):

    
   # Send the message to API AI which invokes an intent
   # and sends the response accordingly
    #The bot response is appened with weaher data fetched from
    #open weather map client
    

    request = ai.text_request()
    request.query = user_text

    response = json.loads(request.getresponse().read().decode('utf-8'))
    responseStatus = response['status']['code']
    if (responseStatus == 200):
        print("Bot response", response['result']['fulfillment']['speech'])

        weather_report = ''

        input_city = response['result']['parameters']['geo-city']

        #Fetching weather data
        owm = pyowm.OWM('023231a7fc73d296d874874991856cfb')  # You MUST provide a valid API key

        forecast = owm.daily_forecast(input_city)

        observation = owm.weather_at_place(input_city)
        w = observation.get_weather()
        print(w)                      
        print(w.get_wind())                 
        print(w.get_humidity())      
        max_temp = str(w.get_temperature('celsius')['temp_max'])  
        min_temp = str(w.get_temperature('celsius')['temp_min'])
        current_temp = str(w.get_temperature('celsius')['temp'])
        wind_speed = str(w.get_wind()['speed'])
        humidity = str(w.get_humidity())
        weather_report = ' max temp: ' + max_temp + ' min temp: ' + min_temp + ' current temp: ' + current_temp + ' wind speed :' + wind_speed + ' humidity ' + humidity + '%'
        print("Weather report ", weather_report)
        return (response['result']['fulfillment']['speech'] + weather_report)
    else:
        return ("Please try again")


def send_message_response(sender_id, message_text):
    sentenceDelimiter = ". "
    messages = message_text.split(sentenceDelimiter)

    for message in messages:
        send_message(sender_id, message)
'''
	
	
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
				#SI DANNI STRADALI
	if req.get("result").get("action") == "forniture-demage.forniture-demage-yes":
		result = req.get("result")
		parameters = result.get("parameters")
					#NO FERITI
		if req.get("result")["contexts"][0]["name"]=="domanda3":
			licenseplate = 		req.get("result")["contexts"][2]["parameters"].get("number-sequence")
			dateloss = 		req.get("result")["contexts"][2]["parameters"].get("date")
			timeloss = 		req.get("result")["contexts"][2]["parameters"].get("time")
			cityloss = 		req.get("result")["contexts"][2]["parameters"].get("geo-city")
			name_other_driver = 	req.get("result")["contexts"][2]["parameters"].get("namedriver2")
			surname_other_driver = 	req.get("result")["contexts"][2]["parameters"].get("surnamedriver2")
			datedriver2 = 		req.get("result")["contexts"][2]["parameters"].get("date-otherdriver")
			driver2_license_number =req.get("result")["contexts"][2]["parameters"].get("license_driving")
			driver2_license_plate = req.get("result")["contexts"][2]["parameters"].get("license-plate")
			ass = 			req.get("result")["contexts"][2]["parameters"].get("assicurazione")
			danni=			req.get("result")["contexts"][1]["parameters"].get("forniture-demage")

			license = "Dear costumer, the claim of you car accident, with these details:\n-LICENSE PLATE NUMBER: "+licenseplate+"\n-DATE OF THE ACCIDENT: "+dateloss+"\n-TIME OF THE ACCIDENT: "+timeloss+"\n-PLACE OF THE ACCIDENT: "+cityloss+"\nhas been correct registered.\n\nPlease use claim no. 12345 for reference" 
			important="\n\n******** IMPORTANT ********\n\nThe schedule of the third part driver involved in the accident is:\n-NAME: "+name_other_driver+"\n-SURNAME: "+surname_other_driver+"\n-DATE OF BIRTH: "+datedriver2+"\n-LICENSE NUMBER: "+driver2_license_number+"\n-LICENSE PLATE NUMBER: "+driver2_license_plate+"\n-INSURANCE: "+ass
			#funziona posizione=" posizione 0 e "+req.get("result")["contexts"][0]["name"]+"\nposizione 1 "+req.get("result")["contexts"][1]["name"]+ "posizione 2 "+req.get("result")["contexts"][2]["name"]+" facciamo prova e vediamo se alcuni dati inseriti vanno bene "+name_other_driver+" "+surname_other_driver+" "+cityloss
						#SI POLIZIA
			if len(req.get("result")["contexts"][1]["parameters"]) > 2:
				Ndenuncia = 	req.get("result")["contexts"][1]["parameters"].get("complain-number")
				agentID = 	req.get("result")["contexts"][1]["parameters"].get("agent-id")

				extra2="\nThere were not injured.\nThe police have been called. The complain "+Ndenuncia+" by Agent "+agentID+" was properly loaded.\nThere were street forniture demages:\n-"+danni
				prova="11.57 "+str(len(req.get("result")["contexts"][1]["parameters"]))+" "+license+important+extra2
				res = makeWebhookResult(prova)
				return res
						#NO POLIZIA
			elif len(req.get("result")["contexts"][1]["parameters"]) == 2:
				extra1="\nThere were not injured.\nThe police have not been called.\nThere were street forniture demages:\n-"+danni
				prova1=license+important+extra1
				res = makeWebhookResult(prova1)
				return res
					#SI FERITI
		if req.get("result")["contexts"][0]["name"]=="posicion":
			licenseplate = 		req.get("result")["contexts"][4]["parameters"].get("number-sequence")
			dateloss = 		req.get("result")["contexts"][4]["parameters"].get("date")
			timeloss = 		req.get("result")["contexts"][4]["parameters"].get("time")
			cityloss = 		req.get("result")["contexts"][4]["parameters"].get("geo-city")
			name_other_driver = 	req.get("result")["contexts"][4]["parameters"].get("namedriver2")
			surname_other_driver = 	req.get("result")["contexts"][4]["parameters"].get("surnamedriver2")
			datedriver2 = 		req.get("result")["contexts"][4]["parameters"].get("date-otherdriver")
			driver2_license_number =req.get("result")["contexts"][4]["parameters"].get("license_driving")
			driver2_license_plate = req.get("result")["contexts"][4]["parameters"].get("license-plate")
			ass = 			req.get("result")["contexts"][4]["parameters"].get("assicurazione")
			danni=			req.get("result")["contexts"][3]["parameters"].get("forniture-demage")
			
			name_injured = 		req.get("result")["contexts"][4]["parameters"].get("name-injiured")
			surname_injured = 	req.get("result")["contexts"][4]["parameters"].get("surname-injured")
			part_injured = 		req.get("result")["contexts"][4]["parameters"].get("injury-part")
			seat = 			req.get("result")["contexts"][4]["parameters"].get("seat-position")
			
			license = "Dear costumer, the claim of you car accident, with these details:\n-LICENSE PLATE NUMBER: "+licenseplate+"\n-DATE OF THE ACCIDENT: "+dateloss+"\n-TIME OF THE ACCIDENT: "+timeloss+"\n-PLACE OF THE ACCIDENT: "+cityloss+"\nhas been correct registered.\n\nPlease use claim no. 12345 for reference" 
			important="\n\n******** IMPORTANT ********\n\nThe schedule of the third part driver involved in the accident is:\n-NAME: "+name_other_driver+"\n-SURNAME: "+surname_other_driver+"\n-DATE OF BIRTH: "+datedriver2+"\n-LICENSE NUMBER: "+driver2_license_number+"\n-LICENSE PLATE NUMBER: "+driver2_license_plate+"\n-INSURANCE: "+ass
			#injured=" vediamo se funziona."
			injured="\n\n***** VERY IMPORTANT *****\n\nTHE PASSENGER: "+name_injured+" "+surname_injured+"; was injured in the "+part_injured+". "+name_injured+" found himself in "+seat+"."
			#speech=" posizione 0 e "+req.get("result")["contexts"][0]["name"]+"\nposizione 1 "+req.get("result")["contexts"][1]["name"]+"\nposizione 2 "+req.get("result")["contexts"][2]["name"]+"\nposizione 3 "#+req.get("result")["contexts"][3]["name"]+"\nposizione 4 "+req.get("result")["contexts"][4]["name"]
			#res = makeWebhookResult(speech)
			#return res
						#SI POLIZIA
			if len(req.get("result")["contexts"][0]["parameters"]) > 6:
				Ndenuncia = 	req.get("result")["contexts"][2]["parameters"].get("complain-number")
				agentID = 	req.get("result")["contexts"][2]["parameters"].get("agent-id")
				extra2="\nThe police have been called.The complain number: "+Ndenuncia+" taken by Agent "+agentID+", was properly loaded.\nThere were street forniture demages:\n"+danni
				prova=license+important+injured+extra2
				res = makeWebhookResult(prova)
				return res
						#NO POLIZIA
			elif len(req.get("result")["contexts"][0]["parameters"]) == 6:
				extra1="\nThe police have not been called.\nThere were street forniture demages:\n"+danni
				prova1=license+important+injured+extra1
				res = makeWebhookResult(prova1)
				return res

	
				#NO DANNI STRADALI
	if req.get("result").get("action") == "forniture-demage.forniture-demage-no":
		result = req.get("result")
		parameters = result.get("parameters")
					#NO FERITI
		if req.get("result")["contexts"][0]["name"]=="domanda3":
			licenseplate = 		req.get("result")["contexts"][2]["parameters"].get("number-sequence")
			dateloss = 		req.get("result")["contexts"][2]["parameters"].get("date")
			timeloss = 		req.get("result")["contexts"][2]["parameters"].get("time")
			cityloss = 		req.get("result")["contexts"][2]["parameters"].get("geo-city")
			name_other_driver = 	req.get("result")["contexts"][2]["parameters"].get("namedriver2")
			surname_other_driver = 	req.get("result")["contexts"][2]["parameters"].get("surnamedriver2")
			datedriver2 = 		req.get("result")["contexts"][2]["parameters"].get("date-otherdriver")
			driver2_license_number =req.get("result")["contexts"][2]["parameters"].get("license_driving")
			driver2_license_plate = req.get("result")["contexts"][2]["parameters"].get("license-plate")
			ass = 			req.get("result")["contexts"][2]["parameters"].get("assicurazione")

			license = "Dear costumer, the claim of you car accident, with these details:\n-LICENSE PLATE NUMBER: "+licenseplate+"\n-DATE OF THE ACCIDENT: "+dateloss+"\n-TIME OF THE ACCIDENT: "+timeloss+"\n-PLACE OF THE ACCIDENT: "+cityloss+"\nhas been correct registered.\n\nPlease use claim no. 12345 for reference" 
			important="\n\n******** IMPORTANT ********\n\nThe schedule of the third part driver involved in the accident is:\n-NAME: "+name_other_driver+"\n-SURNAME: "+surname_other_driver+"\n-DATE OF BIRTH: "+datedriver2+"\n-LICENSE NUMBER: "+driver2_license_number+"\n-LICENSE PLATE NUMBER: "+driver2_license_plate+"\n-INSURANCE: "+ass

			#speech=" posizione 0 e "+req.get("result")["contexts"][0]["name"]+"\nposizione 1 "+req.get("result")["contexts"][1]["name"]+"\nposizione 2 "+req.get("result")["contexts"][2]["name"]+"\nposizione 3 "#+req.get("result")["contexts"][3]["name"]+"\nposizione 4 "+req.get("result")["contexts"][4]["name"]
			#res = makeWebhookResult(speech)
			#return res
						#SI POLIZIA
			if len(req.get("result")["contexts"][1]["parameters"]) != 0:
				Ndenuncia = 	req.get("result")["contexts"][1]["parameters"].get("complain-number")
				agentID = 	req.get("result")["contexts"][1]["parameters"].get("agent-id")
				extra2="\nThere were not injured.\nThe police have been called.\nThe complain number: "+Ndenuncia+" taken by Agent "+agentID+", was properly loaded.\nThere were not street forniture demages."
				#prova="11.51 "+str(len(req.get("result")["contexts"][1]["parameters"]))+license+important+extra2
				prova=license+important+extra2
				res = makeWebhookResult(prova)
				return res
						#NO POLIZIA
			elif len(req.get("result")["contexts"][1]["parameters"]) == 0:
				extra1="\nThere were not injured.\nThe police have not been called.\nThere were not street forniture demages."
				prova1=license+important+extra1
				res = makeWebhookResult(prova1)
				return res
					#SI FERITI
		if req.get("result")["contexts"][0]["name"]=="posicion":
			licenseplate = 		req.get("result")["contexts"][4]["parameters"].get("number-sequence")
			dateloss = 		req.get("result")["contexts"][4]["parameters"].get("date")
			timeloss = 		req.get("result")["contexts"][4]["parameters"].get("time")
			cityloss = 		req.get("result")["contexts"][4]["parameters"].get("geo-city")
			name_other_driver = 	req.get("result")["contexts"][4]["parameters"].get("namedriver2")
			surname_other_driver = 	req.get("result")["contexts"][4]["parameters"].get("surnamedriver2")
			datedriver2 = 		req.get("result")["contexts"][4]["parameters"].get("date-otherdriver")
			driver2_license_number =req.get("result")["contexts"][4]["parameters"].get("license_driving")
			driver2_license_plate = req.get("result")["contexts"][4]["parameters"].get("license-plate")
			ass = 			req.get("result")["contexts"][4]["parameters"].get("assicurazione")
			
			name_injured = 		req.get("result")["contexts"][4]["parameters"].get("name-injiured")
			surname_injured = 	req.get("result")["contexts"][4]["parameters"].get("surname-injured")
			part_injured = 		req.get("result")["contexts"][4]["parameters"].get("injury-part")
			seat = 			req.get("result")["contexts"][4]["parameters"].get("seat-position")
			
			license = "Dear costumer, the claim of you car accident, with these details:\n-LICENSE PLATE NUMBER: "+licenseplate+"\n-DATE OF THE ACCIDENT: "+dateloss+"\n-TIME OF THE ACCIDENT: "+timeloss+"\n-PLACE OF THE ACCIDENT: "+cityloss+"\nhas been correct registered.\n\nPlease use claim no. 12345 for reference" 
			important="\n\n******** IMPORTANT ********\n\nThe schedule of the third part driver involved in the accident is:\n-NAME: "+name_other_driver+"\n-SURNAME: "+surname_other_driver+"\n-DATE OF BIRTH: "+datedriver2+"\n-LICENSE NUMBER: "+driver2_license_number+"\n-LICENSE PLATE NUMBER: "+driver2_license_plate+"\n-INSURANCE: "+ass
			#injured=" vediamo se funziona."
			injured="\n\n***** VERY IMPORTANT *****\n\nTHE PASSENGER: "+name_injured+" "+surname_injured+"; was injured in the "+part_injured+". "+name_injured+" found himself in "+seat+"."
			#speech=" posizione 0 e "+req.get("result")["contexts"][0]["name"]+"\nposizione 1 "+req.get("result")["contexts"][1]["name"]+"\nposizione 2 "+req.get("result")["contexts"][2]["name"]+"\nposizione 3 "#+req.get("result")["contexts"][3]["name"]+"\nposizione 4 "+req.get("result")["contexts"][4]["name"]
			#res = makeWebhookResult(speech)
			#return res
						#SI POLIZIA
			if len(req.get("result")["contexts"][0]["parameters"]) > 4:
				Ndenuncia = 	req.get("result")["contexts"][2]["parameters"].get("complain-number")
				agentID = 	req.get("result")["contexts"][2]["parameters"].get("agent-id")
				extra2="\nThe police have been called. The complain number: "+Ndenuncia+" taken by Agent "+agentID+", was properly loaded.\nThere were not street forniture demages."
				prova=license+important+injured+extra2
				res = makeWebhookResult(prova)
				return res
						#NO POLIZIA
			elif len(req.get("result")["contexts"][0]["parameters"]) == 4:
				extra1="\nThe police have not been called.\nThere were not street forniture demages."
				prova1=license+important+injured+extra1
				res = makeWebhookResult(prova1)
				return res
	
	if req.get("result").get("action") == "location.share":
		#url = "https://raw.githubusercontent.com/giacomo1989/prova-import/master/pizzaimport.json"
		#response = urllib.request.urlopen(url)
		#content = response.read()
		#data = json.loads(content.decode("utf8"))
		
		#lat = req.get("messagging")[0]["message"]["attachments"][0]["payload"]["coordinates"]["lat"]
		#lng = event.message.attachments[0].payload.coordinates.long
		
		#result = req.get("result")
		#parameters = result.get("parameters")
		speech="9.53 ok il collegamento e attivo "#+lat
		res = makeWebhookResult(speech)
		return res

	if req.get("result").get("action") == "yahooWeatherForecast":
		result 		= req.get("result")
		parameters 	= result.get("parameters")
		city 		= parameters.get("geo-city") 
		
		baseurl = "https://query.yahooapis.com/v1/public/yql?"
		yql_query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text= '"+ city+"')"
		yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
		result1 = urlopen(yql_url).read()
    		data = json.loads(result1)
		
		speech="10.21 le previsioni meteo a "+city+" saranno a dispozione a breve"
		res = makeWebhookResult(speech)
		return res
		
		'''
		baseurl = "https://query.yahooapis.com/v1/public/yql?"		
		yql_query = makeYqlQuery1(req)
    		yql_url = baseurl + urlencode({'q': yql_query}) + "&format=json"
    		result = urlopen(yql_url).read()
    		data = json.loads(result)
		
		speech="le previsioni meteo saranno a dispozione a breve"
		res = makeWebhookResult(speech)
		return res
	
	
		
	#if req.get("result").get("action") != "yahooWeatherForecast":
            	#return {}
	if req.get("result").get("action") == "yahooWeatherForecast":
	baseurl = "https://query.yahooapis.com/v1/public/yql?"		
	yql_query = makeYqlQuery1(req)
    	if yql_query is None:
        	return {}
    	yql_url = baseurl + urlencode({'q': yql_query}) + "&format=json"
    	result = urlopen(yql_url).read()
    	data = json.loads(result)
    	res1 = makeWebhookResult1(data)
    	
	speech="18.02 meteo prova"
	res = makeWebhookResult(speech)
		
	return res
	
			
def makeYqlQuery1(req):
    result = req.get("result")
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    if city is None:
        return None

    return "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='" + city + "')"

#yahooh weather forecast
def makeWebhookResult1(data):
    query = data.get('query')
    if query is None:
        return {}

    result = query.get('results')
    if result is None:
        return {}

    channel = result.get('channel')
    if channel is None:
        return {}

    item = channel.get('item')
    location = channel.get('location')
    units = channel.get('units')
    if (location is None) or (item is None) or (units is None):
        return {}

    condition = item.get('condition')
    if condition is None:
        return {}

    # print(json.dumps(item, indent=4))

    speech1 = "Today in " + location.get('city') + ": " + condition.get('text') + \
             ", the temperature is " + condition.get('temp') + " " + units.get('temperature')

    print("Response:")
    print(speech1)
    '''
#fine yahoo weather forecast
	
def makeWebhookResult(speech):
    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data":[],
        # "contextOut": [],
        "source": "prueba"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')




'''
CODICE CHE FUNZIONA PER L'APPLICAZIONE PIZZA.BCN IN API.AI

#!/usr/bin/env python

from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
import urllib.request, urllib.parse, urllib.error
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r



url = "https://raw.githubusercontent.com/giacomo1989/prova-import/master/pizzaimport.json"
response = urllib.request.urlopen(url)
content = response.read()
data = json.loads(content.decode("utf8"))


def processRequest(req):
	if req.get("result").get("action") == "Cost":
		result = req.get("result")
		parameters = result.get("parameters")
		pizza = parameters.get("type")
		valore = data.get("price").get(pizza)
		speech = "12.11 The price of pizza " +pizza+ " is "+valore+" euro. Bye Bye" 
		res = makeWebhookResult(speech)
		return res
		
	elif req.get("result").get("action") == "order.pizza":
		result = req.get("result")
		parameters = result.get("parameters")
		pizza = parameters.get("type")
		#tonno = parameters.get("fish")
		#cipolla = parameters.get("vegetables")
		#if tonno == "tonno" and cipolla == "cipolla" :
		speech = "10.22 perfect, your "+pizza+"it will be ready in 5 minuts. Bye Bye" 
		res = makeWebhookResult(speech)
		return res
		#else
		#	return {}
	
	elif req.get("result").get("action") == "adding":
		result = req.get("result")
		parameters = result.get("parameters")
		#tonno= parameters.get("fish")
		#aa=fish[0]
		#if aa == "tonno" :
		if parameters.get("type") == "margherita" :
			if parameters.get("fish") == "tonno" and parameters.get("vegetables") == "cipolla" :
				speech = "12.13 Perfect, you added these extra on your pizza "+parameters.get("type")+". your pizza tonno and cipolla will be ready in 5 minuts."
				res = makeWebhookResult(speech)
				return res
			elif parameters.get("vegetables") == "cipolla" and parameters.get("fish") == "tonno" :
				speech = "12.13 Perfect, you added these extra on your pizza "+parameters.get("type")+". your pizza tonno and cipolla will be ready in 5 minuts."
				res = makeWebhookResult(speech)
				return res
		
			else:
				return{}
		
		elif parameters.get("type") == "diavola" :
			if parameters.get("extra") != none : 
				speech = "11.32 Perfect, your pizza "+parameters.get("type")+" with this extra: "+parameters.get("extra")+", "+parameters.get("fish")+", "+parameters.get("cheese")+", "+parameters.get("vegetables")+", "+parameters.get("embutido")+" it will be ready in 5 minuts."
				res = makeWebhookResult(speech)
				return res
			else:
				return{}
		
		else:
			return{}
	
	else:
		return {}

def makeWebhookResult(speech):
    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data":[],
        # "contextOut": [],
        "source": "prueba"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
    '''
