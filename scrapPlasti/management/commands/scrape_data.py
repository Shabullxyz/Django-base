
from django.core.management.base import BaseCommand
from scrapPlasti.scraper import scrape_website

class Command(BaseCommand):
    help = 'Run the web scraper to get HTML content'

    def handle(self, *args, **kwargs):
        html_content = scrape_website()
        if html_content:
            self.stdout.write(self.style.SUCCESS('Successfully retrieved the HTML content'))
            self.stdout.write(html_content)
        else:
            self.stdout.write(self.style.ERROR('Failed to retrieve the HTML content'))
