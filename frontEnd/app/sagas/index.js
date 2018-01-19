import { all, takeEvery } from 'redux-saga/effects'
import * as submitSaga from './submitSaga'
import * as actions from '../constants/actionTypes'
// ****** SAGAS ******
// Creates side affects (call to API, interact with database)
// Listens for actions and dispatches other actions
// Interacts with external API's
export default function * root () {
  yield all([
    takeEvery(actions.SUBMIT_DETAILS, submitSaga.submitDetals),
  ])
}
