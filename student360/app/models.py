from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30, blank=False)
    gender = models.CharField(max_length=6, blank=False)
    rollNo = models.AutoField(primary_key=True) #auto increment field
    standard = models.CharField(max_length=5, blank=False)
    section = models.CharField(max_length=1, blank=False)

    class Meta:
        db_table = "Student"

class Subject(models.Model):
    studentRollNo = models.IntegerField(primary_key=True, blank=False)
    english = models.IntegerField(blank=False, default=0)
    science = models.IntegerField( blank=False, default=0)
    maths = models.IntegerField(blank=False, default=0)
    computer = models.IntegerField(blank=False, default=0)
    social = models.IntegerField(blank=False, default=0)
    
    # The value in this field is derived from the first two.
    # Updated every time the model instance is saved.
    total_marks = models.PositiveIntegerField(
        default=0,  # This value will be overwritten during save()
        editable=False,  # Hides this field in the admin interface.
    )

    student_name = models.CharField(max_length=30, blank=False, default="")

    def save(self, *args, **kwargs):
        # calculate sum before saving.
        self.total_marks = self.calculate_sum()
        self.student_name = self.get_student_name()
        super(Subject, self).save(*args, **kwargs)

    def calculate_sum(self):
        """ Calculate a numeric value for the model instance. """
        try:
            return self.english + self.science + self.maths + self.computer + self.social
        except KeyError:
            # Value_a or value_b is not in the VALUES dictionary.
            # Do something to handle this exception.
            # Just returning the value 0 will avoid crashes, but could 
            # also hide some underlying problem with your data.
            return 0     

    def get_student_name(self):
        stud = Student.objects.get(rollNo=self.studentRollNo)
        return stud.name

    class Meta:
        db_table = "Subject"