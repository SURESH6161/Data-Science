from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

api_key = 'AIzaSyDjOKj7zyvfE5uaxFW7N3HbD4DhdnHlZxI'  # Replace with your actual API key
youtube = build('youtube', 'v3', developerKey=api_key)

# List of YouTube channel IDs
channel_ids = [
    'UCnz-ZXXER4jOvuED5trXfEA',  # Example Channel
    'UCZSNzBgFub_WWil6TOTYwAg',  # Netflix India Official
    'UC8md0UEGj7UbjcZtMjBVrgQ',  # Behindwoods TV
    'UC4zWG9LccdWGUlF77LZ8toA',  # Prime Video India
    'UC8lPjTzRiG37n1Q2kpz3Rfg',  # JioHotstar Tamil
    'UCq-Fj5jknLsUf-MWSy4_brA',  #T-Series
    'UCX6OQ3DkcsbYNE6H8uQQuVA',  #MrBeast
    'UCbCmjCuTUZos6Inko4u57UQ',  #Cocomelon - Nursery Rhymes
    'UCpEhnqL0y41EpW2TvWAHD7Q',  #SET India
    'UCk8GzjMOrta8yxDcKfylJYw',  #Kids Diana Show
    'UCJ5v_MCY6GNUBTO8-D3XoAg',  #WWE
    'UC295-Dw_tDNtZXFeAPAW6Aw',  #5-Minute Crafts
    'UCFFbwnve3yF62-tVXkTyHqg',  #Zee Music Company
    'UCvlE5gTbOvjiolFlEm-c_Ow',  #Vlad and Niki
    'UC-lHJZR3Gqxm24_Vd_AJ5Yw',   #PewDiePie
    'UCJplp5SjeGSdVdwsfb9Q7lQ'   # Like Nastya
]

# Function to get YouTube channel statistics
def get_channel_stats(youtube, channel_id):
    request = youtube.channels().list(
        part="snippet,statistics",
        id=channel_id
    )
    response = request.execute()

    data = dict(
        Channel_name=response['items'][0]['snippet']['title'],
        Subscribers=int(response['items'][0]['statistics']['subscriberCount']),
        Views=int(response['items'][0]['statistics']['viewCount']),
        Total_videos=int(response['items'][0]['statistics']['videoCount'])
    )

    return data

# Get stats for all channels
channel_data = [get_channel_stats(youtube, channel_id) for channel_id in channel_ids]

# Convert to Pandas DataFrame
df = pd.DataFrame(channel_data)

# Display the DataFrame
print(df)

# Set figure size for plots
sns.set(rc={'figure.figsize':(10, 6)})

plt.figure()
sns.barplot(x='Channel_name', y='Subscribers', data=df)
plt.xticks(rotation=90)
plt.title("Subscribers per Channel")
plt.tight_layout()

# Plot Views
plt.figure()
sns.barplot(x='Channel_name', y='Views', data=df)
plt.xticks(rotation=90)
plt.title("Total Views per Channel")
plt.tight_layout()

# Plot Total Videos
plt.figure()
sns.barplot(x='Channel_name', y='Total_videos', data=df)
plt.xticks(rotation=90)
plt.title("Total Videos per Channel")
plt.tight_layout()

# Show the plots
plt.show()

# Save DataFrame to an Excel file
file_name = "youtube_channel_stats.xlsx"
df.to_excel(file_name, index=False)

# Uncomment below lines if running in Google Colab to download the file
# from google.colab import files
# files.download(file_name)
