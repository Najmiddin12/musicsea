from django.db import models

class Singer(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    when_born = models.CharField(max_length=100, blank=False, null=False)
    where_born = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Album(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    cover = models.ImageField(upload_to='images/')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to='images/')
    audio = models.FileField(upload_to='files/')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        ordering = ('tag_id',)

    def __str__(self):
        return self.title

class Playlist(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


