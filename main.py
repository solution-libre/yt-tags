#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import os
import sys

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

# Enable dry-run mode
dry_run = False

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "oauth_client.json"

new_line = "\n- - - - - -\n"
class YouTubeHandler(object):
    def __init__(self):
      # Get credentials and create an API client
      flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
      credentials = flow.run_console()

      self.yt = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)
      self.channel_info = self.get_channel_info()

    def get_channel_info(self):
        request = self.yt.channels().list(
          part="contentDetails",
          mine=True
        )
        return request.execute()

    def get_playlist_videos(self, next_page_token=None):
        upload_playlist = self.channel_info["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
        request = self.yt.playlistItems().list(
          part="snippet",
          playlistId=upload_playlist,
          maxResults=50,
          pageToken=next_page_token
        )
        return request.execute()

    def get_video(self, id):
        request = self.yt.videos().list(
          part="snippet",
          id=id
        )
        return request.execute()['items'][0]

    def set_tags(self, tags):
      response = self.get_playlist_videos()

      print(new_line)

      while ("nextPageToken" in response):
        for item in response["items"]:
          video = self.get_video(item["snippet"]["resourceId"]["videoId"])
          print("updating video: " + video["snippet"]["title"] + " https://www.youtube.com/watch?v=" + video["id"])
          self.add_missing_tags(video, tags)
        response = self.get_playlist_videos(response["nextPageToken"])

      for item in response["items"]:
          video = self.get_video(item["snippet"]["resourceId"]["videoId"])
          print("updating video: " + video["snippet"]["title"] + " https://www.youtube.com/watch?v=" + video["id"])
          self.add_missing_tags(video, tags)

    def add_missing_tags(self, video, tags):
      if 'tags' in video["snippet"]:
        video["snippet"]["tags"] = list(set(video["snippet"]["tags"]) | set(tags))
      else:
        video["snippet"]["tags"] = tags
      body={
        "id": video["id"],
        "snippet": video["snippet"]
      }
      if dry_run:
        print(body)
      else:
        request = self.yt.videos().update(
          part="snippet",
          body=body
        )
        return request.execute()

def menu():
  print(new_line + 'Enter your default tags: (One by line and press CTRL + D (Unix) or CTRL + Z (Windows) to validate)')
  tags = sys.stdin.read().splitlines()
  print(new_line)

  yt = YouTubeHandler()
  yt.set_tags(tags)

  print(new_line)
  print("Done! thanks.")

def main():
    running = True
    while running:
      running = menu()

if __name__ == "__main__":
    main()
