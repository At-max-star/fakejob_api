from django.db import models

# Create your models here.
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=62, verbose_name="会社名")
    job_name = models.CharField(max_length=62, verbose_name="求人名")
    salary = models.CharField(max_length=62, verbose_name="給料")
    
    job_content = models.TextField(verbose_name="仕事内容")
    application_requirement = models.TextField(verbose_name="応募要件")
    created = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    modified = models.DateTimeField(auto_now=True, verbose_name="更新日")
    
    def __str__(self):
        return self.job_name

    class Meta:
        db_table = 'articles'
        verbose_name_plural = "求人"
        
