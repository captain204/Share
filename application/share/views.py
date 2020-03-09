from flask import (Blueprint,flash, render_template, url_for, redirect)


snapss = Blueprint('snaps', __name__)



@snaps.route('/listings', methods=['GET'])
def listings():
    return "Hello"