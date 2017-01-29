from django.db import models


class Experience(models.Model):
    EXPERIENCE_TYPE_CHOICES = (
        ('ET01', 'Artistic Endeavors'),
        ('ET02', 'Community Service/Volunteer --Medical/Clinical'),
        ('ET03', 'Community Service/Volunteer --Not Medical/Clinical'),
        ('ET04', 'Conferences Attended'),
        ('ET05', 'Extracurricular Activities'),
        ('ET06', 'Hobbies'),
        ('ET07', 'Honors/Awards/Recognition'),
        ('ET08', 'Intercollegiate Athletics'),
        ('ET09', 'Leadership - not listed elsewhere'),
        ('ET10', 'Military Service'),
        ('ET11', 'Other'),
        ('ET12', 'Paid Employment - Medical/Clinical'),
        ('ET13', 'Paid Employment - Not Medical/Clinical'),
        ('ET14', 'Physician Shadowing/Clinical Observation'),
        ('ET15', 'Presentation/Posters'),
        ('ET16', 'Publications'),
        ('ET17', 'Research/Lab'),
        ('ET18', 'Teaching/Tutoring/Teaching Assistant)')
    )
    experience_type = models.CharField(max_length=4, choices=EXPERIENCE_TYPE_CHOICES)
    experience_name = models.CharField(max_length=200)

    MONTH_CHOICES=(
        (1, 'January'),
        (2, 'February'), 
        (3, 'March'),
        (4, 'April'),
        (5, 'May'),
        (6, 'June'),
        (7, 'July'),
        (8, 'August'),
        (9, 'September'),
        (10, 'October'),
        (11, 'November'),
        (12, 'December')
    )
    start_month = models.PositiveSmallIntegerField(choices=MONTH_CHOICES)
    start_year = models.PositiveSmallIntegerField()
    end_month = models.PositiveSmallIntegerField(choices=MONTH_CHOICES)
    end_year = models.PositiveSmallIntegerField()
    total_hours = models.PositiveIntegerField()
    #################################################################################
    #TODO: repeated (yes/no) 2nd start/end date, 3rd start/end date, ... etc
    #################################################################################
    organization_name = models.CharField(max_length=100, blank=True)
    #################################################################################
    #TODO: country, (state if usa), (province if canada), city
    #################################################################################
    contact_first_name = models.CharField(max_length=35)
    contact_last_name = models.CharField(max_length=35)
    contact_title = models.CharFeild(max_length=100)

    #################################################################################
    #TODO: Verify phone_regex
    #################################################################################
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact_phone = models.CharField(validators=[phone_regex], blank=True) # validators should be a list

    contact_email = models.EmailField()
    experience_description = models.CharField(max_length=700)
    notes = models.TextField(max_legnth=2000)
