from django.db import models
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=40,blank=False)

class GenealogyFile(models.Model):
    file = models.FileField(upload_to="excel")


class VehicleModel(models.Model):
    model_name = models.CharField(max_length=15,blank=False)
    model_code = models.CharField(max_length=15,blank=False)
    customer = models.CharField(max_length=15,blank=False) #change to foreighnKey field to customer model

class Vehicle(models.Model): #info to be imported from genealogy excel files 
    model = models.CharField(max_length=15,blank=False,null=False) #change to foreighnKey with vehiclemodel
    lot = models.CharField(max_length=10,blank=False,null=False)
    vin_no = models.CharField(max_length=17,blank=False,null=False) #add condition - length has to be 17 characters - legal requirement
    engine_no = models.CharField(max_length=15,blank=False,null=False)
    gearbox_no = models.CharField(max_length=15,blank=False,null=False)
    cabin_no = models.CharField(max_length=15,blank=True,null=True)
    front_axle_no = models.CharField(max_length=15,blank=False,null=False)
    rear_axle1_no = models.CharField(max_length=15,blank=False,null=False)
    rear_axle2_no = models.CharField(max_length=15,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vin_no

    def get_absolute_url(self):
        return reverse('home')


#class VehicleStatus(moels.Model): #model tracks status of each unit during build (production - REWORK/EOL - DISPATCH)
    



class Claim(models.Model): #MODELtracks claims per models
    customer = models.CharField(max_length=20,blank=False) #change to foreighnkey field to cuetomer model
    model_name = models.CharField(max_length=20, blank=False) #change to foreighnkey field to vehiclemodels - makes above field redundant 
    part_no = models.CharField(max_length=15, blank=False)
    part_description = models.CharField(max_length=20, blank=False)
    quantity = models.IntegerField()
    lot_no = models.CharField(max_length=10, blank=False)
    vehicle = models.CharField(max_length=17, blank=False) #change this to a foreighn key field to vehicle model
    category = models.CharField(max_length=5, blank=False) #change to choiceField (KDQR,MMO)
    reason_code = models.CharField(max_length=20, blank=False) #change to choiceField) (Wrong Shipment, Not Supplied, Short Shipment, pack damage, line Damage, Line Loss)
    created = models.DateTimeField(auto_now_add=True)
    #add imageupload field for photo evidence.
    #add option to handle repetitive claims e.g claim affecting all units in a lot - to ease data entry. explore adding repeated boolean field 


class EOL(models.Model):
    vehicle = models.OneToOneField(Vehicle,on_delete=models.CASCADE)
    brakeTest = models.BooleanField(default=False)
    wheelAlignment = models.BooleanField(default=False)
    diagnosis = models.BooleanField(default=False)
    roadTest = models.BooleanField(default=False)
    qc = models.BooleanField(default=False)
    remarks = models.CharField(blank=True, max_length=500)


class Rework(models.Model):
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    details = models.CharField(blank=True, max_length=500)
    manning = models.IntegerField(blank=True)
    duration = models.IntegerField(blank=True) 
    date = models.DateTimeField(auto_now_add=False)
    #claim = models.ForeignKey(Claim)


