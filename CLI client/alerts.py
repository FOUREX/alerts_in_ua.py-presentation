from os import getenv, system, name as os_name
from datetime import datetime
from time import sleep

from argparse import ArgumentParser
from dotenv import load_dotenv
from prettytable import PrettyTable
from alerts_in_ua.alerts_client import AlertsClient
from alerts_in_ua.locations import Locations


if os_name == "nt":
    CLEAR_COMMAND = "cls"
else:
    CLEAR_COMMAND = "clear"

load_dotenv("../.env")


alerts_client = AlertsClient(getenv("ALERTS_CLIENT_TOKEN"))


def format_alert(locations: Locations, _format: list[str]) -> PrettyTable:
    table = PrettyTable()
    table.align = "l"
    table.field_names = _format

    for location in locations:
        table.add_row([getattr(location, attr) for attr in _format])

    return table


def show_once(_format: list[str]):
    locations = alerts_client.get_active()
    print(format_alert(locations, _format))


def monitor(frequency: int, _format: list[str]):
    while True:
        system(CLEAR_COMMAND)

        print(f"Оновлення кожні {60 // frequency} секунд. Оновлено {datetime.now().strftime('%H:%M:%S')}\n")
        show_once(_format)

        sleep(60 / frequency)


def main():
    parser = ArgumentParser(
        prog='CLI alerts client',
        description='Консольний клієнт бібліотеки alerts-in-ua.py',
        usage="py {} [options]".format(__file__.split('\\')[-1]),
        epilog='Yep!',
    )

    parser.add_argument(
        "mode", nargs="?", default="default",
        help="Режими роботи: default - одноразове відображення, monitor - автооновлення даних"
    )

    parser.add_argument(
        "-freq", "--frequency", nargs="?", type=int, default=3,
        help="Частота оновлення даних на хвилину (режим монітора)"
    )

    parser.add_argument(
        "-f", "--format", nargs="*", default=["started_at", "alert_type", "location_title"],
        help="Атрибути локацій які будуть відображені"
    )

    args = parser.parse_args()

    match args.mode:
        case "monitor":
            monitor(args.frequency, args.format)
        case "default":
            show_once(args.format)
        case _:
            print("Не вірний режим відображення")


if __name__ == "__main__":
    main()
