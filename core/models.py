from django.db import models

# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     bio = models.TextField()

#     def __str__(self):
#         return self.name

# class Blog(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     pub_date = models.DateTimeField(auto_now_add=True)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title


class userModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll_no = models.IntegerField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name
    