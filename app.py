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

def processRequest(req):
	
	if req.get("result").get("action") == "forniture-demage.forniture-demage-yes":
		result = req.get("result")
		parameters = result.get("parameters")
		
		
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
				
		if len(req.get("result")["contexts"][1]["parameters"]) > 2:
			Ndenuncia = 	req.get("result")["contexts"][1]["parameters"].get("complain-number")
			agentID = 	req.get("result")["contexts"][1]["parameters"].get("agent-id")
			
			extra2="\nThere were not injured.\nThe police have been called. The complain "+Ndenuncia+" by Agent "+agentID+" was properly loaded\nThere were street forniture demages:\n-"+danni
			prova="11.57 "+str(len(req.get("result")["contexts"][1]["parameters"]))+" "+license+important+extra2
			res = makeWebhookResult(prova)
			return res
		
		elif len(req.get("result")["contexts"][1]["parameters"]) == 2:
			extra1="\nThere were not injured.\nThe police have not been called\nThere were street forniture demages:\n-"+danni
			prova1=license+important+extra1
			res = makeWebhookResult(prova1)
			return res
	
	
	
	if req.get("result").get("action") == "forniture-demage.forniture-demage-no":
		result = req.get("result")
		parameters = result.get("parameters")
		
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

			if len(req.get("result")["contexts"][1]["parameters"]) != 0:
				Ndenuncia = 	req.get("result")["contexts"][1]["parameters"].get("complain-number")
				agentID = 	req.get("result")["contexts"][1]["parameters"].get("agent-id")
				extra2="\nThere were not injured.\nThe police have been called. The complain "+Ndenuncia+" by Agent "+agentID+" was properly loaded\nThere were not street forniture demages."
				prova="11.51 "+str(len(req.get("result")["contexts"][1]["parameters"]))+license+important+extra2
				res = makeWebhookResult(prova)
				return res

			elif len(req.get("result")["contexts"][1]["parameters"]) == 0:
				extra1="\nThere were not injured.\nThe police have not been called\nThere were not street forniture demages."
				prova1=license+important+extra1
				res = makeWebhookResult(prova1)
				return res
				
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
			
			name_injured = 		req.get("result")["contexts"][2]["parameters"].get("name-injiured")
			surname_injured = 	req.get("result")["contexts"][2]["parameters"].get("surname-injured")
			part_injured = 		req.get("result")["contexts"][2]["parameters"].get("injury-part")
			seat = 			req.get("result")["contexts"][2]["parameters"].get("seat-position")
			
			license = "Dear costumer, the claim of you car accident, with these details:\n-LICENSE PLATE NUMBER: "+licenseplate+"\n-DATE OF THE ACCIDENT: "+dateloss+"\n-TIME OF THE ACCIDENT: "+timeloss+"\n-PLACE OF THE ACCIDENT: "+cityloss+"\nhas been correct registered.\n\nPlease use claim no. 12345 for reference" 
			important="\n\n******** IMPORTANT ********\n\nThe schedule of the third part driver involved in the accident is:\n-NAME: "+name_other_driver+"\n-SURNAME: "+surname_other_driver+"\n-DATE OF BIRTH: "+datedriver2+"\n-LICENSE NUMBER: "+driver2_license_number+"\n-LICENSE PLATE NUMBER: "+driver2_license_plate+"\n-INSURANCE: "+ass
			#injured=" vediamo se funziona."
			injured="\n\n***** VERY IMPORTANT *****\n\nTHE PASSENGER:"#+name_injured+surname_injured+"; was injured in the "+part_injured+". "+name_injured+" found himself in "+seat prova
			#speech=" posizione 0 e "+req.get("result")["contexts"][0]["name"]+"\nposizione 1 "+req.get("result")["contexts"][1]["name"]+"\nposizione 2 "+req.get("result")["contexts"][2]["name"]+"\nposizione 3 "#+req.get("result")["contexts"][3]["name"]+"\nposizione 4 "+req.get("result")["contexts"][4]["name"]
			#res = makeWebhookResult(speech)
			#return res

			if len(req.get("result")["contexts"][0]["parameters"]) > 4:
				Ndenuncia = 	req.get("result")["contexts"][2]["parameters"].get("complain-number")
				agentID = 	req.get("result")["contexts"][2]["parameters"].get("agent-id")
				extra2="\nThe police have been called. The complain "+Ndenuncia+" by Agent "+agentID+" was properly loaded\nThere were not street forniture demages."
				prova="11.51 "+license+important+injured+extra2
				res = makeWebhookResult(prova)
				return res

			elif len(req.get("result")["contexts"][0]["parameters"]) == 4:
				extra1="\nThe police have not been called\nThere were not street forniture demages."
				prova1=license+important+injured+extra1
				res = makeWebhookResult(prova1)
				return res

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
