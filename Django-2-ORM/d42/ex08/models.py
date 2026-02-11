from django.db import models

# Create your models here.
class Planet(models.Model):
	name = models.CharField(max_length=64, primary_key=True)
	climate = models.TextField(null=True)
	diameter = models.IntegerField(null=True)
	orbital_period = models.IntegerField(null=True)
	population = models.BigIntegerField(null=True)
	rotation_period = models.IntegerField(null=True)
	surface_water = models.FloatField(null=True)
	terrain = models.CharField(max_length=128, null=True)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'ex08_planets'


class People(models.Model):
	name = models.CharField(max_length=64, primary_key=True)
	birth_year = models.CharField(max_length=32, null=True)
	gender = models.CharField(max_length=32, null=True)
	eye_color = models.CharField(max_length=32, null=True)
	hair_color = models.CharField(max_length=32, null=True)
	height = models.IntegerField(null=True)
	mass = models.FloatField(null=True)
	homeworld = models.ForeignKey(
		Planet,
		to_field='name',
		db_column='homeworld',
		on_delete=models.SET_NULL,
		null=True,
	)

	def __str__(self):
		return self.name

	class Meta:
		db_table = 'ex08_people'
