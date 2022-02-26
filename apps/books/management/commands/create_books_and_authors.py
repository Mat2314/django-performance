from django.core.management.base import BaseCommand, CommandError
from apps.authors.models import Author
from apps.books.models import Book
import random


class Command(BaseCommand):
    help = 'Create multiple books and authors records'

    def add_arguments(self, parser):
        parser.add_argument('authors_amount', nargs='?', type=int)

    def handle(self, *args, **options):
        # Get amount of authors to add the new ones with indexes that will not repeat
        amount_of_authors = Author.objects.all().count()

        for i in range(options['authors_amount']):
            # Create an author
            new_author = Author.objects.create(name="Author_" + str(i + amount_of_authors))

            # Create random amount of books for this author
            books_amount = random.randint(1, 5)
            for _ in range(books_amount):
                Book.objects.create(
                    title="Book_" + str(i),
                    preview="In a land far far away ...",
                    price=random.randint(10, 100),
                    author=new_author
                )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {options["authors_amount"]} authors and their books'))
