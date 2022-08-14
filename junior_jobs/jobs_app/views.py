from django.shortcuts import render

from .models import Vacancy, Specialty, Company


def main_view(request):
    specialities = Specialty.objects.all()
    companies = Company.objects.all()
    context = {
        'specialities': specialities,
        'companies': companies,
        'title': 'Джуманджи',
    }
    return render(request, 'jobs_app/index.html', context=context)


def all_vacancies_view(request):
    vacancies = Vacancy.objects.all()
    context = {
        "vacancies": vacancies,
        'title': 'Все Вакансии',
    }
    return render(request, 'jobs_app/all_vacancies.html', context=context)


def vacancy_view(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    context = {
        'vacancy': vacancy,
        'title': vacancy.title,
    }
    return render(request, 'jobs_app/vacancy.html', context=context)


def vacancy_cat_view(request, category):
    specialty = Specialty.objects.get(code=category)
    vacancies = Vacancy.objects.filter(specialty=specialty.id)
    context = {
        'vacancies': vacancies,
        'specialty': specialty,
        'title': specialty.title,
    }

    return render(request, 'jobs_app/vacancies.html', context=context)


def companies_view(request, company_id):
    company = Company.objects.get(id=company_id)
    vacancies = Vacancy.objects.filter(company_id=company_id)
    context = {
        'company': company,
        'vacancies': vacancies,
        'title': company.name,
    }
    return render(request, 'jobs_app/company.html', context=context)


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
