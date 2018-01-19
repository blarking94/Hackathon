import '../node_modules/jquery/dist/jquery.min.js'
import React from 'react'
import ReactDOM from 'react-dom'
import { AppContainer } from 'react-hot-loader'
import { ConnectedRouter as Router } from 'react-router-redux';
import { store, history } from './state';
import { Provider } from 'react-redux';
import App from './containers/App';


const render = Component => {
  ReactDOM.render(
    <AppContainer>
      <Provider store={store}>
        <Router history={history}>
          <Component />
        </Router>
      </Provider>
    </AppContainer>,
    document.getElementById('root')
  )
}

render(App)

// Webpack Hot Module Replacement API
if (module.hot) {
  module.hot.accept('./containers/App', () => { render(App) })
}
