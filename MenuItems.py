from operations import download_video,download_best_video,download_playlist,download_partial_playlist

def get_url_and_location():
    url = input("Enter the url: ")
    print("\nEnter the download location(Press 'Enter' for default location, else give the folder path...)")
    location = input("Download location: ")
    return url, location

def dwnld_video_options():   
    url, location = get_url_and_location()
    print("\na. Select the quality of the video")
    print("b. Download the best audio/video quality video")
    download_option = input("Select the above options: ")
    
    if(download_option=='a'):
        quality = input("Enter the frame height: ")
        if(location == ''):
            download_video(quality,url)
        else:            
            download_video(quality,url,location)       
    elif((download_option == 'b')):
        if(location == ''):
            download_best_video(url)
        else:            
            download_best_video(url,location)

def dwnld_playlist_options():   
    url, location = get_url_and_location()
    resolution = input("Enter the video resolution: ")
    print("a. Download an entire playlist")
    print("b. Download a partial playlist")
    download_option = input("Select the above options: ")
    
    if(download_option=='a'):
        if(location == ''):                        
            download_playlist(url,1,resolution)
        else:                      
            download_playlist(url,1,resolution,location)
    elif((download_option == 'b')):
        start_index = input("Enter the start index: ")
        end_index = input("Enter the end index: ")
        if(location == ''):
            download_partial_playlist(url,resolution,start_index,end_index)
        else:            
            download_partial_playlist(url,resolution,start_index,end_index,location)
        
def main_menu():
        
    print('\n***********************************************************')
    print('\t\tYoutube downloader\t')
    print('***********************************************************')

    # Main menu
    print("\nSelect the below options")
    print("\n1. Download a video")
    print("2. Download a playlist")
    print("3. Check the version")
    print("4. Update the Application")
    print("5. Close the Application")

    return input("\nSelect an option from above list(Type the number): ")