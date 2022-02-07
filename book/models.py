from django.db import models

class Book(models.Model):

    GENRE_CHOICE = (
        ('Detective', 'Detective'),
        ('Comedy', 'Comedy'),
        ('History', 'History'),
        ('Fantasy', 'Fantasy'),
        ('SelfEducation', 'SelfEducation'),
        ('Classic','Classic')
    )
    title = models.CharField(max_length=100)
    description  = models.TextField()
    image = models.ImageField(upload_to='')
    genre = models.CharField(choices=GENRE_CHOICE, max_length=100, null=True)
    data = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class BookComment(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE,
                              related_name='book_comment')
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.books.title



class Expert(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE,
                              related_name='expert')
    full_name = models.CharField(max_length=50)
    ACTIVITY = (
        ('BUSINESSMAN','BUSINESSMAN'),
        ('BLOGGER','BLOGGER'),
        ('HOLLYWOOD STAR','HOLLYWOOD STAR'),
        ('DRIVER','DRIVER'),
        ('KILLER','KILLER'),
    )
    activity = models.CharField(choices=ACTIVITY,max_length=100)
    info = models.TextField()

    def __str__(self):
        return str(self.books)



class ExpertRecomendation(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE,
                              related_name='expert_recommendation')
    recommendation_text = models.TextField()

    def __str__(self):
        return str(self.books)