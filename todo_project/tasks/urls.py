from django.urls import path
from .views import Vrat_seznam_ukolu, Vloz_ukol, task_detail, nearest_deadline_task, rotate_array, kth_largest, longest_increasing_path, tasks_list

urlpatterns = [
    path("tasks/", Vrat_seznam_ukolu, name="task-list"), #get metoda zobrazí ukoly
    path("tasks/", Vloz_ukol, name="task-create"), #post metoda - ulozi ukol
    path('tasks/<int:id>/', task_detail, name='task-detail'), #implementuje všechny 3 metody podle id - get, update, delete
    path('tasks/nearest-deadline/', nearest_deadline_task, name='nearest-deadline'), #zobrazí úkol s nearest deadline
    #LeetCode
    path('api/leetcode/rotate-array/', rotate_array, name='rotate-array'),
    path('api/leetcode/kth-largest/', kth_largest, name='kth-largest'),
    path('api/leetcode/longest-increasing-path/', longest_increasing_path, name='longest-increasing-path'),
    path('tasks_list', tasks_list, name='tasks-list'),

]