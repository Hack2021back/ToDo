from django.urls import path
from to_do_api.views import home, ToDoListDateAPIViews, ToDoListTodayAPIViews, ToDoListTomorrowAPIViews, ToDoListNextWeekAPIViews


urlpatterns = [
    path("", home),
    path("to_do_list_date/<slug:date>/", ToDoListDateAPIViews.as_view()),
    path("to_do_list_today_date/", ToDoListTodayAPIViews.as_view()),
    path("to_do_list_tomorrow_date/", ToDoListTomorrowAPIViews.as_view()),
    path("to_do_list_next_week_date/", ToDoListNextWeekAPIViews.as_view()),

]
