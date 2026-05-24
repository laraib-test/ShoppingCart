from django.core.management.base import BaseCommand

from shoppinglist.scraper import scrape_all


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        scrape_all()

        self.stdout.write(
            self.style.SUCCESS("Scraping completed successfully.")
        )