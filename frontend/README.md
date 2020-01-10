# Frontend
### Table of Contents 
1. [Introduction](#Introduction) 
2. [Local Development](#Installation)
3. [Usage](#Usage)

<a name="Introduction"></a>

### Introduction

The frontend project is the client implentation of our application. It uses Ionic to provide easy cross platform mobile development. Ionic Framework is an open source UI toolkit for building performant, high-quality mobile and desktop apps using web technologies (HTML, CSS, and JavaScript). As a basis we use Angular.


<a name="Installation"></a>

### Local Development

Here is a guide on how to setup the development environment. This video on youtube also looks good if you want to get started with Ionic 4: https://www.youtube.com/watch?v=r2ga-iXS5i4

##### Prerequisites
1. [NodeJS](https://nodejs.org/en/)
    Download the latest version and make sure to install npm (Node Package Manager) as well as add the according PATH variables. Verify your installation by running this command from a command line:
    ```sh
    npm -v
    ```
    The following packages can now be installed from the command line
2. Angular
    Run
    ```sh
    npm install -g @angular/cli
    ng -v
    ```
    To install the angular cli globally on your machine. Run 2nd command to verify your installation.
3. Ionic + Cordova
    Run
    ```sh
    npm install -g ionic cordova
    ionic -v
    cordova -v
    ```
    to install Ionic and Cordova globally on your machine. Run the last two commands to verify your installation.

You are now able to start local development!

##### Start local development
Go into the frontend folder and run
```sh
npm install
```
This will install all necessary dependencies specified in the `package.json`. Make sure to always run this command after installing new components or checking out a new branch!
To start a local development server run:
```sh
ionic serve

or

npm start
```
This will run a live development server at port 8000. You can access it by navigating to `http://localhost:8000` in your browser. If you change the code, the server will automatically update and show the changes.

##### Useful Visual Studio Code Extensions
- Angular 8 Snippets, Typescript, Html, ...
- Ionic 4 Snippets
- TSLint

##### Folder Structure
`./`
Here you can find the `package.json`, `.gitignore` and the `README.md`.
`./node_modules/`
Your node dependencies installed by `npm i`. Please do not add this to git!
`./e2e/`
Contains end-to-end tests
`./src/`
This is where the magic is happening.
`./src/app/`
Here you can find the logic of the app, as well as all pages of the app.

##### Deployment
*NOTE: Deployment is usually a little bit tricky.* 

To deploy an **android** application you have to install Android Studio and the Android SDK. Refer to this page for more information: [https://ionicframework.com/docs/installation/android](https://ionicframework.com/docs/installation/android)
To build an android apk run:
```sh
ionic cordova build android
```
You will find the .apk file under `platform/android/build/outputs/apk/`.

To deploy an **ios** app you have to install Xcode (MAC only!)
For ios run:
```sh
ionic cordova build ios
```
To build a **web** app run:
```
ionic build --prod
```
You can the deploy the contents of the `www/` folder.

<a name="Usage"></a>

### Usage
##### Android
*NOTE* for this you need to have the Android SDK Manager installed! 

If you just want to use install the app on your phone use the already build .apk file under `platform/android/build/outputs/apk/`. 
You first have to activate USB debuggin on your device. You can find option under development settings.
Connect your phone with the machine and open a terminal. Run 
```sh
adb devices
```
to ensure your phone is recognized by the computer.
Run
```sh
adb install -r PATH_TO_APK
```
The app should now be installed on your phone.

##### IOS
![Ain't nobody got money for that](http://m.quickmeme.com/img/f6/f6e7db7d95e61a877a01f49cc002fdda316a104cfdccee8a2aa665c164e64428.jpg)