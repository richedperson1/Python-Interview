from flask import Blueprint,Response
from orm import folder_info
from test import addingFolder
simple_page = Blueprint('simple_page', __name__,url_prefix = "/blue")

@simple_page.route('page')
def show():
    # try:
        # folder_name,email_id
        return Response(addingFolder("hrfiles5","rutijaldjfs5",simple_page),mimetype="text/even-stream")
    # except Exception as e:
    #     return(f"Not founds , {e}" )