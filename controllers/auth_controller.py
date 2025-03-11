from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from models.usuario import Usuario
from models.database import db
from werkzeug.security import check_password_hash

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = Usuario.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Inicio de sesión exitoso!", "success")
            return redirect(url_for("auth.admin_dashboard" if user.es_admin else "auth.user_dashboard"))
        else:
            flash("Usuario o contraseña incorrectos", "danger")
    return render_template("login.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Has cerrado sesión correctamente", "info")
    return redirect(url_for("auth.login"))

@auth.route("/admin_dashboard")
@login_required
def admin_dashboard():
    if not current_user.es_admin:
        return redirect(url_for("auth.user_dashboard"))
    return render_template("admin_dashboard.html", username=current_user.username)

@auth.route("/user_dashboard")
@login_required
def user_dashboard():
    return render_template("user_dashboard.html", username=current_user.username)