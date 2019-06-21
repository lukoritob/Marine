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
    
    #Report models.
# class Average_fish_density(models.Model):
#     Name_Local = models.CharField(max_length=30)
#     AvgOf_Total_Count = models.FloatField()


# class Average_fish_density_persite_allyears(models.Model):
#     SiteName = models.CharField(max_length=20
#     first = models.CharField(max_length=30)
#     AvgOf_Total_Count = models.FloatField()
    


# class Annual_average_fish_density_persite(models.Model):
#     SiteName = models.CharField(max_length=20)
#     Date_Survey = models.DateTimeField('date surveyed')
#     Name_Local = models.CharField(max_length=30)
#     Total_Count = models.IntegerField()
     
     
     

# class Average_benthic_cover(models.Model):
#     Enter_benthic_category = models.CharField(max_length=20)
#     Avg_Of_Cover = models.FloatField()


# class Average_benthic_cover_persite_allyears(models.Model):
#     SiteName = models.CharField(max_length=20)
#     Enter_benthic_category = models.CharField(max_length=20)
#     Avg_Of_Cover = models.FloatField()


# class Annual_average_benthic_cover_persite(models.Model):
#     pass

# class Average_invertebrates_cover(models.Model):
#     Name_Invert = models.CharField(max_length=20)
#     AvgOf_No_Invert = models.FloatField()


# class Average_invertebrates_cover_persite_allyears(models.Model):
#     SiteName = models.CharField(max_length=20)
#     Date_Survey = models.DateTimeField('date surveyed')
#     FirstOf_Name_Invert = models.CharField(max_length=30)
#     SumOf_No_Invert = models.IntegerField()
#     AvgOf_No_Invert = models.FloatField()


# class Annual_average_invertebrate_cover_persite(models.Model):
#     SiteName = models.CharField(max_length=20)
#     Date_Survey = models.DateTimeField('date surveyed')
#     FirstOf_Name_Invert = models.CharField(max_length=30)
#     AvgOf_No_Invert = models.FloatField()
    

#overall fish records with averages per fish type per site.
# class Overall_fishrecords(models.Model):
#     pass

#overall invertebrate data with % per year per invert per site.
# class Overall_invertebrate_data(models.Model):
#     pass


