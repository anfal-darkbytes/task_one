class Pdffile(models.Model):
    pdf = models.FileField(upload_to='pdfdirectory/')
    filename = models.CharField(max_length=20)
    pagenumforcover = models.IntegerField()
    coverpage = models.FileField(upload_to='coverdirectory/')
