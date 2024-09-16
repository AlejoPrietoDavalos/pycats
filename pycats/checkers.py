from datetime import datetime, date, timedelta, UTC

from pycats.cat import Cat


def when_need_anti_parasitic(*, cat: Cat) -> date:
    """ Según el veterinario, se debe dar cada 4 o 5 meses."""
    if len(cat.anti_parasitic) == 0:
        raise ValueError("No hay fecha de antiparasitario.")
    MONTH_4 = 4 * 28
    return cat.anti_parasitic[-1].date + timedelta(days=MONTH_4)

def need_anti_parasitic(*, cat: Cat, ) -> bool:
    date_now = datetime.now(tz=UTC).date() # FIXME: Poner que haga el chequeo con esto.
    return
