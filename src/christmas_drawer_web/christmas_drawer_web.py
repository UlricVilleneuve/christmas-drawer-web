import random
import typing
import string

from src.christmas_drawer_web.config import SECRET_KEY
from flask import Flask, render_template, redirect
from src.christmas_drawer_web.forms.token import TokenForm
from src.christmas_drawer_web.models.participant import Participant
from src.christmas_drawer_web.draw_simulation import simulate_draw

application = Flask(__name__)
application.secret_key = SECRET_KEY


def generate_random_token():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for _ in range(32))
    return result_str


group_marie_frank = 1
group_cath_ju = 2
group_maria_ulric = 3
group_manon_laval = 4
frank = Participant("Francois", [group_marie_frank])
marie = Participant("Marie-Claude", [group_marie_frank])
cath = Participant("Cath", [group_cath_ju])
ju = Participant("Julien", [group_cath_ju])
maria = Participant("Maria", [group_maria_ulric])
ulric = Participant("Ulric", [group_maria_ulric])
charles = Participant("Charles", [])
manon = Participant("Manon", [group_manon_laval])
laval = Participant("Laval", [group_manon_laval])
participants = [frank, marie, cath, ju, maria, ulric, charles, manon, laval]

tokens_to_participant: typing.Dict[str, Participant]
tokens_to_participant = {
    generate_random_token(): frank,
    generate_random_token(): marie,
    generate_random_token(): cath,
    generate_random_token(): ju,
    generate_random_token(): maria,
    generate_random_token(): ulric,
    generate_random_token(): charles,
    generate_random_token(): manon,
    generate_random_token(): laval
}

for token, participant in tokens_to_participant.items():
    print(f'{participant.name}:{token}')

if not simulate_draw(participants):
    raise RuntimeError(f'After 250 attempts, could not find a solution {participants}')


@application.route('/', methods=["GET"])
def index():
    return redirect("/home", code=302)


@application.route('/home', methods=["GET", "POST"])
def home():
    token_form = TokenForm()
    if token_form.validate_on_submit():
        token_entered = token_form.token.data
        print(f'{token_entered} token was entered')
        return redirect(f"/token/{token_entered}", code=302)
    if token_form.errors:
        print(f'Form errors {token_form.errors}')
        raise Exception(f'Received the following errors when submitting home form: {token_form.errors}')
    return render_template("home.html", form=token_form)


@application.route('/token/<token>', methods=["GET"])
def token1(token):
    return render_template("result.html", participant_name=tokens_to_participant[token].name, result_name=tokens_to_participant[token].pick.name)


if __name__ == '__main__':
    print('running main')
    application.run()
