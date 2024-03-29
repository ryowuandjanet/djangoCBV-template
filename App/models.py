from django.db import models

GENDER = (
  ('M', 'M'),
  ('F', 'F')
)

CAREER = (
  ('Frontend', 'Frontend'),
  ('Backend', 'Backend'),
  ('Fullstack', 'Fullstack'),
  ('Intern', 'Intern')
)

class Candidate(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=25)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=1, choices=GENDER)
    career=models.CharField(max_length=50, choices=CAREER)

    def __str__(self):
        return self.name