from django.shortcuts import render
import requests
import json

import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "d35126556bmshcbe6b5d865906e5p1770cdjsn41db5346d2f1",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

print(response)


# Create your views here.
def helloworldview(request):
	mylist=[]
	noofresults=int(response['results'])

	for x in range(0,noofresults):

		mylist.append(response['response'][x]['country'])

	if request.method=="POST":
		selectedcountry=request.POST['selectedcountry']

		for x in range(0,noofresults):
			if selectedcountry==response['response'][x]['country']:
				new=response['response'][x]['cases']['new']
				active=response['response'][x]['cases']['active']
				critical=response['response'][x]['cases']['critical']
				recovered=response['response'][x]['cases']['recovered']
				total=response['response'][x]['cases']['total']
				deaths=int(total)-int(active)-int(recovered)

		context={'selectedcountry':selectedcountry,'mylist':mylist,'new':new,'active':active,'critical':critical,'recovered':recovered,'deaths':deaths,'total':total}
		return render(request,'helloworld.html',context)

	context={'mylist':mylist}
	return render(request,'helloworld.html',context)
