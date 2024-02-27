from django.shortcuts import render,redirect
import requests





def function(request):
    api_url = 'https://applicationsjson.s3.amazonaws.com/coin_master/coin_master.json'
    response = requests.get(api_url).json()
    first_data = response[0]['data']
    # keys = [item['key'] for item in api_url]
    context = {'apidata': first_data,'date':response}
    return render(request,'index.html',context)


