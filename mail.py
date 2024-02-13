
import smtplib, ssl;

def send_form_email(sender, recipient, server, sender_password, content,server_port=465):
    port = server_port;
    password = sender_password;
    context = ssl.create_default_context();

    with smtplib.SMTP_SSL(server, server_port, context=context) as server_:
        server_.login(sender, password);
        server_.sendmail(sender, recipient, f"""\
Subject: automatic response
From: "{server} bot" <{sender}>

{content}

""");

