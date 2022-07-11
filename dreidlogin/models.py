from django.db import models
from datetime import date
# Create your models here.
class Human(models.Model):
    """Model that represents a human that was approved in our super hard test
    Nome
Robot Name
Gender
Birth year

Pet
City
Hair Color
Height

    """
    
    name = models.CharField(max_length=200)
    robot_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    birth_year = models.IntegerField()
    pet = models.BooleanField()
    city = models.CharField(max_length=200)
    hair_color = models.CharField(max_length=200)
    height = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def age(self):
        current_year = date.today().year
        return current_year - self.birth_year

    @classmethod
    def create(cls, session):
        human = cls(
            name=session.get('name'),
            robot_name=session.get('robot_name'),
            gender=session.get('gender') ,
            birth_year=session.get('birth_year'),
            pet=session.get('pet'),
            city=session.get('city'),
            hair_color=session.get('hair_color'),
            height=session.get('height')
            )
        return human.save()