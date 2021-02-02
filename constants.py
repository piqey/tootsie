# Basic constants
BASICS = {
    "CMD_PREFIX": "]",
    "FART_MAX": 8
}

# Prints
PRINTS = {
    # Define some stuff that only appear in the program window
    "READY": "yoooo {user} is in the house",
    "FOUND_GUILD": "{user} is connected to {guild} ({id})",

    # DM-related prints
    "DM_RECEIVED": "Received a DM from {author}, sending response...",
    "DM_REPLIED": "Sent a response to {author}'s DM.",

    # Fart-related prints
    "FART_FAILED": "Unable to rip ass; user is not in a voice channel.",
    "FART_PLAYED": "Finished deploying weapons in {channel}.",
    "FART_ERROR": "Unable to rip ass; error encountered: {error}",

    # General use prints
    "DISCONNECTING": "Disconnecting...",
    "DISCONNECTED": "Disconnected from {channel}."
}

# Messages
MESSAGES = {
    # Define some different messages that won't ever change
    "DM_RESPONSES": (
        "I don't know how to respond to this situation.",
        "My creator did not think this far ahead. Or did he?",
        "I'm a bot that makes fart noises, why are you messaging me?",
        "Are you looking for an easter egg or something?",
        "I hope you don't keep sending me these messages."
    ),
    "FART_AFFIRMATION": (
        "Your wish is my command, {user}.",
        "It will be done, my lord ({user}).",
        "Consider it done, {user}!",
        "Good thing you called, {user}, I just ate a ton of beans.",
        "Aye aye, captain ({user})!",
        "aight sounds good {user}",
        "tactical warhead inbound by order of {user}",
        "{user} you better prepare yourself for some extra smelly braps",
        "{user}, how can you make such a crappy request?"
    ),
    "FART_FAILED": "{user}, you have to be in a voice channel to do that!",
    "FART_TERRIBLE_PERSON": "You're a bigger piece of shit than I am. Denied."
}
