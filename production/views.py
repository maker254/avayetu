import pandas as pd
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DetailView
from production.models import Customer,Vehicle,GenealogyFile,EOL
from production.forms import CustomerCreateForm,VehicleCreateForm,GenealogyUploadForm,EOLCreateForm

# Create your views here.
class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerCreateForm
    template_name = "production/customer-create.html"

class VehicleCreateView(CreateView):
    model = Vehicle
    form_class = VehicleCreateForm
    form = GenealogyUploadForm
    vehicle_data = Vehicle.objects.all()
    template_name = "production/vehicle-create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicle_data = self.vehicle_data
        context["vehicle_data"] = vehicle_data
        return context

def import_genealogydata_to_db(request):
    data_to_display = Vehicle.objects.all()
    if request.method == "POST":
        form = GenealogyUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print("form iko chonjo")
            file = request.FILES['file']
            GenealogyFile.objects.create(file=file) #upload/create file to GenealogyFile model
            df = pd.read_excel(file)
            for _, row in df.iterrows():
                #created = True
                vehicle, created = Vehicle.objects.get_or_create(
                    model=row['MODEL'],
                    lot=row['LOT'],
                    vin_no=row['VIN NUMBER'] if row['VIN NUMBER'] else row['Serial Number'],
                    engine_no=row['ENGINE NUMBER'] or row['HDT Engine'],
                    gearbox_no=row['GEARBOX NUMBER'] or row['Gear Box'],
                    cabin_no=row['CABIN NUMBER'],
                    front_axle_no=row['FRONT AXLE NUMBER'] or row['FF - Front Axle'],
                    rear_axle1_no=row['RR AXLE NUMBER'] or row['RR - Rear axle'],
                    rear_axle2_no=row['RI AXLE NUMBER'] or row['RI - Rear axle']
                )
                if created:
                    messages.success(request, f'Successfully imported Genealogy Data') #{vehicle.vin_no}
                else:
                    messages.warning(request, f'{vehicle.vin_no} upload error( vin either already exists or has an error please correct the uploaded excel file and try again')
            print("Data upload/import to DB successful")
            return redirect('/production/addvehicle')
        else:
            print(form.errors)
            print(form)
            print("Myfren the Form is not valid")
    else:
        form = GenealogyUploadForm
    return render(request, "production/genealogy-import.html", {'form':form, 'vehicle_data':data_to_display})    
    

class EOLCreateView(CreateView):
    model = EOL
    form_class = EOLCreateForm
    template_name = "production/eol-create.html"

class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = "production/vehicle-detail.html"



