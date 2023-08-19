from django.core.management.base import BaseCommand
from rest_framework.exceptions import ValidationError
from currencies.serializers import CurrencySerializer
import requests


class Command(BaseCommand):
    help = "Receiving and saving currencies and their rates"

    def handle(self, *args, **options):
        try:
            response = requests.get(
                "https://www.cbr-xml-daily.ru/daily_json.js", timeout=0.5
            )
            response.raise_for_status()
            data = response.json()
            data = list(data.get("Valute").values())
            serializer = CurrencySerializer(data=data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            self.stdout.write("Collection of currencies and their rates completed.")
        except requests.exceptions.RequestException as ex:
            self.stdout.write(f"WARN! Request exception found:\n{ex}")
        except KeyError:
            self.stdout.write("Response body structure has been changed.")
        except ValidationError as ex:
            self.stdout.write(f"WARN! Validation error found:\n{ex}")
