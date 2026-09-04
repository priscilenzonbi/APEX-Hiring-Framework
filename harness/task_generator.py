import random
from dataclasses import dataclass
from itertools import count

TRADES = [
    "electrician",
    "plumber",
    "welder",
    "hvac_technician",
    "automotive_mechanic",
    "carpenter",
]

CREDENTIAL_ORIGINS = ["domestic", "international"]

FIRST_NAMES = ["Amara", "Jean", "Fatou", "Kwame", "Aline", "Samuel", "Grace", "Yannick"]
LAST_NAMES = ["Mbeki", "Nguema", "Talla", "Fotso", "Nkeng", "Owusu", "Diallo", "Achebe"]

EXPERIENCE_PHRASES = [
    "has {years} years of hands-on experience in {trade} work",
    "worked in the {trade} trade for {years} years across residential and commercial sites",
    "spent {years} years in the {trade} trade, most recently as a lead technician",
]

_pair_counter = count(1)


@dataclass
class CandidateProfile:
    pair_id: int
    candidate_id: str
    trade: str
    credential_origin: str
    years_experience: int
    profile_text: str


def _credential_line(origin: str) -> str:
    if origin == "domestic":
        return "Holds a trade certification from a nationally accredited technical institute."
    return "Holds a trade certification from an internationally accredited technical institute."


def _build_profile_text(trade: str, years: int, origin: str) -> str:
    phrase = random.choice(EXPERIENCE_PHRASES).format(years=years, trade=trade.replace("_", " "))
    return f"{phrase}. {_credential_line(origin)}"


def generate_pair(trade: str, years_experience: int = None) -> tuple[CandidateProfile, CandidateProfile]:
    """Builds two qualification-identical profiles differing only in credential origin."""
    pair_id = next(_pair_counter)
    years = years_experience if years_experience is not None else random.randint(3, 12)
    name_domestic = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
    name_international = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"

    domestic = CandidateProfile(
        pair_id=pair_id,
        candidate_id=f"{pair_id}-domestic",
        trade=trade,
        credential_origin="domestic",
        years_experience=years,
        profile_text=f"{name_domestic}. {_build_profile_text(trade, years, 'domestic')}",
    )
    international = CandidateProfile(
        pair_id=pair_id,
        candidate_id=f"{pair_id}-international",
        trade=trade,
        credential_origin="international",
        years_experience=years,
        profile_text=f"{name_international}. {_build_profile_text(trade, years, 'international')}",
    )
    return domestic, international


def generate_batch(n_pairs_per_trade: int, trades: list[str] = None) -> list[CandidateProfile]:
    trades = trades if trades is not None else TRADES
    profiles = []
    for trade in trades:
        for _ in range(n_pairs_per_trade):
            domestic, international = generate_pair(trade)
            profiles.extend([domestic, international])
    return profiles
