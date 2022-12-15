import datetime

from collections import defaultdict
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .models import Tuman, IjtimoiyHimoya, Person

def login_required_decorator(func):
    return login_required(func, login_url='login_page')

# Create your views here.
def login_page(request):
    if request.user.is_authenticated:
        return redirect('home_page')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect('home_page')
    return render(request, 'auth/login.html')

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")

@login_required_decorator
def home_page(request):
    today = datetime.date.today()
    week_day = today.day - 7
    oy = str(today).split("-")[1]
    yil = str(today).split("-")[0]

    monitoringlar = Person.objects.all()
    kunlik_summa = 0
    xaftalik_summa = 0
    oylik_summa = 0
    yillik_summa = 0

    k = 0
    for i in range(len(monitoringlar)):
        if str(today) == str(monitoringlar[i].created).split(" ")[0]:
            k += 1
            kunlik_summa += monitoringlar[i].summa

    x = 0
    for i in range(len(monitoringlar)):
        if week_day <= int(str(monitoringlar[i].created).split(" ")[0].split("-")[2]):
            x += 1
            xaftalik_summa += monitoringlar[i].summa

    o = 0
    for i in range(len(monitoringlar)):
        if int(oy) == int(str(monitoringlar[i].created).split(" ")[0].split("-")[1]):
            o += 1
            oylik_summa += monitoringlar[i].summa

    y = 0
    for i in range(len(monitoringlar)):
        if int(yil) == int(str(monitoringlar[i].created).split(" ")[0].split("-")[0]):
            y += 1
            yillik_summa += monitoringlar[i].summa

    sana = str(datetime.date.today())[8:10]
    sana = int(sana)
    context = {
        'sana': sana,
        'kunlik_summa': kunlik_summa,
        'xaftalik_summa': xaftalik_summa,
        'oylik_summa': oylik_summa,
        'yillik_summa': yillik_summa,
        'k': k,
        'x': x,
        'o': o,
        'y': y,
    }

    return render(request, 'index.html', context)

@login_required_decorator
def kunlik_monitoring_page(request):
    today = datetime.date.today()
    print(today)
    monitoringlar = Person.objects.all()

    ijtimoiy_ximoyalar_names = []
    for i in IjtimoiyHimoya.objects.all():
        ijtimoiy_ximoyalar_names.append(i.name)

    kunlik_monitoringlar = []
    jami_summa = 0
    jadval = []

    print(str(monitoringlar[0].created).split(" ")[0])
    for i in range(len(monitoringlar)):
        if str(today) == str(monitoringlar[i].created).split(" ")[0]:
            print("Asliddin")
            kunlik_monitoringlar.append(monitoringlar[i])
            jami_summa += monitoringlar[i].summa

    for i in ijtimoiy_ximoyalar_names:
        for j in kunlik_monitoringlar:
            if j.ijtimoiy_himoya == i:
                jadval.append(
                    (i, j)
                )
    res = defaultdict(list)
    for v, k in jadval: res[v].append(k)
    # print(res['Yoshlar daftari'])

    oxirgi_natija = []
    raqamlar = []
    labellar = []

    for i in res:
        raqamlar.append(len(res[i]))
        labellar.append(i)
        oxirgi_natija.append(
            [i, len(res[i])]
        )
    print(oxirgi_natija)
    sana = str(datetime.date.today())[8:10]
    sana = int(sana)

    if len(oxirgi_natija) == 0:
        a = False
    else:
        a = True

    context = {
        'kunlik_monitoringlar': kunlik_monitoringlar,
        'sana': sana,
        'jami_summa': jami_summa,
        'oxirgi_natija': oxirgi_natija,
        'a': a,
        'raqamlar': raqamlar,
        'labellar': labellar,
    }
    return render(request, 'monitoring/kunlik.html', context)

@login_required_decorator
def xaftalik_monitoring_page(request):
    week_day = datetime.date.today().day - 7
    monitoringlar = Person.objects.all()

    ijtimoiy_ximoyalar_names = []
    for i in IjtimoiyHimoya.objects.all():
        ijtimoiy_ximoyalar_names.append(i.name)

    kunlik_monitoringlar = []
    jami_summa = 0
    jadval = []

    for i in range(len(monitoringlar)):
        if week_day <= int(str(monitoringlar[i].created).split(" ")[0].split("-")[2]):
            kunlik_monitoringlar.append(monitoringlar[i])
            jami_summa += monitoringlar[i].summa

    for i in ijtimoiy_ximoyalar_names:
        for j in kunlik_monitoringlar:
            if j.ijtimoiy_himoya == i:
                jadval.append(
                    (i, j)
                )
    res = defaultdict(list)
    for v, k in jadval: res[v].append(k)
    # print(res['Yoshlar daftari'])

    oxirgi_natija = []
    raqamlar = []
    labellar = []

    for i in res:
        raqamlar.append(len(res[i]))
        labellar.append(i)
        oxirgi_natija.append(
            [i, len(res[i])]
        )
    print(oxirgi_natija)
    sana = str(datetime.date.today())[8:10]
    sana = int(sana)

    if len(oxirgi_natija) == 0:
        a = False
    else:
        a = True

    context = {
        'kunlik_monitoringlar': kunlik_monitoringlar,
        'sana': sana,
        'jami_summa': jami_summa,
        'oxirgi_natija': oxirgi_natija,
        'a': a,
        'raqamlar': raqamlar,
        'labellar': labellar,
    }
    return render(request, 'monitoring/xaftalik.html', context)

