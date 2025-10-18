from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Depo, Train, Wagon, Remark, TrainWagon
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q

@login_required
def dashboard(request):
    depots = Depo.objects.all()
    total_remarks = Remark.objects.count()
    open_remarks = Remark.objects.filter(status='open').count()
    return render(request, 'pdk_system/dashboard.html', {
        'depots': depots, 'total_remarks': total_remarks, 'open_remarks': open_remarks
    })

@login_required
def form_blank(request):
    if request.method == 'POST':
        train_number = request.POST.get('train_number')
        wagons_raw = request.POST.get('wagons')
        wagon_nums = [w.strip() for w in wagons_raw.split(',') if w.strip()]
        # find or create train
        train = Train.objects.create(number=train_number, depo=Depo.objects.first())
        # attach wagons
        wagons = []
        for num in wagon_nums:
            wagon, _ = Wagon.objects.get_or_create(number=num)
            TrainWagon.objects.create(train=train, wagon=wagon)
            wagons.append(wagon)
        # find open remarks for these wagons
        open_remarks = Remark.objects.filter(wagon__in=wagons, status='open').order_by('date_found')
        return render(request, 'pdk_system/blank_preview.html', {'train': train, 'wagons': wagons, 'open_remarks': open_remarks})
    return render(request, 'pdk_system/form_blank.html')

@login_required
def fill_blank(request, train_id):
    train = get_object_or_404(Train, id=train_id)
    if request.method == 'POST':
        # process submitted remarks
        # For simplicity, allow adding new remark textareas named new_remark_{wagon.id}
        for tw in TrainWagon.objects.filter(train=train):
            fixed = request.POST.get(f'fixed_{tw.wagon.id}') == 'on'
            if fixed:
                Remark.objects.filter(wagon=tw.wagon, status='open').update(status='closed')
        # new remarks
        for key, val in request.POST.items():
            if key.startswith('new_remark_') and val.strip():
                wagon_id = int(key.split('_')[-1])
                wagon = Wagon.objects.get(id=wagon_id)
                Remark.objects.create(wagon=wagon, train=train, description=val, created_by=request.user)
        messages.success(request, 'Бланк сохранён')
        return redirect(reverse('dashboard'))
    wagons = [tw.wagon for tw in TrainWagon.objects.filter(train=train)]
    open_remarks = Remark.objects.filter(wagon__in=wagons, status='open')
    return render(request, 'pdk_system/fill_blank.html', {'train': train, 'wagons': wagons, 'open_remarks': open_remarks})
