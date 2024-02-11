from os import getenv, system, mkdir, remove, listdir, name as os_name
from os.path import isdir
from datetime import datetime
from time import sleep
from io import BytesIO

from dotenv import load_dotenv
from argparse import ArgumentParser
from prettytable import PrettyTable

from alerts_in_ua.alerts_client import AlertsClient
from alerts_in_ua.locations import Locations
from alerts_in_ua.map_style import MapStyle

if os_name == "nt":
    CLEAR_COMMAND = "cls"
    OPEN_IMAGE_COMMAND = "start"
else:
    CLEAR_COMMAND = "clear"
    OPEN_IMAGE_COMMAND = "xdg-open"

load_dotenv("../.env")

alerts_client = AlertsClient(getenv("ALERTS_CLIENT_TOKEN"))


def check_dir(dir_name: str):
    if dir_name not in listdir():
        mkdir(dir_name)
    elif not isdir(dir_name):
        remove(dir_name)
        mkdir(dir_name)


def format_alert(locations: Locations, _format: list[str]) -> PrettyTable:
    table = PrettyTable()
    table.align = "l"
    table.field_names = _format

    for location in locations:
        table.add_row([getattr(location, attr) for attr in _format])

    return table


def save_image_as_png(image: BytesIO, image_name: str = "None", *, path: str = "."):
    check_dir("saves")

    with open(rf"{path}\{image_name}.png", "wb") as file:
        file.write(image.getvalue())


def show_image(image: BytesIO):
    check_dir("temp")

    image_path = fr"temp\alerts.png"
    save_image_as_png(image, "alerts", path="temp")

    system(f"{OPEN_IMAGE_COMMAND} {image_path}")


def show_once(_format: list[str], do_save_image: bool, do_show_image: bool):
    locations = alerts_client.get_active(force=True)
    print(format_alert(locations, _format))

    image_name = datetime.strptime(locations.last_updated_at, "%Y/%m/%d %H:%M:%S %z").strftime("%Y-%m-%d %H.%M.%S")
    locations_map = locations.render_map(MapStyle(dpi=90))

    if do_save_image:
        save_image_as_png(locations_map, image_name, path="saves")

    if do_show_image:
        show_image(locations_map)


def monitor(frequency: int, _format: list[str], do_save_image: bool):
    while True:
        system(CLEAR_COMMAND)

        print(f"Оновлення кожні {60 // frequency} секунд. Оновлено {datetime.now().strftime('%H:%M:%S')}\n")
        show_once(_format, do_save_image, False)

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
        "--show-image", action="store_true",
        help="Відображення мапи тривог (не працює в режимі монітора)"
    )

    parser.add_argument(
        "--save-image", action="store_true",
        help=r"Зберігання мапи тривог як зображення в директорію .\saves"
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
            monitor(args.frequency, args.format, args.save_image)
        case "default":
            show_once(args.format, args.save_image, args.show_image)
        case "show":
            show_once(args.format, args.save_image, args.show_image)
        case _:
            print("Не вірний режим відображення")


if __name__ == "__main__":
    main()
