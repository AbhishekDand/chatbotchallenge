import json
import requests

def lambda_handler(event, context):
    # TODO implement
    country= event['currentIntent']['slots']['country']
    url = "https://covid-19-data.p.rapidapi.com/country"
    querystring = {"format":"json","name":country}
    headers = {
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
            'x-rapidapi-key': "d65751bc29msh5c7831c10864e7ap10a499jsn6ff1bfc248e2"
            }
    response = requests.request("GET", url, headers=headers, params=querystring)

    obj=response.json()
    
    line=str(obj[0]["country"])+"\n Confirmed:"+str(obj[0]["confirmed"])+"\n Recovered:"+str(obj[0]["recovered"])+"\n Deaths:"+str(obj[0]["deaths"])
        
    print(line)
        
       
    #print(response.text)
    fulfillmentText=line
    response={
        "dialogAction":{
            "type":"Close",
            "fulfillmentState":"Fulfilled",
            "message":{
                "contentType":"SSML",
                "content":line
                
            },
        }
    }
    return response
