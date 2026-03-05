from flask import Blueprint, render_template, request, redirect, url_for, flash

main_bp = Blueprint("main", __name__)

def bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    if bmi <= 24.9:
        return "normal weight"
    if bmi <= 29.9:
        return "overweight"
    return "obese"

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/calculate", methods=["POST"])
def calculate():
    try:
        weight = float(request.form.get("weight", 0))
        feet = float(request.form.get("feet", 0))
        inches = float(request.form.get("inches", 0))
    except (TypeError, ValueError):
        flash("Please enter valid numbers for weight and height.", "error")
        return redirect(url_for("main.index"))

    if weight <= 0:
        flash("Weight must be greater than 0.", "error")
        return redirect(url_for("main.index"))

    height_inches = feet * 12 + inches
    if height_inches <= 0:
        flash("Height must be greater than 0.", "error")
        return redirect(url_for("main.index"))

    bmi = (weight / (height_inches ** 2)) * 703
    category = bmi_category(bmi)

    flash(f"Your BMI is {bmi:.1f} — {category}.", "success")
    return redirect(url_for("main.index"))
