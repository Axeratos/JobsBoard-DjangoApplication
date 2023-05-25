from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexJobSeekerView.as_view(), name="home"),
    path("employer", views.IndexEmployerView.as_view(), name="employer_home"),
    path("create-company", views.CreateCompany.as_view(), name="create_company"),
    path("company-profile/<int:pk>", views.DetailCompany.as_view(), name="company_details"),
    path("companies", views.ViewCompanies.as_view(), name="all_companies"),
    path("update-company/<int:pk>", views.UpdateCompany.as_view(), name="update_company"),
    path("create-vacancy", views.CreateVacancy.as_view(), name="create_company"),
    path("detail-vacancy/<int:pk>", views.DetailVacancy.as_view(), name="vacancy_details"),
    path("errors/404", views.EntityNotFoundView.as_view(), name="not_found"),
    path("update-vacancy/<int:pk>", views.UpdateVacancy.as_view(), name="update_vacancy"),
    path("all-vacancies", views.ViewVacancies.as_view(), name="all_vacancies"),
    path("change-response-status/<int:pk>", views.VacancyResponseView.as_view(), name="change_response"),
    path("vacancy-responses/<int:pk>", views.ResponsesView.as_view(), name="view_responses"),
    path("reject-response/<int:vacancy_pk>/<int:user_pk>", views.RejectJobSeeker.as_view(), name="reject_jobseeker"),
]
