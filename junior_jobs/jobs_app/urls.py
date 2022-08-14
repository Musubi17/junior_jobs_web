from django.urls import path

from .views import main_view, all_vacancies_view, vacancy_view, vacancy_cat_view, companies_view, handler500, handler404


urlpatterns = [
    path('', main_view, name='main'),
    path('vacancies/', all_vacancies_view, name='all_vacancies'),
    path('vacancies/<int:vacancy_id>/', vacancy_view, name='vacancy'),
    path('vacancies/cat/<str:category>', vacancy_cat_view, name='vacancy_cat'),
    path('companies/<int:company_id>', companies_view, name='companies'),
]

handler404 = handler404
handler500 = handler500
