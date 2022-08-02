from django.shortcuts import render
from .models import Song, Singer, Album, Tag
from django.db.models.query_utils import Q
from django.core.paginator import Paginator
from django.views.generic import ListView

def home(request):
    songs = Song.objects.all().filter(tag_id=4)
    tags = Tag.objects.all()
    albums = Album.objects.all().filter(tag_id='1').order_by('?')

    return render(request, 'project/home.html', {"songs": songs, "tags": tags, "albums": albums})

def tag(request, pk):
    tag = Tag.objects.get(pk=pk)
    songs = Song.objects.all().filter(tag_id=tag.pk).order_by('?')
    paginator = Paginator(songs, 9)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'project/tag.html', {"songs": songs, "tag": tag, "page_obj": page_obj})

def songm(request):
    search = request.GET.get("search")


    if search is None:
        songs = Song.objects.all().order_by('?')
        paginator = Paginator(songs, 8)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        tops = Song.objects.all().filter(tag_id='1').order_by('?')
        tags = Tag.objects.all()
    else:
        songs = Song.objects.filter(Q(title__contains=search) | Q(album__singer__first_name__contains=search) | Q(album__singer__last_name__contains=search) | Q(album__title__contains=search))
        paginator = Paginator(songs, 7)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        tops = Song.objects.filter(tag_id='1')
        tags = Tag.objects.all()


    return render(request, "project/songm.html", {"songs": songs, "tops": tops, "tags": tags, "search": search, "page_obj": page_obj})

def songe(request, pk):
    song = Song.objects.get(pk=pk)
    asongs = Song.objects.all().filter(album__title__contains=song.album.title)
    paginator = Paginator(asongs, 7)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    ssongs = Song.objects.all().filter(album__singer__first_name__contains=song.album.singer.first_name).order_by('?')
    paginatorr = Paginator(ssongs, 7)  # Show 25 contacts per page.
    page_numberr = request.GET.get('page')
    page_objj = paginatorr.get_page(page_numberr)
    return render(request, 'project/songe.html', {"song": song, "page_obj": page_obj, "page_objj": page_objj})


def albumm(request):
    search = request.GET.get("search")

    if search is None:
        albums = Album.objects.all().order_by('?')
        paginator = Paginator(albums, 5)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        tops = Album.objects.all().filter(tag_id='1')
        paginatorr = Paginator(tops, 5)  # Show 25 contacts per page.
        page_numberr = request.GET.get('page')
        page_objj = paginatorr.get_page(page_numberr)
    else:
        albums = Album.objects.all().filter(Q(singer__album__title__contains=search) | Q(singer__first_name__contains=search) | Q(
            singer__last_name__contains=search))
        paginator = Paginator(albums, 5)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        tops = Album.objects.all().filter(tag_id='1')
        paginatorr = Paginator(tops, 5)  # Show 25 contacts per page.
        page_numberr = request.GET.get('page')
        page_objj = paginatorr.get_page(page_numberr)

    return render(request, "project/albumm.html", {"albums": albums, "tops": tops, "search": search, "page_obj": page_obj, "page_objj": page_objj})

def albume(request, pk):
    album = Album.objects.get(pk=pk)
    songs = Song.objects.all().filter(album__singer_id=album.singer.id)
    paginator = Paginator(songs, 8)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'project/albume.html', {"album": album, "songs": songs, "page_obj": page_obj})

def singerm(request):
    search = request.GET.get("search")

    if search is None:

        singers = Singer.objects.all()
        paginator = Paginator(singers, 8)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    else:
        singers = Singer.objects.filter(
            Q(first_name__contains=search) | Q(last_name__contains=search) | Q(
                album__song__title__contains=search))
        paginator = Paginator(singers, 8)  # Show 25 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    return render(request, "project/singerm.html", {"singers": singers, "search": search, "page_obj": page_obj})

def singere(request, pk):
    singer = Singer.objects.get(pk=pk)
    songs = Song.objects.all().filter(album__singer__first_name=singer.first_name)
    paginator = Paginator(songs, 9)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'project/singere.html', {"singer": singer, "songs": songs, "page_obj": page_obj})

