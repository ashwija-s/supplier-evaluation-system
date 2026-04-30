from django.shortcuts import render, redirect
from .models import Supplier
from .forms import SupplierForm

def supplier_list(request):
    suppliers = Supplier.objects.all()

    form = SupplierForm()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
            

    sort_by = request.GET.get('sort')
    if sort_by == 'cost':
        suppliers = suppliers.order_by('cost')
    elif sort_by == 'delivery':
        suppliers = suppliers.order_by('delivery_time')
    elif sort_by == 'quality':
        suppliers = suppliers.order_by('-quality_rating')
    
    best_supplier = None
    if suppliers:
        best_supplier = sorted(
            suppliers,
            key=lambda s: (s.cost * 0.4 + s.delivery_time * 0.3 - s.quality_rating * 10 * 0.3)
        )[0]
    return render(request, 'suppliers/supplier_list.html',{'suppliers':suppliers,'best_supplier':best_supplier,'form':form})
# Create your views here.
