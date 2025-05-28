from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout


# ==============================
from django.conf import settings
from django.shortcuts import redirect
tutorials = [
    {
        "title": "نصب اوبونتو",
        "description": "آموزش قدم به قدم نصب سیستم عامل اوبونتو.",
        "image_url": "https://assets.ubuntu.com/v1/29985a98-ubuntu-logo32.png",
        "download_link": "/files/ubuntu_install_guide.pdf",
        "video_link": "https://www.aparat.com/v/abc123"
    },
    {
        "title": "کار با ترمینال",
        "description": "مبانی استفاده از ترمینال در لینوکس برای مبتدیان.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Bash_Logo_Colored.svg/1200px-Bash_Logo_Colored.svg.png",
        "download_link": None,
        "video_link": "https://www.aparat.com/v/def456"
    },
    {
        "title": "دستورهای پایه لینوکس",
        "description": "لیست مهم‌ترین دستورهای لینوکس با مثال.",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg",
        "download_link": "/files/linux_commands_cheatsheet.pdf",
        "video_link": None
    }
]


LINUX_DISTROS = {
    "ubuntu": {
        "name": "Ubuntu",
        "description": "Ubuntu یکی از محبوب‌ترین توزیع‌های لینوکس است که توسط Canonical توسعه داده می‌شود.",
        "download_link": "https://releases.ubuntu.com/24.04/ubuntu-24.04-desktop-amd64.iso"
    },
    "debian": {
        "name": "Debian",
        "description": "Debian یک توزیع پایدار، رایگان و محبوب از لینوکس است.",
        "download_link": "https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.5.0-amd64-DVD-1.iso"
    },
    "arch": {
        "name": "Arch Linux",
        "description": "Arch Linux توزیعی مینیمال و rolling release برای کاربران حرفه‌ای است.",
        "download_link": "https://mirror.rackspace.com/archlinux/iso/2024.05.01/archlinux-2024.05.01-x86_64.iso"
    },
    "fedora": {
        "name": "Fedora",
        "description": "Fedora یک توزیع جامعه‌محور از لینوکس است که توسط Red Hat پشتیبانی می‌شود.",
        "download_link": "https://download.fedoraproject.org/pub/fedora/linux/releases/40/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-40-1.14.iso"
    }
}

def linux_list(request):
    return render(request, "linux_distros.html")

def linux_detail(request, distro):
    data = LINUX_DISTROS.get(distro)
    if not data:
        return render(request, "404.html", status=404)
    return render(request, "linux_detail.html", data)
def logout_view(request):
    logout(request)
    return redirect('login')


def error_404_view(request, exception):

	# we add the path to the the 404.html file
	# here. The name of our HTML file is 404.html
	return render(request, '404.html')

class Home(TemplateView):
    template_name = 'home.html'

class Os(TemplateView):
    template_name = 'os.html'

class Aboutus(TemplateView):
    template_name = 'aboutus.html'

class Contactus(TemplateView):
    template_name = 'contactus.html'

class Info(TemplateView):
    template_name = 'info.html'

class Learn(TemplateView):
    template_name = 'learn.html'

class Chat(TemplateView):
    template_name = 'chat.html'

class Wikilinux(TemplateView):
    template_name = 'wikilinux.html'
    
class News(TemplateView):
    template_name = 'news.html'



class SignupView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url=reverse_lazy('login')

