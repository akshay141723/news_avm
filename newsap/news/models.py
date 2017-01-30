from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ResolvedNewsType(models.Model):
	resolved_news_type_name=models.CharField(max_length=250, unique=True)

	class Meta:
		managed=False
		db_table = "resolved_news_type"

class UnresolvedNewsType(models.Model):
	unresolved_news_type_name=models.CharField(max_length=250)
	
	class Meta:
		managed=False
		db_table = "unresolved_news_type"

class MapUnresolvedResolvedNewsTypeMap(models.Model):
	resolved_news_type_id=models.ForeignKey(resolved_news_type)
	unresolved_news_type_id=models.ForeignKey(unresolved_news_type,unique=True)
	
	class Meta:
		managed=False
		db_table = "map_unresolved_resolved_news_type_map"

class ResolvedLocation(models.Model):
	resolved_location_name=models.CharField(max_length=250,unique=True)
		
	class Meta:
		managed=False
		db_table = "resolved_location"

class UnresolvedLocation(models.Model):
	unresolved_location_name=models.CharField(max_length=250)
	
	class Meta:
		managed=False
		db_table = "unresolved_location"

class MapUnresolvedResolvedLocation(models.Model):
	resolved_location_id=models.ForeignKey(resolved_location)
	unresolved_location_id=models.ForeignKey(unresolved_location,unique=True)
	
	class Meta:
		managed=False
		db_table = "map_unresolved_resolved_location"

class Source(models.Model):
	source_name=models.CharField(max_length=250)
	source_url=models.URLField("URL", unique=True)
	
	class Meta:
		managed=False
		db_table = "source"


class Author(models.Model):
	author_name=models.CharField(max_length=250)
	source_id=models.ForeignKey(source)
	
	class Meta:
		managed=False
		db_table = "author"


class ArticleDownload(models.Model):
	local_file_path=models.CharField(max_length=500)
	article_download_created_date=models.DateTimeField(blank=False)
	article_download_last_updated=models.DateTimeField(blank=False)
	iss_parsed=models.TextField(max_length=5)
	
	class Meta:
		managed=False
		db_table = "article_download"

class ArticleParsed(models.Model):
	article_title=models.CharField(max_length=1000)
	uresolved_news_type_id=models.ForeignKey(unresolved_news_type)
	url=models.URLField("URL", unique=True)
	published_date=models.DateTimeField(blank=True)
	created_date=models.DateTimeField(blank=True)
	unresolved_location_id=models.ForeignKey(unresolved_location)
	author_id=models.ForeignKey(author)
	Source_id=models.ForeignKey(source)
	unique_id=models.CharField(max_length=250)
	article_download_id=models.ForeignKey(article_download)
	
	class Meta:
		managed=False
		db_table = "article_parsed"

class ArticleContent(models.Model):
	article_parsed_id=models.ForeignKey(article_parsed)
	content=models.TextField()
	
	class Meta:
		managed=False
		db_table = "article_content"




