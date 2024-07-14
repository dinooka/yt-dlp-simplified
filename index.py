
from operations import version_check, update
from MenuItems import dwnld_video_options, dwnld_playlist_options,main_menu

menu_options = {
    '1': dwnld_video_options,
    '2': dwnld_playlist_options,
    '3': version_check,
    '4': update,
}

while True:
    main_menu_option = main_menu()
    if main_menu_option in menu_options:
        menu_options[main_menu_option]()
    elif main_menu_option == '5':
        break