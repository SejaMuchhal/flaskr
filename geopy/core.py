from flask import Blueprint, request, Response
from .utils import get_geocode_response
from dicttoxml import dicttoxml

bp = Blueprint('core', __name__)

# Endpoint which returns latitude and longitude in the response for given address.
@bp.route('/getAddressDetails', methods=['POST'])
def get_address_details():
    output_format = request.json['output_format']
    address = request.json['address']
    geocode_response = get_geocode_response(address)
    
    if output_format == "xml":
        return Response(dicttoxml(geocode_response),mimetype='application/xml')
    else:
        return geocode_response