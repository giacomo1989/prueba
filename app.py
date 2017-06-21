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
		danni=			req.get("result")["contexts"][0]["parameters"].get("forniture-demage")
		danni_strada = 		parameters.get("forniture-demage")
		
		
		#speech = " esempio se funziona webhook. danni strada: "+context+" 11.47 vediamo se l'array funziona "+danni+" altro valore relativo al nome del contexto "+req.get("result")["contexts"][0]["name"]
		#req.get("result")["contexts"][0]["name"] stringa funzionante
		
		license = "Dear costumer, the claim of you car accident, with these details:\n-LICENSE PLATE NUMBER: "+licenseplate+"\n-DATE OF THE ACCIDENT: "+dateloss+"\n-TIME OF THE ACCIDENT: "+timeloss+"\n-PLACE OF THE ACCIDENT: "+cityloss+"\nhas been correct registered.\n\nPlease use claim no. 12345 for reference" 
		important="\n\n******** IMPORTANT ********\n\nThe schedule of the third part driver involved in the accident is:\n-NAME: "+name_other_driver+"\n-SURNAME: "+surname_other_driver+"\n-DATE OF BIRTH: "+datedriver2+"\n-LICENSE NUMBER: "+driver2_license_number+"\n-LICENSE PLATE NUMBER: "+driver2_license_plate+"\n-INSURANCE: "+ass
		# funziona posizione=" posizione 0 e "+req.get("result")["contexts"][0]["name"]+"\nposizione 1 "+req.get("result")["contexts"][1]["name"]+ "posizione 2 "+req.get("result")["contexts"][2]["name"]+" facciamo prova e vediamo se alcuni dati inseriti vanno bene "+name_other_driver+" "+surname_other_driver+" "+cityloss
		extra="\nThere were not injured.\nThe police have not been called\nThere were street forniture demages:\n-"+danni_strada
		prova=license+important+extra
		res = makeWebhookResult(prova)
		return res
	
	if req.get("result").get("action") == "forniture-demage.forniture-demage-no":
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
		#Ndenuncia = 		req.get("result")["contexts"][1]["parameters"].get("complain-number")
		#agentID = 		req.get("result")["contexts"][1]["parameters"].get("agent-id")
		license = "Dear costumer, the claim of you car accident, with these details:\n-LICENSE PLATE NUMBER: "+licenseplate+"\n-DATE OF THE ACCIDENT: "+dateloss+"\n-TIME OF THE ACCIDENT: "+timeloss+"\n-PLACE OF THE ACCIDENT: "+cityloss+"\nhas been correct registered.\n\nPlease use claim no. 12345 for reference" 
		important="\n\n******** IMPORTANT ********\n\nThe schedule of the third part driver involved in the accident is:\n-NAME: "+name_other_driver+"\n-SURNAME: "+surname_other_driver+"\n-DATE OF BIRTH: "+datedriver2+"\n-LICENSE NUMBER: "+driver2_license_number+"\n-LICENSE PLATE NUMBER: "+driver2_license_plate+"\n-INSURANCE: "+ass
		#extra1="\nThere were not injured.\nThe police have not been called\nThere were not street forniture demages."
		#extra2="\nThere were not injured.\nThe police have been called. The complain "+Ndenuncia+" by Agent "+agentID+" was properly loaded\nThere were not street forniture demages."
		#prova=license+important+extra2
		#res = makeWebhookResult(prova)
		#return res
		
		if len(req.get("result")["contexts"][2]["parameters"]) != 0:
			Ndenuncia = 	req.get("result")["contexts"][1]["parameters"].get("complain-number")
			agentID = 	req.get("result")["contexts"][1]["parameters"].get("agent-id")
			
			extra2="\nThere were not injured.\nThe police have been called. The complain "+Ndenuncia+" by Agent "+agentID+" was properly loaded\nThere were not street forniture demages."
			prova="19.32"+str(len(req.get("result")["contexts"][2]["parameters"]))+license+important+extra2
			res = makeWebhookResult(prova)
			return res
		
		elif len(req.get("result")["contexts"][2]["parameters"]) == 0:
			extra1="\nThere were not injured.\nThe police have not been called\nThere were not street forniture demages."
			prova1="19.25"+license+important+extra1
			res = makeWebhookResult(prova1)
			return res
			
			
	'''
	if req.get("result").get("action") == "forniture-demage.forniture-demage-yes" and req["contexts"][1]["name"]== "domanda1":
		result = req.get("contexts")
		datetime= result["contexts"][1]["date-time.original"]
		city= result["contexts"][1]["geo-city"]
		surname2= result["contexts"][1]["surnamedriver2"]
		name2= result["contexts"][1]["namedriver2"]
		datedriver2= result["contexts"][1]["date-otherdriver"]
		#danni= result["contexts"][1]["forniture-demage"][1]
		numeropoliza= result["contexts"][1]["number-sequence.original"]
		
		parameters = result.get("parameters")
		saluto = parameters.get("benvenuto")
		
		speech = " Dear costumer, your claim of your car accident: policy number "+numeropoliza+ "heppened on "+datetime+" in "+city+" has been correct registered. Please use claim no. 112233 for reference.There were not injured.The police have not been called and there were forniture demages: street lamp" 
		res = makeWebhookResult(speech)
		return res
	'''
	'''
	if req.get("result").get("action") == "claim.accident":
		result = req.get("result")
		parameters = result.get("parameters")
		datedriver2 = parameters.get("date-otherdriver")
		datetime = parameters.get("date-time")
		city = parameters.get("geo-city")
		name2 = parameters.get("namedriver2")
		numeropoliza = parameters.get("number-sequence")
		surname2 = parameters.get("surnamedriver2")
			if req.get("result").get("action") == "lesionados.lesionados-yes":
				result = req.get("result")
				parameters = result.get("parameters")
				nameinfortunato = parameters.get("name-injiured")
				surnameinfortunato = parameters.get("surname-injured")
				parteinfortunata = parameters.get("injury-part")
					if req.get("result").get("action") == "seat.position":
						result = req.get("result")
						parameters = result.get("parameters")
						posizione = parameters.get("seat-position")
							if req.get("result").get("action") == "police.police-yes":
								result = req.get("result")
								parameters = result.get("parameters")
								agenteID = parameters.get("agent-id")
								ndenuncia = parameters.get("complain-number")
									if req.get("result").get("action") == "forniture-demage.forniture-demage-yes":
										result = req.get("result")
										parameters = result.get("parameters")
										danni = parameters.get("forniture-demage")
										speech = " Dear costumer, your claim of your car accident: policy number "+numeropoliza+ "heppened on "+datetime+" in "+city+" has been correct registered.Please use claim no. 112233 for reference. IMPORTANT: "+nameinfortunato+" "+surnameinfortunato+" was injured the "+parteinfortunata+" in "+posizione+" . The complain number "+ndenuncia" taken by police agent number "+agenteID+" was properly loaded. There were forniture demages: "+danni  
										res = makeWebhookResult(speech)
										return res
									else
										speech = " Dear costumer, your claim of your car accident: policy number "+numeropoliza+ "heppened on "+datetime+" in "+city+" has been correct registered.Please use claim no. 112233 for reference. IMPORTANT: "+nameinfortunato+" "+surnameinfortunato+" was injured the "+parteinfortunata+" in "+posizione+" . The complain number "+ndenuncia" taken by police agent number "+agenteID+" was properly loaded. There were not forniture demages."
										res = makeWebhookResult(speech)
										return res
							else
								if req.get("result").get("action") == "forniture-demage.forniture-demage-yes":
										result = req.get("result")
										parameters = result.get("parameters")
										danni = parameters.get("forniture-demage")
										speech = " Dear costumer, your claim of your car accident: policy number "+numeropoliza+ "heppened on "+datetime+" in "+city+" has been correct registered. Please use claim no. 112233 for reference.. IMPORTANT: "+nameinfortunato+" "+surnameinfortunato+" was injured the "+parteinfortunata+" in "+posizione+" . The police have not been called. There were forniture demages: "+danni  
										res = makeWebhookResult(speech)
										return res
									else
										speech = " Dear costumer, your claim of your car accident: policy number "+numeropoliza+ "heppened on "+datetime+" in "+city+" has been correct registered. Please use claim no. 112233 for reference. IMPORTANT: "+nameinfortunato+" "+surnameinfortunato+" was injured the "+parteinfortunata+" in "+posizione+" . The police have not been called. There were not forniture demages."
										res = makeWebhookResult(speech)
										return res
					else
						return{}
			else
				if req.get("result").get("action") == "police.police-yes":
								result = req.get("result")
								parameters = result.get("parameters")
								agenteID = parameters.get("agent-id")
								ndenuncia = parameters.get("complain-number")
									if req.get("result").get("action") == "forniture-demage.forniture-demage-yes":
										result = req.get("result")
										parameters = result.get("parameters")
										danni = parameters.get("forniture-demage")
										speech = " Dear costumer, your claim of your car accident: policy number "+numeropoliza+ "heppened on "+datetime+" in "+city+" has been correct registered.Please use claim no. 112233 for reference. There were not injured. The complain number "+ndenuncia" taken by police agent number "+agenteID+" was properly loaded. There were forniture demages: "+danni  
										res = makeWebhookResult(speech)
										return res
									else
										speech = " Dear costumer, your claim of your car accident: policy number "+numeropoliza+ "heppened on "+datetime+" in "+city+" has been correct registered.Please use claim no. 112233 for reference. There were not injured. The complain number "+ndenuncia" taken by police agent number "+agenteID+" was properly loaded. There were not forniture demages."
										res = makeWebhookResult(speech)
										return res
							else
								if req.get("result").get("action") == "forniture-demage.forniture-demage-yes":
										result = req.get("result")
										parameters = result.get("parameters")
										danni = parameters.get("forniture-demage")
										speech = " Dear costumer, your claim of your car accident: policy number "+numeropoliza+ "heppened on "+datetime+" in "+city+" has been correct registered. Please use claim no. 112233 for reference. There were not injured. The police have not been called. There were forniture demages: "+danni  
										res = makeWebhookResult(speech)
										return res
									else
										speech = " Dear costumer, your claim of your car accident: policy number "+numeropoliza+ "heppened on "+datetime+" in "+city+" has been correct registered. Please use claim no. 112233 for reference. There were not injured. The police have not been called. There were not forniture demages."
										res = makeWebhookResult(speech)
										return res
	
	if req.get("result").get("action") == "claim.accident":
		result = req.get("result")
		parameters = result.get("parameters")
		
		
		licenseplate = parameters.get("number-sequence")
		dateloss = parameters.get("date")
		timeloss = parameters.get("time")
		cityloss = parameters.get("geo-city")
		name_other_driver = parameters.get("namedriver2")
		surname_other_driver = parameters.get("surnamedriver2")
		datedriver2 = parameters.get("date-otherdriver")
		driver2_license_number = parameters.get("license_driving")
		driver2_license_plate = parameters.get("license-plate")
		ass = parameters.get("assicurazione")
		#speech = "dati raccolti prima parte esempio: "+name_other_driver+" "+surname_other_driver
			if req.get("result").get("action") == "lesionados.lesionados-yes":
				result = req.get("result")
				parameters = result.get("parameters")
				nameinfortunato = parameters.get("name-injiured")
				surnameinfortunato = parameters.get("surname-injured")
				speech = " dati raccolti seconda parte es: "+nameinfortunato+" "+surnameinfortunato
				res = makeWebhookResult(speech)
				return res
	'''	

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
