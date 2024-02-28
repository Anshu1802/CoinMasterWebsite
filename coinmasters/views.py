from django.shortcuts import render,redirect
import requests





def function(request):
    api_url = 'https://applicationsjson.s3.amazonaws.com/coin_master/spinlink_coinmaster.json'
    response = requests.get(api_url).json()
    first_data = response[0]['data']
    context = {'apidata': first_data,'date':response}
    return render(request,'index.html',context)


def click(request,id):
    api_url = 'https://applicationsjson.s3.amazonaws.com/coin_master/spinlink_coinmaster.json'
    response = requests.get(api_url).json()
    for ansh in response:
        if (str(ansh['id'])==str(id)):
            temp=ansh['data']
    context={'data':temp,'date':response}
    return render(request,'file.html',context)





    

