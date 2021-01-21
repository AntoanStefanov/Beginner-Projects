from pytube import YouTube


def download():
    data = input("Enter the link: ")

    link = YouTube(data)

    print('Title:', link.title)

    print('Views:', link.views)

    print('Length:', link.length, 'seconds')

    print('Rating:', link.rating)

    youtube_stream = link.streams.get_highest_resolution()

    print('Downloading...')
    youtube_stream.download(r'C:\Users\antoa\OneDrive\Работен Плот')
    print('Download completed!')


def main():
    download()
    while input('Do you want to download another video Y/N ? ').upper() == 'Y':
        download()


main()
