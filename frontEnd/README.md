# React, Redux, Saga and Express Template
A basic template for a server side loading react, redux, saga and express app suitable for deployment on Heroku.

Clone the project with  `git clone https://github.com/blarking94/React-Redux-Express-Template.git`

## Requirements
This application has been built using: 
* Node v8.4.0
* NPM 5.3.0 
* Webpack 3.7.1 (install after npm with `npm install -g webpack`)
* *Optional* Heroku-CLI 6.14.36

## Key Dependencies
This application has been built using: 
* React 15.2.2
* Redux 3.6.0
* Express 4.16.1
* Webpack 3.7.1

## Set Up
Once cloned, install all the packages required for the application by running `npm install`

The template includes 3 scripts to be run with npm in the package.json file and two commands to be run optionally with heroku. 

Inside package.json:

```
"scripts": {
        "start": "node server.js",
        "start-dev": "SET NODE_ENV=development && nodemon server.js",
        "build": "SET NODE_ENV=production && webpack --config ./webpack.prod.config.js --progress --colors"
    }
```
    
To run development mode run `npm run-script start-dev` this will start the application in development mode where node, webpack and react should all hot reload - perfect for development! 

To run the application in production mode run `npm run-script build` followed by `npm start`.

### Notice for non windows users
If you aren’t running a windows based OS and you're running on Linux / Mac OS you will need to change the scripts in package.json to: 
```
"scripts": {
        "start": "node server.js",
        "start-dev": "NODE_ENV=development nodemon server.js",
        "build": "NODE_ENV=production webpack --config ./webpack.prod.config.js --progress --colors"
    }
```
    
## Using Heroku Cloud Services
Personally, I like using [Heroku](https://www.heroku.com) for deploying hobby projects on the cloud. As we can use it for free! 

If you have heroku installed, and assuming you have set up a git repository for your work already. Run the following commands to deploy your application on heroku. 

```
heroku git:remote -a name-of-my-heroku-app
git add .
git commit -am "make it better"
git push heroku master
```

Alternatively, if you would like to run the application locally on heroku run 
`heroku local web-dev` or `heroku local web` depending on if you want to launch in development or production mode.
