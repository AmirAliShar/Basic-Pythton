import json

#we use the json becase to easy for creating indexing
def load_data():
    try:
        with open("youtube.txt",'r') as file:
           return json.load(file)
    except FileNotFoundError:
        return []

#Save the data 
def save_data(video):
    with open("youtube.txt",'w') as file:
        json.dump(video,file)
        

def all_videos(video):
    print("\n")
    print('*' * 50)
    for index, videos in enumerate(video,start = 1):
        print(f"{index}. {videos['name']}, Duration: {videos['time']}")
    print("\n")
    print('*' * 50)

def add_videos(video):
    print("\n")
    print('*' * 50)
    name=input("Enter the name of video = ")
    time=float(input("Enter the time of video(float) = "))
    video.append({"name":name,"time":time})
    save_data(video)

def update_videos(video):
    print("\n")
    print('*' * 50)
    all_videos(video)
    index =int(input("Enter the index of video to update = "))

    if 1<= index <= len(video):
        name =input("Enter the name of video = ")
        time =float(input("Enter the time of video = "))
        video[index-1] = ({"name":name,"time":time})
        save_data(video)

    else:
        print("Index is out of range")

def delete_video(video):
    print("\n")
    print('*' * 50)
    all_videos(video)
    index =int(input("Enter the index of video to be deleted. "))
    if 1<= index <= len(video):
        del video[index-1]
        save_data(video)
    else:
        print("Index is out of range")

def main():
    print("\n")
    print('*' * 50)
    video = load_data()
    while True:
        print("Youtube Manager || Choose the Option")
        print("1: List of the videos")
        print("2: adding the videos")
        print("3: Update the videos")
        print("4: Delete the videos")
        print("5: Exit")

        choice =int(input("Enter the choice "))
        
        match choice:
            case 1:
                all_videos(video)
            case 2: 
                add_videos(video)
            case 3:
                update_videos(video)
            case 4:
                delete_video(video)

            case 5:
                break

if __name__ == "__main__":
    main()