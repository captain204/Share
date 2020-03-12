from flask import (
    Blueprint,
    redirect,
    request,
    flash,
    url_for,
    render_template,session)

listing = Blueprint('listing', __name__, template_folder='templates')


from flask_login import (
    login_required,
    login_user,
    current_user,
    logout_user)


from application import db,login_manager

# Models
from application.listings.models import(
    Listings) 
from application.users.models import(
    User) 

from application.listings.forms import (
     ListingForm)




@listing.route('/add', methods=['GET','POST'])
@login_required
def add():
    """ Add new Listing"""
    form = ListingForm(request.form)
    if request.method == 'POST':
        if form.validate():
            name = request.form.get('name')
            address = request.form.get('address')
            user_id = current_user.id
            listing = Listings(name=name,address=address, user_id=user_id)
            db.session.add(listing)
            db.session.commit()
            flash('Listing added successfully')
            return redirect(url_for('listing.mylistings'))
        else:
            flash("Something went wrong while posting your listing")
            return redirect(url_for('listings.mylistings'))
    return render_template('listings/add_listings.html', form=form)


@listing.route('/mylistings', methods=['GET'])
@login_required
def mylistings():
    id = current_user.id
    #db.session.query(Post).filter(Post.title == 'Post 1').all()
    #user = User.query.filter_by(email=email).first()
    result = Listings.query.filter_by(user_id =id).all()
    return render_template('listings/listings.html', results = result)


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """ Redirect unauthorized users to Login page ."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('user.login'))

