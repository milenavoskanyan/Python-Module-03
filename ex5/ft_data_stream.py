# next(), range(), len(), print(), import typing,
# typing.Generator, import random, random.*

import random
from typing import Generator

NAMES = ["bob", "alice", "dylan", "charlie"]
ACTIONS = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "release"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(NAMES), random.choice(ACTIONS))


def consume_event(events: list[tuple[str, str]]
                  ) -> Generator[tuple[str, str], None, None]:
    while events:
        ev_idx = random.randint(0, len(events) - 1)  # 1 or 0?
        event = events[ev_idx]
        del events[ev_idx]
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")

    gen = gen_event()
    for i in range(1000):
        name, action = next(gen)
        print(f"Event {i}: Player {name} did action {action}")

    events = []
    for _ in range(10):
        events += [next(gen)]
    print(f"Built list of 10 events: {events}")
    print()

    for del_ev in consume_event(events):
        print(f"Got event from list: {del_ev}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
