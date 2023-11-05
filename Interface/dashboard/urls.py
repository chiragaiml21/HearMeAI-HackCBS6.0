from django.urls import path

from . import views
from . import games
from . import sign_model

urlpatterns = [
    path("", views.index, name="dashboard"),
    path("statistics", views.statistics, name="statistics"),
    path("play-games/", views.play_games, name="play"), 
    
    path("test/", views.test, name="test"),
    #  path('video_feed/', sign_model.video_feed, name='video_feed'),
    
    # ================================ TRAINING ===============================
    
    path("trainings/", views.trainings, name="trainings"),
    path("hand-sign-training/", views.hand_sign_training, name="hand-sign-training"),
    path("sounds_training/", views.sounds_training, name="sounds_training"),
    
    path('get_words_by_character/', views.get_words_by_character, name='get_words_by_character'),
    path("selected_word/<int:id>", views.selected_word, name="selected_word"),
    
    path("get_word/<int:id>", views.get_word, name="get_word"),
    
    path("play_sign_video/<int:id>", views.play_sign_video, name="play_sign_video"),

# ====================================== TESTING =============================

    path("practice/", views.practice, name="practice"),
    
    # ================================ Games ===============================
    
    path("tic-tac-toe/", games.tic_tac_toe, name="tic-tac-toe"),
    path("piano", games.piano, name="piano"),
    path("guess-the-number", games.guess_the_number, name="guess-the-number"),
    path("chess", games.chess, name="chess"),
    
    path('update_points/', games.update_points, name='update_points'),
    
    # ================================ Profile work =======================
    
    path("my-profile/", views.my_profile, name="my-profile"),
    path("update-profile/", views.update_profile, name="update-profile"),
    
    path("update-avatar/<int:id>", views.update_avatar, name="update-avatar")
    
    
]