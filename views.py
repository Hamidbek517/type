import json
from datetime import timedelta
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Avg, Count, Max, Sum
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Natija
from .texts import tasodifiy_matn

def royxat_form(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.save())
        return redirect("home")
    return render(request, "core/royxat.html", {"form": form})

def statistika(user):
    q = Natija.objects.filter(user=user)
    bugun = timezone.localdate()
    a = q.aggregate(eng=Max("wpm"), aniq=Avg("aniqlik"), jami=Count("id"), belgi=Sum("togri"))
    return {"bugun": q.filter(sana__date=bugun).count(), "eng": round(a["eng"] or 0), "aniq": round(a["aniq"] or 0),
            "jami": a["jami"], "belgi": a["belgi"] or 0, "soz": (a["belgi"] or 0) // 5}

def home(request):
    return render(request, "core/home.html", {"s": statistika(request.user) if request.user.is_authenticated else None})

def mashq(request):
    return render(request, "core/mashq.html", {"matn": tasodifiy_matn()})

def matn_api(request):
    return JsonResponse({"matn": tasodifiy_matn()})

@require_POST
def saqlash(request):
    if not request.user.is_authenticated:
        return JsonResponse({"xato": "Natijani saqlash uchun tizimga kiring."}, status=401)
    try:
        d = json.loads(request.body)
        vaqt = int(d["vaqt"]); togri = int(d["togri"]); jami = int(d["jami"])
        seriya = [round(float(x), 1) for x in d.get("seriya", [])][:120]
    except (ValueError, KeyError, TypeError):
        return JsonResponse({"xato": "Ma'lumotlar noto‘g‘ri."}, status=400)
    if vaqt not in (30, 60) or jami < 0 or togri < 0 or togri > jami or jami > 2000:
        return JsonResponse({"xato": "Natija qabul qilinmadi."}, status=400)
    minut = vaqt / 60
    wpm = togri / 5 / minut
    if wpm > 300:
        return JsonResponse({"xato": "Natija haqiqiy emas deb topildi."}, status=400)
    oldin = Natija.objects.filter(user=request.user).aggregate(r=Max("wpm"), o=Avg("wpm"))
    n = Natija.objects.create(user=request.user, wpm=round(wpm, 1), cpm=round(togri / minut, 1),
        aniqlik=round(togri / jami * 100, 1) if jami else 0, xatolar=jami - togri, togri=togri, vaqt=vaqt, seriya=seriya)
    return JsonResponse({"rekord": oldin["r"] is None or n.wpm > oldin["r"], "rekord_qiymat": round(max(oldin["r"] or 0, n.wpm)),
        "oldingi_ortacha": round(oldin["o"]) if oldin["o"] is not None else None})

def reyting(request):
    bugun = timezone.localdate()
    qator = list(Natija.objects.filter(sana__date=bugun).values("user__username")
        .annotate(eng=Max("wpm"), aniq=Avg("aniqlik"), soni=Count("id")).order_by("-eng", "-aniq"))
    mening = next((i + 1 for i, r in enumerate(qator) if request.user.is_authenticated and r["user__username"] == request.user.username), None)
    return render(request, "core/reyting.html", {"qator": qator[:50], "mening": mening, "bugun": bugun})

@login_required
def natijalarim(request):
    q = Natija.objects.filter(user=request.user)
    return render(request, "core/natijalarim.html", {"s": statistika(request.user), "royxat": q[:20],
        "seriya": list(reversed([n.wpm for n in q[:15]]))})

def sozlamalar(request):
    return render(request, "core/sozlamalar.html")
