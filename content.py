from typing import Dict
from models import Scene, Choice


# ── YOUR PERSONAL MESSAGE ─────────────────────────────────────────────────────
# Edit this before you give her the app!
PERSONAL_MESSAGE = (
    "Write your message to Sern here."
)

COUPON = "Infinite kisses — redeemable any time, no expiry."
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