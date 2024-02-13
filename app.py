from flask import Flask, render_template_string, request;
from pathlib import Path;
from dominate.tags import *;
import dominate, json, os;
from mail import send_form_email;
from dotenv import load_dotenv;

app = Flask(__name__)
version = "waiver v0.1-alpha"


load_dotenv();

@app.route("/<formname>/submit", methods = ["POST"])
def submit(formname):
    json_file = json.loads(Path("./forms/" + formname + ".json").read_text());
    doc = dominate.document(title=formname + " submission");

    content=f"Response for form \"{json_file["name"]}\":\n\n";
    for question in json_file["questions"]:
        content += (question["question"] + ":\n\n\t" + request.form[question["id"]] + "\n\n");

    send_form_email(sender=os.getenv("BOT_ADDRESS"),
                    recipient=os.getenv("RECIPIENT_ADDRESS"),
                    server=os.getenv("EMAIL_SERVER"),
                    sender_password=os.getenv("BOT_PASSWORD"),
                    content=content);

    with doc.head:
        link(rel="stylesheet", href="{{url_for('static', filename='style.css')}}");

    with doc:
        p(f"thank you for your submission of {json_file["name"]}!")

    return render_template_string(doc.render());


@app.route("/<formname>")
def index(formname):
    json_file = json.loads(Path("./forms/" + formname + ".json").read_text());
    doc = dominate.document(title=formname);

    with doc.head:
        link(rel="stylesheet", href="{{url_for('static', filename='style.css')}}");

    with doc:
        with div():
            attr(id="header");

            h1(json_file["name"]);
            p(json_file["description"]);


        with div():
            attr(id="body");

            with form(enctype="multipart/form-data", method="post", action="/" + formname + "/submit"):
                for question in json_file["questions"]:
                    with label(fr=question["id"]):
                        p(question["question"]);
                    if question["type"] == "text":
                        input_(id=question["id"], type="text", name=question["id"]);
                    br();
                    br();
                br();
                input_(type="submit", value="Submit");

        with div():
            attr(id="watermark");

            small(p(f"made with waiver ({version})"));

    return render_template_string(doc.render());


