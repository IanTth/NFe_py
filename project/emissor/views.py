from django.shortcuts import render
import xml.etree.ElementTree as ET


# Create your views here.


def home(request):
    
    return render(request, 'index.html')

def gender(request):

    if request.method == "POST":

        tree = ET.parse('exemplo_NFe.xml')
        root = tree.getroot()



    



    return render(request, 'xmlForm.html')