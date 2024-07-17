from django.shortcuts import render

def admin_sign_in(request):
    template_name = 'admin_dashboard/sign-in.html'
    return render(request, template_name)