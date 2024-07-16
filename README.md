<a name="readme-top"></a>
<br />

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#environment-variables">Environment variables</a></li>
        <li><a href="#deployment">Deployment</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Project Overview
This project is designed to create an API to clean product name.
The main components of the project are written in Python and include the following files:

<b>main.py</b>: The main file that contains the Flask app and route for the API.

<b>gemini_handler.py</b>: This file contains the function to clean the product name based on JSON input data with the help of Gemini LLM Model.

Docker is used to deploy Cloud Run service to download segment data using Boto3 library.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* Python 3.9
* Docker

### Environment variables

1. Secret keys are stored in **.env**.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### CI/CD

1. Create a merge request from feature branch to main branch.
2. The merge request will run through set of unit tests before merging the code into main branch.
3. If the test cases pass, then deployment will be done automatically through gitlab pipelines.

### Deployment

1. Set google cloud environment.
    ```sh
   gcloud init
   ```
2. Deploys the project on Google Cloud Run.
    ```sh
   gcloud builds submit
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

1. Install python packages.
    ```sh
   pip install -r requirements.txt
   ```
2. Export the service account credentials file.
    ```sh
   export GOOGLE_APPLICATION_CREDENTIALS=app_credentials.json
   ```
3. Set Flask App to main.py.
    ```sh
   FLASK_APP=main.py
   ```
4. Run the Flask Application.
   ```sh
   flask run
   ```
5. The Flask app provides several routes for performing various tasks related to data fetching and storage:

<ul>
  <li>/clean_product: Endpoint to process the JSON and return clean product name.</li>
</ul>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>
