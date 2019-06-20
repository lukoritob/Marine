from django.db import models

class BenthicSurvey_Data(models.Model):
    Enter_transect_ID = models.IntegerField()
    Enter_benthic_category = models.CharField(max_length=20)
    Enter_total_cover = models.IntegerField()


class FishSurvey_data(models.Model):
    ID = models.IntegerField(primary_key=True)
    Trans_ID = models.IntegerField()
    Name_Local = models.CharField(max_length=20)
    Total_Count = models.IntegerField()

class Invert_Data(models.Model):
    TransID = models.IntegerField()
    Name_Invert = models.CharField(max_length=20)
    No_Invert = models.IntegerField()
    
class Lookup_Benthic(models.Model):
    Name_Local = models.CharField(max_length=30)
    Abbrv = models.CharField(max_length=5)
    Name_Common = models.CharField(max_length=30)
    ID = models.IntegerField(primary_key=True)
    
class Lookup_Fish(models.Model):
    Name_Local = models.CharField(max_length=30)
    Name_Common = models.CharField(max_length=30)
    ID = models.IntegerField(primary_key=True)
    Scientific_N = models.CharField(max_length=30)
 
class Lookup_Invert(models.Model):
    Name_Local = models.CharField(max_length=30)
    Name_Common = models.CharField(max_length=30)
    ID = models.IntegerField(primary_key=True)
    
class Lookup_Site(models.Model):   
    SiteName = models.CharField(max_length=20)
    ID = models.IntegerField(primary_key=True)
    GPS_X = models.IntegerField()
    GPS_Y = models.IntegerField()
    
    def __str__(self):
        return self.SiteName
    
class Survey_Info(models.Model):
    TransID = models.IntegerField(primary_key=True)
    Name_Data_Collector = models.CharField(max_length=30)
    Site_Name = models.CharField(max_length=20)
    Trans_No = models.IntegerField()
    Date_Survey = models.DateTimeField('date surveyed')
