from typing import Dict
from models import Scene, Choice


# ── YOUR PERSONAL MESSAGE ─────────────────────────────────────────────────────
# Edit this before you give her the app!
PERSONAL_MESSAGE = (
    "Dear Sern,\n\n"
    "Happy birthday! Although we are miles apart this day remains so special to me. "
    "I have missed you so much especially since you left for exchange but I'm always "
    "thinking about you hehe. The past 2 weeks in particular have been rough for me "
    "due to the passing of my grandpa etc. Thanks for checking in on me even when you "
    "were out and about. It means so much to me.\n\n"
    "I was especially touched by you celebrating my birthday hehe. The Thai food treat "
    "and of course buying the scooter for me.\n\n"
    "This website is my way of thanking you hehe. It contains small little inside jokes "
    "and some of my favorite photos of us 💓 and our friends.\n\n"
    "I did code this with some help from my trusty friend, Claude as my skills aren't "
    "too advanced yet. But I am thinking that as I improve and generate more ideas we "
    "can make this website into a little blog and a repository of our moments together.\n\n"
    "I love you so much Sern and I hope you love this website. It will be with you everywhere hehe.\n\n"
    "Most importantly I pray God will continue to watch over you and keep you safe hehe.\n\n"
    "This Bible verse makes me think of you and fills me with gratitude for having a "
    "loving and supportive partner like you hehe.\n\n"
    "Ecclesiastes 4:9-10\n"
    "Two are better than one: they earn a far greater reward for their toil.\n"
    "And if one should fall, his companion will help him up.\n\n"
    "Have a great birthday Sern and always remember that I love you so much 🥰\n\n"
    "Love,\nDavid"
)

COUPON = "Infinite kisses — redeemable any time, no expiry hehe"
# ─────────────────────────────────────────────────────────────────────────────


def build_scenes(gf_name: str) -> Dict[str, Scene]:
    PTS = "bubba_points"

    return {
        "start": Scene(
            id="start",
            title=f"Happy Birthday, {gf_name}",
            text=(
                f"Hey Sern!\n\n"
                "I know you're far away in Eindhoven right now, "
                "but I made you this little game so you know I'm thinking of you.\n\n"
                "Pick a path and let's go."
            ),
            a=Choice(
                label="Sweet route",
                next_id="sweet1",
                gives={PTS: 1},
                message="+ 1 Bubba point.",
            ),
            b=Choice(
                label="Playful route",
                next_id="play1",
                gives={PTS: 1},
                message="+ 1 Bubba point.",
            ),
        ),

        "sweet1": Scene(
            id="sweet1",
            title="Sweet Route",
            text="Pick your ideal morning:",
            a=Choice(
                label="Greek yoghurt and figs at home",
                next_id="hub",
                gives={PTS: 1},
                message="+ 1 Bubba point. Good taste.",
            ),
            b=Choice(
                label="Slow walk somewhere green",
                next_id="hub",
                gives={PTS: 1},
                message="+ 1 Bubba point. Love that for you.",
            ),
        ),

        "play1": Scene(
            id="play1",
            title="Playful Route",
            text="Pick your travel snack:",
            a=Choice(
                label="Figs",
                next_id="hub",
                gives={PTS: 1, "figs": 1},
                message="+ 1 Bubba point. Fig token collected.",
            ),
            b=Choice(
                label="Greek yoghurt",
                next_id="hub",
                gives={PTS: 1, "yoghurt": 1},
                message="+ 1 Bubba point. Yoghurt token collected.",
            ),
        ),

        "hub": Scene(
            id="hub",
            title="Checkpoint",
            text=(
                "You need 3 Bubba points to unlock the surprise.\n\n"
                "Check the sidebar to see how many you have."
            ),
            a=Choice(
                label="Pick a place we should go next",
                next_id="places_scene",
                gives={PTS: 1},
                message="+ 1 Bubba point.",
            ),
            b=Choice(
                label="Pick a treat",
                next_id="treat_scene",
                gives={PTS: 1},
                message="+ 1 Bubba point.",
            ),
        ),

        "places_scene": Scene(
            id="places_scene",
            title="Next on the list",
            text="Where should we go when you're back?",
            a=Choice(
                label="Gardens by the Bay, again",
                next_id="final_gate",
                gives={PTS: 1},
                message="+ 1 Bubba point. Classic choice.",
            ),
            b=Choice(
                label="Somewhere new",
                next_id="final_gate",
                gives={PTS: 1},
                message="+ 1 Bubba point. Adventure awaits.",
            ),
        ),

        "treat_scene": Scene(
            id="treat_scene",
            title="Pick a treat",
            text="What are you in the mood for?",
            a=Choice(
                label="Something sweet",
                next_id="final_gate",
                gives={"sweet": 1},
                message="Sweet token added.",
            ),
            b=Choice(
                label="Something savoury",
                next_id="final_gate",
                gives={"savoury": 1},
                message="Savoury token added.",
            ),
        ),

        "final_gate": Scene(
            id="final_gate",
            title="Almost there",
            text=(
                "You need 3 Bubba points to unlock the surprise.\n\n"
                "If you're not there yet, go back and explore another path."
            ),
            a=Choice(
                label="Unlock the surprise",
                next_id="final",
                requires={PTS: 3},
                message="Unlocked hehehe!",
            ),
            b=Choice(
                label="Go back",
                next_id="hub",
                message="No worries — grab some more points first.",
            ),
        ),

        "final": Scene(
            id="final",
            title=f"Happy Birthday, {gf_name}",
            text=f"{PERSONAL_MESSAGE}\n\n———\n{COUPON}",
            a=Choice(label="Play again", next_id="start"),
            b=Choice(label="Restart", next_id="start"),
        ),
    }
