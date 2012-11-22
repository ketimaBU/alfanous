# Create your views here.


from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

from django.utils import translation
from django.utils.translation import ugettext as _
from django.utils.translation import ungettext
from django.utils.translation import pgettext_lazy # for ambiguities
from django.utils.translation import get_language_info


import json
from sys import path
path.append( "alfanous.egg/alfanous" )

from alfanous.Outputs import Raw

RAWoutput = Raw() #use default paths

def jos2(request):
    """ JSON Output System II """

    if len( request.GET ): 
        response_data = RAWoutput.do( request.GET )
        response =  HttpResponse(json.dumps(response_data), mimetype="application/json")
        response['charset'] = 'utf-8'
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET'
        
    else:
        response_data = RAWoutput._information["json_output_system_note"]
        response = HttpResponse(response_data)
        
    return response 
    



def results(request):

    response = RAWoutput.do( request.GET )

    # language information
    language = translation.get_language_from_request(request)
    language_info = get_language_info(language)

    #print  language ,language_info['name'], language_info['name_local'], language_info['bidi']
     

    translation.activate(language)
    request.LANGUAGE_CODE = translation.get_language()
    

    return render_to_response('wui.html', {"bidi": "rtl" if language_info['bidi'] else "ltr","language_local_name": language_info['name_local']})
