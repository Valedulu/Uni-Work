
def get_media_type():

    filename = input("File name: ")

    #lowercase and whitespaces
    filename_lower = filename.lower().strip()

    if filename_lower.endswith('.gif'):
        print("image/gif")
    elif filename_lower.endswith('.jpg'):
        print("image/jpeg")
    elif filename_lower.endswith('.jpeg'):
        print("image/jpeg")
    elif filename_lower.endswith('.png'):
        print("image/png")
    elif filename_lower.endswith('.pdf'):
        print("application/pdf")
    elif filename_lower.endswith('.txt'):
        print("text/plain")
    elif filename_lower.endswith('.zip'):
        print("application/zip")
    else:
        #a non extension
        print("application/octet-stream")

if __name__ == "__main__":
    get_media_type()


