from django.urls import path
from baseApp import views


urlpatterns = [
    path(
        "ttd_admin_login/ttd_admin_homepage",
        views.ttd_admin_homepage,
        name="ttd_admin_homepage",
    ),
    path("ttd_admin_login/", views.ttd_admin_login, name="ttd_admin_login"),
    path("ttd_admin_signin/", views.ttd_admin_signin, name="ttd_admin_signin"),
    path("get_paragraph", views.get_paragraph, name="get_paragraph"),
    path("typing_tests", views.typing_tests, name="typing_tests"),
    path("get_typing_tests", views.get_typing_tests, name="get_typing_tests"),
    path("delete_paragraphs", views.delete_paragraphs, name="delete_paragraphs"),
    path("get_typing_variants", views.get_typing_variants, name="get_typing_variants"),
    path("delete_variants", views.delete_variants, name="delete_variants"),
    path("getUsers", views.getUsers, name="getUsers"),
    path("editing_tests", views.editing_tests, name="editing_tests"),
    path("getSearch", views.getSearch, name="getSearch"),
    path("getPlayerData", views.getPlayerData, name="getPlayerData"),
    path("startFrontend", views.startFrontend, name="startFrontend"),
    path("getFontendCodes", views.getFontendCodes, name="getFontendCodes"),
    path("setEventEnd", views.setEventEnd, name="setEventEnd"),
    path("setEventNext", views.setEventNext, name="setEventNext"),
    path("startTimerOne", views.startTimerOne, name="startTimerOne"),
    path(
        "getStartTimerOneCodes",
        views.getStartTimerOneCodes,
        name="getStartTimerOneCodes",
    ),
    path("startLeaderBoard", views.startLeaderBoard, name="startLeaderBoard"),
    path("getLeaderBoardCode", views.getLeaderBoardCode, name="getLeaderBoardCode"),
    path("startTypingArea", views.startTypingArea, name="startTypingArea"),
    path("getTypingAreaCode", views.getTypingAreaCode, name="getTypingAreaCode"),
    path("getEvent1Code", views.getEvent1Code, name="getEvent1Code"),
    path("getEvent2Code", views.getEvent2Code, name="getEvent2Code"),
    path("starEvent1", views.starEvent1, name="starEvent1"),
    path("starEvent2", views.starEvent2, name="starEvent2"),
]
