from django.shortcuts import render
import math


def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def sign_up(request):
    return render(request, 'sign_up.html')

def single(angle, length, gravity):
    initial_angle_rad = math.radians(angle)
    period = 2 * math.pi * math.sqrt(length / gravity)
    angular_frequency = 2 * math.pi / period
    t_values = [i / 100 for i in range(int(period * 100))]
    theta_values = [initial_angle_rad * math.cos(angular_frequency * t) for t in t_values]
    return t_values, theta_values

def both(angle, length):
    rad = math.radians(angle)
    periodE = 2 * math.pi * math.sqrt(length / 9.807)
    periodM = 2 * math.pi * math.sqrt(length / 1.62)
    angfreE = 2 * math.pi / periodE
    angfreM = 2 * math.pi / periodM
    tvalues_E = [i / 100 for i in range(int(periodE * 100))]
    tvalues_M = [i / 100 for i in range(int(periodM * 100))]
    thetaE = [rad * math.cos(angfreE * t) for t in tvalues_E]
    thetaM = [rad * math.cos(angfreM * t) for t in tvalues_M]

def pendulum(request):
    if request.method == 'POST':
        length = float(request.POST.get('length'))
        initial_angle = float(request.POST.get('initial_angle'))
        radio = int(request.POST.get('gravity'))
        status = 1

        gravity = 9.8  # default gravity
        if radio == 1:
            gravity = 9.8
            t_values, theta_values = single(initial_angle, length, gravity)
            choice = "single"
            return render(request, 'pendulum.html', { 'choice':choice, 'status':status,'length':length,'t_values': t_values, 'theta_values': theta_values})
        elif radio == 2:
            gravity = 1.62
            t_values, theta_values = single(initial_angle, length, gravity)
            choice = "single"
            return render(request, 'pendulum.html', {'choice':choice, 'status':status, 'length':length, 't_values': t_values, 'theta_values': theta_values})
        elif radio == 3:
            choice = "both"
            return both(initial_angle, length)
        else:
            t_values, theta_values = single(initial_angle, length, gravity)
            choice = "single"
            return render(request, 'pendulum.html', {'choice':choice, 'status':status,  'length':length, 't_values': t_values, 'theta_values': theta_values})

    else:
        return render(request, 'pendulum.html')

def projectile(request):
    return render(request, 'projectile.html')
