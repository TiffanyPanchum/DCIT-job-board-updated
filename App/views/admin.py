from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, url_for, flash
from App.models import db
# from App.controllers import create_user

from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies

from .index import index_views


from App.controllers import(
    get_user_by_username,
    get_all_listings,
    get_company_listings,
    add_listing,
    add_categories,
    get_listing,
    delete_listing
)

from App.models import(
    Alumni,
    Company,
    Admin
)

admin_views = Blueprint('admin_views', __name__, template_folder='../templates')

# handle publish
@admin_views.route('/publish_job/<int:job_id>', methods=['POST'])
@jwt_required()
def publish_job(job_id):
    try:
        job = get_listing(job_id)  # Fetch the job by ID
        if job:
            job.isApproved = True  # Set the job as approved
            db.session.commit()  # Commit the change to the database
            flash('Job published successfully!', 'success')
        else:
            flash('Job not found', 'unsuccessful')
    except Exception as e:
        flash('Error publishing the job: ' + str(e), 'unsuccessful')
        db.session.rollback()

    return redirect(url_for('index_views.index_page'))

# handle unpublish
@admin_views.route('/unpublish_job/<int:job_id>', methods=['POST'])
@jwt_required()
def unpublish_job(job_id):
    try:
        job = get_listing(job_id)  # Fetch the job by ID
        if job:
            job.isApproved = False  # Set the job as unpublished (i.e., not approved)
            db.session.commit()  # Commit the change to the database
            flash('Job unpublished successfully!', 'success')
        else:
            flash('Job not found', 'unsuccessful')
    except Exception as e:
        flash('Error unpublishing the job: ' + str(e), 'unsuccessful')
        db.session.rollback()

    return redirect(url_for('index_views.index_page'))  # Redirect to the admin dashboard

# handle deletion
@admin_views.route('/delete_listing/<int:job_id>', methods=['GET'])
@jwt_required()
def delete_listing_action(job_id):

    deleted = delete_listing(job_id)

    response = None

    if deleted:
        flash('Job listing deleted!', 'success')
        response = redirect(url_for('index_views.index_page'))
    else:
        flash('Error deleting job listing', 'unsuccessful')
        response = (redirect(url_for('index_views.login_page')))

    return response


# @index_views.route('/delete-exercise/<int:exercise_id>', methods=['GET'])
# @login_required
# def delete_exercise_action(exercise_id):
    
#     user = current_user

#     res = delete_exerciseSet(exercise_id)

#     if res == None:
#         flash('Invalid or unauthorized')
#     else:
#         flash('exercise deleted!')
#     return redirect(url_for('user_views.userInfo_page'))


# handle updates