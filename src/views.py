from flask import render_template, abort, flash, redirect, url_for, request
from models import courses, videos, contact_info

def index():
    return render_template('index.html', courses=courses)

def course(course_id):
    try:
        course = courses[int(course_id) - 1]
    except (IndexError, ValueError):
        abort(404)
    return render_template('course.html', course=course)

def videos_page():
    return render_template('videos.html', videos=videos)

def contact():
    if request.method == "POST":
        title = request.form.get("message_title", "").strip()
        body = request.form.get("message_body", "").strip()
        print(f"[mock email] To: {contact_info['email']} | Title: {title} | Body: {body}")
        flash("Your message has been sent! We'll be in touch soon.", "success")
        return redirect(url_for("contact"))
    return render_template('contact.html', contact=contact_info)