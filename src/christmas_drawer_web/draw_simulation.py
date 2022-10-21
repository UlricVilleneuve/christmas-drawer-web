import random
import typing
from src.christmas_drawer_web.models.participant import Participant


def simulate_draw(participants: typing.List[Participant]):
    not_drawn_yet = participants.copy()
    already_drawn = []

    success = True
    for participant in participants:
        pick_ok = False
        chosen_pick_index = -1
        counter = 0
        while not pick_ok:
            random_index = random.randint(0, len(not_drawn_yet)-1)
            # reset bool
            pick_ok = True
            for group in participant.in_groups:
                if group in not_drawn_yet[random_index].in_groups:
                    # participant is in same group as the pick
                    pick_ok = False

            chosen_pick_index = random_index
            counter += 1
            if counter > 250:
                success = False
                break

        participant.pick = not_drawn_yet[chosen_pick_index]
        already_drawn.append(participant.pick)
        not_drawn_yet.remove(participant.pick)
    return success