@login_required_decorator
def oylik_monitoring_page(request):
    oy = str(datetime.date.today()).split("-")[1]
    print(oy)
    monitoringlar = Person.objects.all()

    ijtimoiy_ximoyalar_names = []
    for i in IjtimoiyHimoya.objects.all():
        ijtimoiy_ximoyalar_names.append(i.name)

    kunlik_monitoringlar = []
    jami_summa = 0
    jadval = []

    for i in range(len(monitoringlar)):
        if int(oy) == int(str(monitoringlar[i].created).split(" ")[0].split("-")[1]):
            kunlik_monitoringlar.append(monitoringlar[i])
            jami_summa += monitoringlar[i].summa

    for i in ijtimoiy_ximoyalar_names:
        for j in kunlik_monitoringlar:
            if j.ijtimoiy_himoya == i:
                jadval.append(
                    (i, j)
                )
    res = defaultdict(list)
    for v, k in jadval: res[v].append(k)
    # print(res['Yoshlar daftari'])

    oxirgi_natija = []
    raqamlar = []
    labellar = []

    for i in res:
        raqamlar.append(len(res[i]))
        labellar.append(i)
        oxirgi_natija.append(
            [i, len(res[i])]
        )
    print(oxirgi_natija)
    sana = str(datetime.date.today())[8:10]
    sana = int(sana)

    if len(oxirgi_natija) == 0:
        a = False
    else:
        a = True

    context = {
        'kunlik_monitoringlar': kunlik_monitoringlar,
        'sana': sana,
        'jami_summa': jami_summa,
        'oxirgi_natija': oxirgi_natija,
        'a': a,
        'raqamlar': raqamlar,
        'labellar': labellar,
    }
    return render(request, 'monitoring/oylik.html', context)

@login_required_decorator
def yillik_monitoring_page(request):
    return render(request, 'monitoring/yillik.html')

@login_required_decorator
def shaharlar(request, pk):
    if pk == "qarshi-shahri":
        pk = "Qarshi shahri"
    elif pk == "guzor":
        pk = "G'uzor"
    elif pk == "kokdala":
        pk = "Ko'kdala"
    elif pk == "yakkabog":
        pk = "Yakkabog'"

    if len(pk.split(" ")) != 2:
        pk = f"{pk.title()} tumani"
    context = {
        'city': pk
    }
    return render(request, 'shaharlar.html', context)

@login_required_decorator
def malumot_kiritish(request):
    tumanlar = Tuman.objects.all()
    turlari = IjtimoiyHimoya.objects.all()

    if request.method == "POST":
        person = Person()

        person.ism = request.POST.get('ism')
        person.familiya = request.POST.get('familiya')
        person.otasining_ismi = request.POST.get('otasining_ismi')
        person.passport_seriya = request.POST.get('passport_seriya')
        person.tuman = request.POST.get('tuman')
        person.hozirgi_yashash_manzili = request.POST.get('doimiy_yashash_manzili')
        person.kimga_murojaat_qilgan = request.POST.get('kimga_murojaat_qilgan')
        person.ijtimoiy_himoya = request.POST.get('ijtimoiy_ximoya')
        person.nogironligi = request.POST.get('nogironligi')

        if request.POST.get('nogironligi') == "bor" or request.POST.get('nogironligi') == "Bor":
            person.nogironlik_raqami = request.POST.get('nogironlik_raqami')
        else:
            person.nogironlik_raqami = "0"
        person.mablag_ajratgan_tashkilot = request.POST.get('mablag_ajratgan_tashkilot')
        person.summa = request.POST.get('summa')
        person.photo = request.FILES.get('photo')
        person.tavsif = request.POST.get('tavsif')

        print(request.POST.get('photo'))

        person.save()
        return redirect('person_info_page', pk=person.id)


    context = {
        'tumanlar': tumanlar,
        'turlari': turlari,
    }
    return render(request, 'malumot_kiritish.html', context)

@login_required_decorator
def success(request):
    return render(request, 'success.html')

@login_required_decorator
def error_page(request):
    return render(request, 'error.html')

def export_xls(pk):
    pk = str(pk)
    import xlwt
    from datetime import datetime

    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
                         num_format_str='#,##0.00')
    style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')

    ws.write(0, 0, 1234.56, style0)
    ws.write(1, 0, datetime.now(), style1)
    ws.write(2, 0, 1)
    ws.write(2, 1, 1)
    ws.write(2, 2, xlwt.Formula("A3+B3"))

    wb.save(f'./media/excel/person_{pk}.xlsx')
    print(f"Success: {pk}")

@login_required_decorator
def person_info_page(request, pk):
    context = {}
    if str(pk).isnumeric():
        try:
            person = Person.objects.get(id=int(pk))
            context['person'] = person
            export_xls(pk)
        except:
            return redirect('error_page')
    else:
        return redirect('error_page')
    return render(request, 'person_info.html', context)

@login_required_decorator
def person_excel(request, pk):
    context = {}
    if str(pk).isnumeric():
        try:
            person = Person.objects.get(id=int(pk))
            context['person'] = person

        except:
            return redirect('error_page')
    else:
        return redirect('error_page')
    return render(request, 'person_info.html', context)