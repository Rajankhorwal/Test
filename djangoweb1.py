#urls.py for path
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import view1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view1.index,name='rajan'),
    path('analyze',view1.analyze,name='analyze'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#in setting in dirs insert  directory name in which html files are present
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],

#view1.py
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def index(request):
    context = {}
    if request.method == 'POST' :
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'raj.html', context)


def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")

#raj.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>mysite</title>
    <div  style="padding-left: 200px" >
    {% load static %}
    <img src="{%static 'newsite/images/logo.jpg'%}" width="50" height="50">
    </div>

<style type="text/css">
h1 {text-align: center;}


.sidenav {
			height:100%;
			width:160px;
			position: fixed;
			z-index:1;
			top:0;
			left:0;
			background-color:#111;
			overflow-x:hidden;
			padding-top:20px;
		}

		.sidenav a {
			padding:6px 8px 6px 16px;
			text-decoration: none;
			font-size:25px;
			color: #818181;
			display:block;
		}

		.sidenav a:hover{
			color:#f1f1f1;
		}

        .main{
			margin-left:160px;
			padding: 0px 10px;
        }

.topnav {
  overflow: hidden;

  background-color: #333;
}

/*.topnav a {*/
/*  float: left;*/
/*  display: block;*/
/*  color: #f2f2f2;*/
/*  text-align: center;*/
/*  padding: 10px 10px;*/
/*  text-decoration: none;*/
/*  font-size: 17px;*/
/*}*/

/*.topnav a:hover {*/
/*  background-color: #ddd;*/
/*  color: black;*/
/*}*/

.topnav a.active {
  background-color: #4CAF50;
  color: white;
}

/*.topnav .icon {*/
/*  display: none;*/
/*}*/

    body{
        min-height: 1000px;
        background-image: url("https://previews.123rf.com/images/bbbaaaaz/bbbaaaaz1607/bbbaaaaz160700001/61569391-fond-moderne-avec-style-plexus-parfait-pour-le-site-web-ou-des-banni%C3%A8res-fonds-ou-comme-un-fond-d-%C3%A9cr.jpg");
        background-repeat: repeat;
        background-size: cover;
    }


    .topnav ul {
        margin: 0;
        padding: 0;
        list-style: none;
        position: relative;
    }

     .topnav ul li a {
         display: block;
         padding: 10px;
         color: white;
         text-decoration: none;
         width: 150px;

     }
     .topnav ul:after {
         content: "";
         clear: both;
         display: block;
     }
     .topnav ul li {
         float: left;
         list-style: none;
     }
     .topnav ul ul{
         display:none;
     }


     .topnav ul li:hover>ul {
         display: block;
     }
     .topnav ul li:hover {
     background: black;
         transition: 0.9s;
     }
     .topnav ul li:hover a {
         color: white;
     }
     .topnav ul ul {

         background: black;
         padding: 0;
         margin: 0;
         position: absolute;
         top: 100%;
     }
     .topnav ul ul li {
         float: none;
         position: relative;
     }

     .topnav ul ul li a {
         padding: 25px;
         color: white;
         width: 300px;
         text-align: left;
     }
     .topnav ul ul li a:hover {
         background: lightblue;
         color: black;
         transition: 0.9s;
     }




</style>
</head>
<body>

<h1>Welcome to my first django Website</h1>

<div class="topnav" id="myTopnav" style="padding-left:200px">
    <ul>
    <li><a href="#home" class="active">Home</a></li>
    <li><a href="#news" class="fa fa-phone">contact</a></li>
    <li><a href="#contact">news</a></li>
    <li><a href="#more">more</a>
        <ul>
        <li><a href="#about">about</a></li>
        <li><a href="#contact">contact</a></li>
        <li><a href="#create">create</a></li>
        <li><a href="#register">register</a></li>
        </ul>
    </li>
    </ul>

<!--    <div style="padding-top: 13px">-->
<!--  <nav class="navbar navbar-light bg-light">-->
<!--      <form class="form-inline">-->
<!--    <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">-->
<!--    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>-->
<!--   </form>-->
<!--   </nav>-->
<!--    </div>-->
  </div>

<div style="padding-left:500px">
<form action='/analyze' method='get'>

 <br><br><br><br><textarea name='text' style='margin: 0px; width: 512px; height: 74px;'></textarea><br>
    <input type="checkbox" name="removepunc">remove punctuations(first need to click checkbox before submit)<br>
    <br><button type="submit">Submit</button>

</form>
{% block content %}
  <h2>Upload</h2>
  <form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <input type="file" name="document">
    <button type="submit">Upload file</button>
  </form>
 {% if url %}
    <p>Uploaded file: <a href="{{ url }}">{{ url }}</a></p>
  {% endif %}

{% endblock %}

</div>
<div class="sidenav">
		<a href="/">Home</a>
		<a href="/create">Create</a>
		<a href="https://www.tutorialspoint.com/django/index.htm">help</a>
	</div>



</body>
</html>

