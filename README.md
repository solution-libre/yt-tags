# YT Find & Replace <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->
- [Requirements](#requirements)
- [Connect to the YouTube Api](#connect-to-the-youtube-api)
- [Running the project](#running-the-project)
- [Contributing](#contributing)
- [License](#license)

## Requirements
* python & pip
```
pip install -r requirements.txt
```

## Connect to the YouTube Api
1. Enable the [YouTube Data API v3](https://console.cloud.google.com/apis/library?authuser=1&project=yt-search-replace&supportedpurview=project&q=youtube)
2. Create a new PROJECT, I called mine yt-find-replace
3. Visit `APIs & Services > Credentials > Create credentials`, and generate a OAuth 2.0 Client ID.  Select `Desktop App` as the Application type.
4. You should also set up the OAuth consent screen, leave it as "testing", and add your YouTube email to the test users.
5. Download the service account credentials, rename it as `client_secrets.json` and save it in the root of this repo.  It should look something like this:
```
{
  "type": "service_account",
  "project_id": "xxx-123",
  "private_key_id": "123456",
  "private_key": "-----PRIVATE KEY-----",
  "client_email": "gspread@email.access",
  "client_id": "123456",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/"
}
```

## Running the project

**If you are running in a production environment, be sure to change/remove this line:**
```
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
```

Then run the project:

```
python ./main.py
```

It will ask for your find/replace inputs.  For example:
```
$ Find: We are fundraising for The Trevor Project from April 1, 2021 - June 30, 2021.
$ Replace: We are fundraising for American Foundation for Suicide Prevention from July 1, 2021 - September 30, 2021.
```

You will be asked to visit a URL to authorize the application.  Follow the steps to get the authorization code, and hit enter to continue.  After some time, you should see **"Done! thanks."**

The changes should appear on the video page, but it takes a while to update in YouTube Studio.

Have fun!

## Contributing

Feature suggestion? Bug to report?

__Before opening any issue, please search for existing [issues](https://github.com/telepathics/yt-find-replace/issues) (open and closed).__

Also visit the living [to do](https://github.com/telepathics/yt-find-replace/projects/1) kanban board and [discussions](https://github.com/telepathics/yt-find-replace/discussions) page.

## License
Released under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0), as extended by the [YouTube Data API samples](https://github.com/youtube/api-samples) ♡


