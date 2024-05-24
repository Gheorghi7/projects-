from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)


@app.route('/')
def run_bs():
    return render_template("index.html")


@app.route('/about')
def run_about():
    return render_template(template_name_or_list='about.html')


@app.route('/contact')
def run_contact():
    return render_template(template_name_or_list='contact.html')


@app.route('/login', methods=['POST'])
def email():
    if request.method == 'POST':
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template('contact.html', mes=True)
    return render_template('contact.html', mes=False)


def send_email(name, email, phone_num, message):
    email_mess = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone_num}\nMessage:{message}"
    with smtplib.SMTP('smtp.gmail.com') as connect:
        connect.starttls()
        connect.login('valentina161012@gmail.com', '069614363')
        connect.sendmail('valentina161012@gmail.com', 'gogitacu@gmail.com', email_mess)


if __name__ == '__main__':
    app.run(debug=True)
