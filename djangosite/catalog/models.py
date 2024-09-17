from django.db import models
import uuid
from django.urls import reverse

class Genre(models.Model):
    """
    This model represents a book genres (e.g. Science Fictin, Non Fiction, etc.)
    """

    name = models.CharField(max_length=150, help_text="Enter a book genre (e.g. Sci-Fi, French Poetry, etc.)")

    def __str__(self):
        """
        This method represents Model Object in Admin Site, for example
        """
        return self.name

class Book(models.Model):
    """
    Model that represents a book (not a specific copy of a book)
    """

    title = models.CharField(max_length=150)
    author = models.ForeignKey("Author", on_deletete = models.SET_NULL, null=True)

    summary = models.TextField(max_length=1500, help_text = "Enter a brief summary (description) of a book (it's annotation)")
    isbn = models.CharField("ISBN", max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models. ManyToManyField(Genre, help_text="Select a genre for the book")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[str[self.id]])
    
class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book=models.ForeignKey("Book", on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    loan_status = (
        ("m", "Maintenance"),
        ("o", "On loan"),
        ("a", "Available"),
        ("r", "Reversed")
    )

    status = models.CharField(choices=loan_status, blank=True, max_length=1, default="m", help_text="Book availability")

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return f"{self.id}, ({self.book.title})"
    
class Author(models.Model):

    first_name = models.CharField(max_length=100, help_text="First name of author")
    last_name = models.CharField(max_length=100, help_text="Last name of author (not necessary)", null=True, blank=True)
    data_birth = models.DateField(null=True, blank=True)
    data_dead = models.DateField("Dead", null=True, blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])
        
