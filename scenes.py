SCENES = {
    "wake_up": {
        "description": "You discover a mysterious prehistoric book in an abandoned library.",
        "actions": {
            "read_book": "portal",
            "ignore_book": "game_over"
        }
    },

    "portal": {
        "description": "A glowing portal opens before you.",
        "actions": {
            "enter_portal": "mesozoic_forest",
            "run_away": "game_over"
        }
    },

    "mesozoic_forest": {
        "description": "You arrive in a prehistoric jungle filled with giant ferns.",
        "actions": {
            "explore": "raptors",
            "climb_tree": "trex"
        }
    },

    "raptors": {
        "description": "A pack of velociraptors emerges from the bushes.",
        "actions": {
            "hide": "river",
            "run": "lost_in_time"
        }
    },

    "trex": {
        "description": "A T-Rex roars in the distance.",
        "actions": {
            "escape": "river",
            "observe": "river"
        }
    },

    "river": {
        "description": "You reach a dangerous river.",
        "actions": {
            "cross": "volcano",
            "follow": "volcano"
        }
    },

    "volcano": {
        "description": "A volcano begins erupting.",
        "actions": {
            "escape_portal": "return_home",
            "search_treasure": "prehistoric_legend"
        }
    },

    "return_home": {
        "description": "You return safely to modern times.",
        "actions": {}
    },

    "prehistoric_legend": {
        "description": "You uncover ancient treasure and become a legend.",
        "actions": {}
    },

    "lost_in_time": {
        "description": "You are trapped in the prehistoric world forever.",
        "actions": {}
    }
}